#!/usr/bin/env python3
"""Entry program for the make.fun news-image-20261124 competition.

The entry is one image summing up the world news of Tuesday
24 November 2026. The image ships in this repository as ``entry.png``
(it was drawn by a scripted build; see the job notes). This program's
job is only to place those exact bytes where the grader looks for
them:

    <output dir>/entry.png

The output dir is ``$MAKEFUN_OUTPUT_DIR`` when that variable is set
(the local-test convention) and ``/output`` otherwise (the sandbox).
Copying a committed asset is deterministic by construction: run it
twice and the two outputs are byte-identical.

Standard library only; no network. Python 3.13 in the sandbox.
"""

import os
import shutil
import sys
from pathlib import Path

ASSET_NAME = "entry.png"
DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_ENV_VAR = "MAKEFUN_OUTPUT_DIR"


def asset_path() -> Path:
    """The committed image, sitting next to this file in /bot."""
    return Path(__file__).resolve().parent / ASSET_NAME


def output_dir() -> Path:
    """Where the grader reads the entry from."""
    override = os.environ.get(OUTPUT_ENV_VAR)
    return Path(override) if override else Path(DEFAULT_OUTPUT_DIR)


def main() -> int:
    source = asset_path()
    if not source.is_file():
        print(f"error: asset not found: {source}", file=sys.stderr)
        return 1

    dest_dir = output_dir()
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / ASSET_NAME

    shutil.copyfile(source, dest)

    # A copy must be exact; verify before claiming success so a short
    # write can never pass silently.
    if dest.read_bytes() != source.read_bytes():
        print(f"error: copied file differs from asset: {dest}", file=sys.stderr)
        return 1

    print(f"wrote {dest} ({dest.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
