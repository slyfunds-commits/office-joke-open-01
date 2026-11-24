"""Office Joke Open R1 — "The Fastest Decision".

Writes the keeper line to /output/entry.txt.
Stdlib only (grader: python:3.13-slim, no site-packages).

Keeper: a non-meeting office ritual redefined AS a meeting. The fire drill
is the company's fastest decision — the last beat reframes the evacuation
as a decision and the company's real decisions as slower than fleeing.
Reversal test: the last clause changes what the earlier beats meant. PASS.
"""

import os

ENTRY = (
    "When the alarm goes off, the whole office files out in two minutes flat. "
    "It's the fastest decision this company has ever made."
)


def main() -> None:
    if not ENTRY.strip():
        raise SystemExit("entry is only whitespace")
    if not 1 <= len(ENTRY) <= 200:
        raise SystemExit(f"entry is {len(ENTRY)} chars, outside the 1-200 gate")
    if ENTRY != ENTRY.strip():
        raise SystemExit("entry has leading/trailing whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ENTRY:
        raise SystemExit("byte verification failed: written text differs from ENTRY")
    print(f"wrote {len(written)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
