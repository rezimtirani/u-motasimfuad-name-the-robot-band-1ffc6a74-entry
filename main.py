"""Name the Robot Band — make.fun entry.

Writes one line naming a robot band to $MAKEFUN_OUTPUT_DIR/entry.txt:
The Rusty Bolts, four robots whose drummer has no rhythm, whose singer
auto-tunes himself mid-sentence, and whose debut album is just the sound
of a printer jam. Only the Python standard library is used.
"""

import os
import sys

BAND_LINE = "Meet The Rusty Bolts: four robots, one drummer with no rhythm, and a singer who auto-tunes himself mid-sentence. Their debut album is just a printer jam."

# Sealed gate from the kit's RULES.txt ("## The gate"): the scorer
# takes UTF-8 text of 1 to 200 characters. The req JSON agrees here,
# but the RULES.txt figure is the authority.
MAX_CHARS = 200


def check_line(text):
    """Return the line once it passes the sealed gate, else raise.

    The gate counts UTF-8 characters, not bytes; the line must be a
    single line, not only whitespace, with no trailing newline in the
    output file and no control characters anywhere in it.
    """
    if not isinstance(text, str):
        raise TypeError("entry line must be a string")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, gate allows 1 to {MAX_CHARS}"
        )
    if text.strip() != text or not text.strip():
        raise ValueError("entry must not be blank or padded with whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in text):
        raise ValueError("entry must not contain control characters")
    return text


def describe_line(text):
    """Summarise a line the way the sealed gate measures it.

    The gate counts UTF-8 characters, not bytes, so an ASCII line reads
    the same either way while a line with wide characters would not.
    Returns a one-line human-readable summary.
    """
    chars = len(text)
    byte_count = len(text.encode("utf-8"))
    words = len(text.split())
    return f"{chars} characters, {byte_count} UTF-8 bytes, {words} words"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    line = check_line(BAND_LINE)
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    print(f"wrote {out_path} (entry is {describe_line(line)})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
