"""One last text from a phone running on a single percent.

This program emits a single original message — the funniest last text a
dying phone sends — into /output/entry.txt, or into $MAKEFUN_OUTPUT_DIR
when the grader points elsewhere. The same bytes come out on every run:
no network access, no randomness, nothing read from outside this file.
"""

from pathlib import Path
import os

TEXT = "Deleting myself now. Your alarm for tomorrow goes with me. Sleep in."
# No trailing newline: the gate counts characters, and one would add an
# empty second line the judge would read as part of the message.
LIMIT = 200


def _check(text):
    if not text.strip():
        raise SystemExit("the message must not be blank")
    if "\n" in text or "\r" in text:
        raise SystemExit("the message must be one line")
    if len(text) > LIMIT:
        raise SystemExit(f"the message is {len(text)} characters, over the {LIMIT} limit")


def _destination():
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(chosen) / "entry.txt"


def main():
    _check(TEXT)
    target = _destination()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(TEXT.encode("utf-8"))
    target.chmod(0o644)
    if target.read_bytes() != TEXT.encode("utf-8"):
        raise SystemExit("entry.txt does not hold the approved message")


if __name__ == "__main__":
    main()
