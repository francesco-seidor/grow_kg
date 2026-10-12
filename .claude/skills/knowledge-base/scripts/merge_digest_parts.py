#!/usr/bin/env python3
"""Merge per-segment digests of long documents into one `<doc_id>.json` digest.

plan_batches.py cuts any document over 250k chars into segments so each digest
agent reads its whole slice. Each writes .kb/digests/parts/<doc_id>.part-NN.json;
this folds the parts of a complete document into .kb/digests/<doc_id>.json, the
file everything downstream reads. A document with a missing part is reported and
left unmerged — a digest of a partial read must not pass for the whole.

Usage: python3 merge_digest_parts.py [--root DIR]
"""
import argparse
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kblib as K  # noqa: E402


def merge(parts):
    parts.sort(key=lambda p: p["_n"])
    first = parts[0]
    out = {"doc_id": first["doc_id"], "title": first.get("title", ""),
           "doc_type": first.get("doc_type", "other"), "one_line": first.get("one_line", ""),
           "segments": len(parts)}
    topics, seen = [], {}
    for p in parts:
        for t in p.get("topics") or []:
            k = t["label"].lower()
            if k not in seen:
                seen[k] = t; topics.append(t)
            elif t.get("weight") == "primary":
                seen[k]["weight"] = "primary"
    out["topics"] = topics
    def uniq(key, ident):
        got, res = set(), []
        for p in parts:
            for x in p.get(key) or []:
                k = ident(x)
                if k not in got:
                    got.add(k); res.append(x)
        return res
    out["entities"] = uniq("entities", lambda e: e["name"].lower())
    out["key_claims"] = uniq("key_claims", lambda c: c["claim"])
    out["dates_versions"] = uniq("dates_versions", lambda x: x)
    out["suggested_tags"] = uniq("suggested_tags", lambda x: x)
    out["conflicts_suspected"] = uniq("conflicts_suspected", lambda x: x)
    out["chars"] = sum(int(p.get("chars") or 0) for p in parts)
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root")
    args = ap.parse_args()
    root = K.project_root(args.root)
    P = K.paths(root)
    pdir = os.path.join(P["digests"], "parts")
    plan = K.read_json(os.path.join(P["batches"], "digest-batches.json"), {}) or {}
    expected = {}
    for b in plan.get("batches", []):
        seg = b["docs"][0].get("segment")
        if seg:
            expected[b["docs"][0]["doc_id"]] = seg["total"]
    groups = {}
    for f in glob.glob(os.path.join(pdir, "*.part-*.json")):
        m = re.match(r"(.+)\.part-(\d+)\.json$", os.path.basename(f))
        data = K.read_json(f)
        if m and data:
            data["_n"] = int(m.group(2))
            groups.setdefault(m.group(1), []).append(data)
    merged = incomplete = 0
    for doc_id, parts in sorted(groups.items()):
        total = expected.get(doc_id) or max(p["_n"] for p in parts)
        if len({p["_n"] for p in parts}) < total:
            incomplete += 1
            print(f"incomplete: {doc_id} has {len({p['_n'] for p in parts})}/{total} parts")
            continue
        K.write_json(os.path.join(P["digests"], doc_id + ".json"), merge(parts))
        merged += 1
    print(f"merged {merged} document(s); {incomplete} incomplete")
    return 1 if incomplete else 0


if __name__ == "__main__":
    sys.exit(main())
