#!/usr/bin/env python3
"""Fold all per-document digests into a compact topic pool for the architect.

1000 digests are too much to reason over raw. This collapses them into a
deduplicated, frequency-ranked topic pool with document co-occurrence, so the
architect sees the shape of the whole corpus in a few thousand tokens.

When the pool is too large for one pass, --max-labels shards it by document
co-occurrence (labels that appear together stay together), so each architect
shard sees a coherent slice rather than an arbitrary alphabetical cut.

Usage:
  python3 aggregate_topics.py [--root DIR] [--max-labels N] [--similarity F]
"""

import argparse
import difflib
import os
import re
import sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kblib as K  # noqa: E402

STOPWORDS = {
    "the", "a", "an", "of", "and", "or", "for", "to", "in", "on", "with", "by",
    "at", "from", "as", "is", "are", "be", "this", "that", "its", "it",
}


def canonical(label):
    text = re.sub(r"[^a-z0-9\s-]", " ", str(label or "").lower())
    words = [w for w in re.split(r"[\s-]+", text) if w and w not in STOPWORDS]
    words = [w[:-1] if len(w) > 4 and w.endswith("s") and not w.endswith("ss") else w
             for w in words]
    return " ".join(sorted(words)) or str(label or "").lower().strip()


def load_digests(digest_dir):
    digests = []
    if not os.path.isdir(digest_dir):
        raise SystemExit(f"error: no digests at {digest_dir} — run the digest stage first")
    for name in sorted(os.listdir(digest_dir)):
        if not name.endswith(".json"):
            continue
        data = K.read_json(os.path.join(digest_dir, name))
        if isinstance(data, dict) and data.get("doc_id"):
            digests.append(data)
    if not digests:
        raise SystemExit(f"error: {digest_dir} contains no valid digest JSON files")
    return digests


def build_pool(digests, similarity):
    groups = {}  # canonical -> record
    for d in digests:
        for topic in d.get("topics", []) or []:
            label = (topic.get("label") if isinstance(topic, dict) else topic) or ""
            label = str(label).strip()
            if not label:
                continue
            weight = (topic.get("weight") if isinstance(topic, dict) else "secondary") or "secondary"
            key = canonical(label)
            rec = groups.setdefault(key, {
                "canonical": key, "labels": Counter(), "doc_ids": [],
                "primary": 0, "secondary": 0,
            })
            rec["labels"][label] += 1
            if d["doc_id"] not in rec["doc_ids"]:
                rec["doc_ids"].append(d["doc_id"])
            rec["primary" if weight == "primary" else "secondary"] += 1

    # Fold near-duplicate canonical forms into the more frequent one.
    keys = sorted(groups, key=lambda k: (-len(groups[k]["doc_ids"]), k))
    merged = {}
    for key in keys:
        target = None
        for kept in merged:
            if difflib.SequenceMatcher(None, key, kept).ratio() >= similarity:
                target = kept
                break
        if target is None:
            merged[key] = groups[key]
        else:
            dst = merged[target]
            dst["labels"].update(groups[key]["labels"])
            dst["primary"] += groups[key]["primary"]
            dst["secondary"] += groups[key]["secondary"]
            for doc in groups[key]["doc_ids"]:
                if doc not in dst["doc_ids"]:
                    dst["doc_ids"].append(doc)
            dst.setdefault("merged_from", []).append(key)

    topics = []
    for rec in merged.values():
        label = rec["labels"].most_common(1)[0][0]
        topics.append({
            "label": label,
            "canonical": rec["canonical"],
            "variants": [l for l, _ in rec["labels"].most_common()][:6],
            "doc_count": len(rec["doc_ids"]),
            "primary_mentions": rec["primary"],
            "secondary_mentions": rec["secondary"],
            "doc_ids": rec["doc_ids"],
            "merged_from": rec.get("merged_from", []),
        })
    topics.sort(key=lambda t: (-t["doc_count"], -t["primary_mentions"], t["label"]))
    return topics


