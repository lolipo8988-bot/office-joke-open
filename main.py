"""Write one office joke to /output/entry.txt for the make.fun competition
"Make the AI Judge Laugh: the Office Joke Open"
(u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232).

The entry is a single line about office life, 143 characters long, well
inside the gate's 1-to-200 character limit. The joke: the boss says "take
this offline" — pure meeting jargon — and the narrator takes him literally
and unplugs the router. The turn lands in the last words: HR calls it
sabotage, but IT calls it the most honest status update of the quarter,
because the whole office's real status was "offline" all along. Specific
office detail (the router, HR, IT, the status update), a misdirection that
pays off at the end, and no word that could be cut.

Deterministic: the same bytes are written on every run.
"""

import os

# The contest entry itself, kept as a single named constant so the exact
# wording lives in exactly one place. Do not rewrap or re-punctuate it:
# the submitted text must stay byte-for-byte identical on every run.
TEXT = 'My boss said, "Take this offline," so I unplugged the router. HR called it sabotage; IT called it the most honest status update of the quarter.'

# Entry constraints from the competition rules: one single line of
# UTF-8 text, 1 to 200 characters, not only white space.
EXPECTED_LENGTH = 143
MAX_LENGTH = 200


def main() -> None:
    # Guard the entry contract before writing anything: a single line of
    # exactly the expected length, so an accidental edit fails loudly
    # instead of silently submitting a different entry.
    assert "\n" not in TEXT and "\r" not in TEXT, "entry must be one line"
    assert len(TEXT) == EXPECTED_LENGTH, f"entry must be {EXPECTED_LENGTH} chars"
    assert 1 <= len(TEXT) <= MAX_LENGTH, "entry outside the gate's limits"
    assert TEXT.strip(), "entry must not be only white space"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # newline="" disables newline translation, keeping the written bytes
    # identical to TEXT on every platform.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
