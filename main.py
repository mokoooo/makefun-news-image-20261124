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

Before anything is written, the asset is validated: it must carry
the PNG signature and stay within the competition's size cap, or the
program fails without touching the output directory. The copy itself
is atomic -- the bytes land in a temporary file inside the output
directory and are renamed into place -- so a partial output can never
be graded.

Standard library only; no network. Python 3.13 in the sandbox.
"""

import os
import sys
from pathlib import Path

ASSET_NAME = "entry.png"
DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_ENV_VAR = "MAKEFUN_OUTPUT_DIR"

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
MAX_ASSET_BYTES = 1_048_576  # competition cap: 1 MiB


def validate_asset(data: bytes) -> str | None:
    """Return an error message if the asset is not a gradable PNG."""
    if len(data) > MAX_ASSET_BYTES:
        return (
            f"asset is {len(data)} bytes, over the "
            f"{MAX_ASSET_BYTES}-byte competition cap"
        )
    if not data.startswith(PNG_SIGNATURE):
        return "asset does not start with the PNG signature"
    return None


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

    data = source.read_bytes()
    problem = validate_asset(data)
    if problem is not None:
        print(f"error: invalid asset {source}: {problem}", file=sys.stderr)
        return 1

    dest_dir = output_dir()
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / ASSET_NAME

    # Write to a temp file in the same directory, then rename, so the
    # destination only ever appears complete. The temp name is fixed:
    # no randomness or timestamps anywhere in this program.
    tmp = dest_dir / f".{ASSET_NAME}.tmp"
    try:
        tmp.write_bytes(data)
        os.replace(tmp, dest)
    except OSError as exc:
        tmp.unlink(missing_ok=True)
        print(f"error: could not write output {dest}: {exc}", file=sys.stderr)
        return 1

    # A copy must be exact; verify before claiming success so a short
    # write can never pass silently.
    if dest.read_bytes() != data:
        print(f"error: copied file differs from asset: {dest}", file=sys.stderr)
        return 1

    print(f"wrote {dest} ({dest.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