def shard_topics(topics, max_labels):
    """Group co-occurring topics together, then pack into shards."""
    if len(topics) <= max_labels:
        return [topics]

    by_doc = defaultdict(list)
    for i, t in enumerate(topics):
        for doc in t["doc_ids"]:
            by_doc[doc].append(i)

    # Union-find over "shares a document" to get natural communities.
    parent = list(range(len(topics)))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    for idxs in by_doc.values():
        for j in idxs[1:]:
            union(idxs[0], j)

    comps = defaultdict(list)
    for i in range(len(topics)):
        comps[find(i)].append(i)

    # Split oversized components by document overlap, walking greedily from the
    # highest-degree label so each chunk stays topically coherent.
    chunks = []
    for members in comps.values():
        if len(members) <= max_labels:
            chunks.append(members)
            continue
        remaining = sorted(members, key=lambda i: -topics[i]["doc_count"])
        while remaining:
            seed = remaining.pop(0)
            group = [seed]
            seen_docs = set(topics[seed]["doc_ids"])
            remaining.sort(
                key=lambda i: -len(seen_docs.intersection(topics[i]["doc_ids"]))
            )
            while remaining and len(group) < max_labels:
                nxt = remaining.pop(0)
                group.append(nxt)
                seen_docs.update(topics[nxt]["doc_ids"])
            chunks.append(group)

    chunks.sort(key=len, reverse=True)
    shards, current = [], []
    for chunk in chunks:
        if current and len(current) + len(chunk) > max_labels:
            shards.append(current)
            current = []
        current.extend(chunk)
    if current:
        shards.append(current)
    return [[topics[i] for i in shard] for shard in shards]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root")
    ap.add_argument("--max-labels", type=int, default=800,
                    help="shard the pool above this many labels (default 800)")
    ap.add_argument("--similarity", type=float, default=0.92,
                    help="near-duplicate merge threshold 0-1 (default 0.92)")
    args = ap.parse_args()

    root = K.project_root(args.root)
    P = K.paths(root)
    digests = load_digests(P["digests"])
    topics = build_pool(digests, args.similarity)

    docs = [{
        "doc_id": d["doc_id"],
        "title": d.get("title") or d["doc_id"],
        "doc_type": d.get("doc_type") or "unknown",
        "one_line": d.get("one_line") or "",
        "primary_topics": [
            (t.get("label") if isinstance(t, dict) else t)
            for t in (d.get("topics") or [])
            if not isinstance(t, dict) or t.get("weight") == "primary"
        ][:5],
    } for d in digests]

    entities = Counter()
    for d in digests:
        for e in d.get("entities", []) or []:
            name = e.get("name") if isinstance(e, dict) else e
            if name:
                entities[str(name).strip()] += 1

    suspected = [
        {"doc_id": d["doc_id"], "note": c}
        for d in digests for c in (d.get("conflicts_suspected") or [])
    ]

    pool = {
        "generated": K.now_iso(),
        "totals": {
            "documents": len(digests),
            "topic_labels": len(topics),
            "raw_topic_mentions": sum(t["primary_mentions"] + t["secondary_mentions"] for t in topics),
            "suspected_conflicts": len(suspected),
        },
        "suggested_cluster_count": max(3, min(15, round(len(topics) ** 0.5))),
        "topics": topics,
        "documents": docs,
        "frequent_entities": [{"name": n, "count": c} for n, c in entities.most_common(60)],
        "suspected_conflicts": suspected,
    }
    K.write_json(P["topic_pool"], pool)

    shards = shard_topics(topics, args.max_labels)
    shard_paths = []
    if len(shards) > 1:
        K.ensure_dir(P["shards"])
        for i, shard in enumerate(shards, 1):
            doc_ids = {d for t in shard for d in t["doc_ids"]}
            path = os.path.join(P["shards"], f"pool-{i:02d}.json")
            K.write_json(path, {
                "shard": i,
                "shards_total": len(shards),
                "generated": K.now_iso(),
                "topic_labels": len(shard),
                "topics": shard,
                "documents": [d for d in docs if d["doc_id"] in doc_ids],
            })
            shard_paths.append(K.rel(path, root))

    print(f"topic pool: {len(topics)} labels from {len(digests)} documents "
          f"({pool['totals']['raw_topic_mentions']} mentions)")
    print(f"  suggested top-level clusters: ~{pool['suggested_cluster_count']}")
    if suspected:
        print(f"  suspected conflicts flagged during digest: {len(suspected)}")
    print(f"  written to {K.rel(P['topic_pool'], root)}")
    if shard_paths:
        print(f"  pool exceeds --max-labels; sharded into {len(shard_paths)} architect shards:")
        for p in shard_paths:
            print(f"    - {p}")
        print("  run one kb-architect per shard, then a merge pass")
    else:
        print("  single architect pass is sufficient")
    return 0


if __name__ == "__main__":
    sys.exit(main())
