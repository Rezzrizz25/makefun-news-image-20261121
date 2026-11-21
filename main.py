#!/usr/bin/env python3
"""news-image-20261121 — make.fun entry.

Writes one image summing up the world news of Saturday 21 November 2026
to /output/entry.png. The image is held in this repository as entry.png
(a 1024x1024 PNG, 124,113 bytes, under the 1 MiB cap); the program copies
it byte-for-byte, so both runs write the same bytes. No network access,
standard library only.
"""

import hashlib
import os
import shutil
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024
MAX_BYTES = 1048576


def validate_png(path: str) -> tuple:
    """Fail loudly unless path is a valid PNG of the expected size.

    Checks the 8-byte PNG signature and the IHDR width/height, so a
    truncated or wrong-size image is caught here instead of being
    submitted silently.
    """
    with open(path, "rb") as fh:
        header = fh.read(33)
    if len(header) < 33 or header[:8] != PNG_SIGNATURE:
        raise ValueError(f"{path}: not a PNG file (bad signature)")
    if header[12:16] != b"IHDR":
        raise ValueError(f"{path}: not a PNG file (no IHDR chunk)")
    width, height = struct.unpack(">II", header[16:24])
    if (width, height) != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
        raise ValueError(
            f"{path}: expected {EXPECTED_WIDTH}x{EXPECTED_HEIGHT}, "
            f"got {width}x{height}"
        )
    size = os.path.getsize(path)
    if size > MAX_BYTES:
        raise ValueError(f"{path}: {size} bytes exceeds the 1 MiB cap")
    return width, height


def main() -> int:
    try:
        validate_png(SRC)
    except (OSError, ValueError) as exc:
        print(f"error: source image invalid: {exc}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dest)
    # Post-copy integrity check: the written file must hash exactly like
    # the source, so a partial or corrupted copy is caught, not submitted.
    with open(SRC, "rb") as fh:
        src_hash = hashlib.sha256(fh.read()).hexdigest()
    with open(dest, "rb") as fh:
        dest_hash = hashlib.sha256(fh.read()).hexdigest()
    if src_hash != dest_hash:
        print("error: copied file hash differs from source", file=sys.stderr)
        return 1
    print(f"wrote {dest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
