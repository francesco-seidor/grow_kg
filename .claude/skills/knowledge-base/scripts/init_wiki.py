#!/usr/bin/env python3
"""Create the wiki/ skeleton and install the viewers into it.

Two jobs:

1. Directories and the `_meta` report stubs, so the root index can link to
   `_meta/conflicts.md`, `_meta/provenance.md` and `_meta/changelog.md` before
   the auditor has written them — without them every linker-stage validation
   reports a dangling link. Real audit output is never clobbered.

2. The viewers, copied verbatim from `assets/`: `graph-viewer.html` →
   `wiki/graph.html`, `chat-viewer.html` → `wiki/chat.html`, plus `chat-app.js`
   and the vendored d3 and Anthropic SDK into `wiki/_meta/`. They are not
   generated per build — only their data files are — so this runs first and puts
   a working page in a vault that has no data yet. Opened then, each viewer
   shows its "run /kb-build first" banner rather than a 404.

   Unlike the `_meta` stubs, these copies ARE overwritten: they are this skill's
   files, not the reader's, and a viewer fix has to be able to land. Copies are
   content-addressed, so an unchanged asset touches nothing.

Also reports any leftover Obsidian artefacts. The pipeline no longer generates
`.obsidian/` or `*.canvas`; the graph viewer is `wiki/graph.html`.

Usage:
  python3 init_wiki.py [--root DIR]
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kblib as K  # noqa: E402


# Created empty so the root index can link to them before the auditor fills them
# in. Without this, every linker-stage validation reports a dangling link.
META_STUBS = {
    "conflicts.md": (
        "Conflicts",
        "Unresolved disagreements between source documents, awaiting a human decision.",
        "No conflicts recorded yet. The auditor fills this in during the audit stage.",
    ),
    "provenance.md": (
        "Provenance",
        "Which source document fed which node, and what has not been compiled yet.",
        "No provenance recorded yet. The auditor fills this in during the audit stage.",
    ),
    "changelog.md": (
        "Changelog",
        "What each compile run added, updated, deprecated or flagged.",
        "No runs recorded yet.",
    ),
}


def write_meta_stubs(meta_dir):
    created = []
    for name, (title, description, body) in META_STUBS.items():
        path = os.path.join(meta_dir, name)
        if os.path.exists(path):
            continue  # never clobber real audit output
        front = K.dump_frontmatter(
            {"title": title, "description": description, "tags": ["kb/meta"],
             "created": K.today(), "updated": K.today()},
            order=["title", "description", "tags", "created", "updated"],
        )
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(f"---\n{front}\n---\n\n# {title}\n\n{body}\n")
        created.append(name)
    return created


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root")
    args = ap.parse_args()

    root = K.project_root(args.root)
    P = K.paths(root)
    K.ensure_dir(P["wiki"])
    K.ensure_dir(P["meta"])
    K.ensure_dir(P["router"])
    K.ensure_dir(P["wiki_vendor"])

    stubs = write_meta_stubs(P["meta"])
    print("wiki/ skeleton ready: wiki/, wiki/_meta/, wiki/_meta/router/, "
          "wiki/_meta/vendor/")
    if stubs:
        print(f"  _meta stubs created: {', '.join(stubs)}")
    else:
        print("  _meta stubs already present")

    copied, notes = K.sync_viewer_assets(P)
    if copied:
        print(f"  viewers installed: {', '.join(copied)}")
    else:
        print("  viewers already current")
    for note in notes:
        K.eprint(f"warning: {note}")

    # Reported, never deleted: these may be committed, and `.obsidian/` may hold
    # a reader's own hand-tuned settings. Wikilinks still work, so opening wiki/
    # in Obsidian remains a valid personal choice — the pipeline just stops
    # managing it. Deleting a reader's config is not this script's call.
    leftovers = K.stale_obsidian_artifacts(P["wiki"])
    if leftovers:
        print("\nnote: leftover Obsidian artefacts in wiki/ — no longer generated or")
        print("      read by this pipeline, safe to delete by hand:")
        for item in leftovers:
            print(f"        {item}")
        print("      nothing was deleted. The graph viewer is now wiki/graph.html.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
