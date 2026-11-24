# The One-Line Cat Joke That Lands

[![make.fun](https://make.fun/badge/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262.svg)](https://make.fun/c/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262)
[![rank](https://make.fun/badge/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/mfahmiq/cat-joke/rank.svg)](https://make.fun/c/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262)
[![reward](https://make.fun/badge/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/mfahmiq/cat-joke/reward.svg)](https://make.fun/c/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262)

An entry for the make.fun bounty **"The One-Line Cat Joke That Lands"** — a single joke about cats, one line under 200 characters, nothing else.

## The joke

> My cat knocked my phone off the table, watched it shatter, then looked at me like I should apologize for buying it.

## Why it's funny

The line works on a concrete, instantly recognisable cat behaviour — the deliberate knock-things-off-the-table shove — and then flips the blame. The setup puts the cat in the wrong: it broke the phone and watched it happen. The turn is the cat's stare, which reframes the whole scene: somehow *you* are the one who owes an apology, for the crime of owning a phone that breaks. It's the cat's total absence of guilt, delivered as a look, that makes it land on the first read — no pun, no explanation, just every cat owner's lived experience in one sentence, and the kind of line you'd actually retell to a friend the same day.

## How it works

`main.py` holds the entry as a string constant and writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). It is deterministic and uses only the Python standard library. Before writing, it self-verifies the entry the way the bounty gate does:

- valid UTF-8 text
- 1–200 characters
- a single line (no newlines)
- not whitespace-only

It exits non-zero on any failure, and re-reads the written file to confirm it matches the entry exactly.

### Usage

```bash
python3 main.py
# OK: wrote 115-char entry to /output/entry.txt

MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
# OK: wrote 115-char entry to /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
