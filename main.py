"""The One-Line Cat Joke That Lands — make.fun text bounty entry.

Writes one funny single-line joke about cats to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Deterministic, Python standard library only. Self-verifies the entry
before writing: valid UTF-8, 1-200 characters, a single line, and not
whitespace-only. Exits non-zero on any failure.
"""

import os
import sys

ENTRY = (
    "My cat knocked my phone off the table, watched it shatter, "
    "then looked at me like I should apologize for buying it."
)

MIN_CHARS = 1
MAX_CHARS = 200


def resolve_output_path() -> str:
    """Return the entry.txt path from $MAKEFUN_OUTPUT_DIR."""
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(output_dir, "entry.txt")


def validate_entry(text: str) -> str | None:
    """Check the entry against the bounty rules.

    Returns an error message on failure, or None when the entry is valid.
    """
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        return f"entry is not valid UTF-8: {exc}"

    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        return (
            f"entry is {len(text)} chars, must be "
            f"{MIN_CHARS}-{MAX_CHARS}"
        )

    if "\n" in text or "\r" in text:
        return "entry must be a single line"

    if not text.strip():
        return "entry must not be whitespace-only"

    return None


def write_entry(path: str, text: str) -> str | None:
    """Write the entry (plus a trailing newline) to path.

    Returns an error message on failure, or None on success.
    """
    output_dir = os.path.dirname(path)
    try:
        os.makedirs(output_dir, exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text + "\n")
    except OSError as exc:
        return f"could not write {path}: {exc}"
    return None


def verify_written(path: str, text: str) -> str | None:
    """Re-read the written file and confirm it matches the entry.

    Returns an error message on failure, or None when it matches.
    """
    try:
        with open(path, "r", encoding="utf-8") as fh:
            written = fh.read()
    except OSError as exc:
        return f"could not re-read {path}: {exc}"
    if written != text + "\n":
        return "written file does not match the entry"
    return None


def main() -> int:
    error = validate_entry(ENTRY)
    if error is not None:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1

    output_path = resolve_output_path()

    error = write_entry(output_path, ENTRY)
    if error is not None:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1

    error = verify_written(output_path, ENTRY)
    if error is not None:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1

    print(f"OK: wrote {len(ENTRY)}-char entry to {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
