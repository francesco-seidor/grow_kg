#!/usr/bin/env python3
"""Create .kb/venv with the optional extraction dependencies.

Only two packages, both pure-Python and Python 3.8+ compatible:
  mammoth  — docx -> HTML preserving Word heading styles (fidelity matters)
  pyyaml   — frontmatter parsing (a fallback parser exists, but this is better)

The pipeline works without this venv: extract.py falls back to a bundled
dependency-free docx reader and kblib falls back to a mini YAML parser. The
fallbacks lose inline emphasis, so run this when you can.

Usage:
  python3 bootstrap.py [--root DIR] [--check] [--force]
"""

import argparse
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kblib as K  # noqa: E402

PACKAGES = ["mammoth>=1.6", "pyyaml>=6.0"]


def venv_python(root):
    return os.path.join(root, ".kb", "venv", "bin", "python")


def probe(python):
    """Report which optional deps are importable by the given interpreter."""
    code = (
        "import json,importlib.util as u;"
        "print(json.dumps({n: u.find_spec(n) is not None for n in ['mammoth','yaml']}))"
    )
    try:
        out = subprocess.run([python, "-c", code], capture_output=True, timeout=60)
        if out.returncode == 0:
            import json

            return json.loads(out.stdout.decode().strip())
    except Exception:
        pass
    return {"mammoth": False, "yaml": False}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root")
    ap.add_argument("--check", action="store_true", help="report status, install nothing")
    ap.add_argument("--force", action="store_true", help="recreate the venv")
    args = ap.parse_args()

    root = K.project_root(args.root)
    py = venv_python(root)

    if args.check:
        if os.path.exists(py):
            state = probe(py)
            print(f"venv: {py}")
            for name, ok in state.items():
                print(f"  {name}: {'ok' if ok else 'MISSING'}")
            print("mode: full fidelity" if all(state.values()) else "mode: degraded")
        else:
            state = probe(sys.executable)
            print("venv: absent")
            for name, ok in state.items():
                print(f"  {name} (system python): {'ok' if ok else 'MISSING'}")
            print("mode: degraded — bundled fallbacks will be used")
        return 0

    if args.force and os.path.isdir(os.path.join(root, ".kb", "venv")):
        import shutil

        shutil.rmtree(os.path.join(root, ".kb", "venv"))

    if not os.path.exists(py):
        K.ensure_dir(os.path.join(root, ".kb"))
        print(f"creating venv at {os.path.join(root, '.kb', 'venv')} ...")
        res = subprocess.run(
            [sys.executable, "-m", "venv", os.path.join(root, ".kb", "venv")],
            capture_output=True,
        )
        if res.returncode != 0:
            print("could not create the venv:", res.stderr.decode()[:500], file=sys.stderr)
            print("\nDEGRADED MODE: the pipeline will still run using bundled fallbacks\n"
                  "(docx read without inline emphasis; mini YAML parser).", file=sys.stderr)
            return 2

    print(f"installing {', '.join(PACKAGES)} ...")
    res = subprocess.run(
        [py, "-m", "pip", "install", "--quiet", "--disable-pip-version-check", *PACKAGES],
        capture_output=True,
    )
    if res.returncode != 0:
        tail = res.stderr.decode()[-800:]
        print("pip install failed:\n" + tail, file=sys.stderr)
        print("\nDEGRADED MODE: the pipeline will still run using bundled fallbacks.",
              file=sys.stderr)
        return 2

    state = probe(py)
    for name, ok in state.items():
        print(f"  {name}: {'ok' if ok else 'MISSING'}")
    print("bootstrap complete — full fidelity extraction available"
          if all(state.values()) else "bootstrap incomplete — degraded mode")
    return 0 if all(state.values()) else 2


if __name__ == "__main__":
    sys.exit(main())
