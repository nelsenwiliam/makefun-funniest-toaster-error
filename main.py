"""make.fun entry: The Funniest Toaster Error Message.

Writes one line (at most 120 characters) to /output/entry.txt: the error
message a kitchen toaster shows its owner when something goes wrong.

The line is a deadpan appliance error code: the toaster notices its owner
has toasted a third slice within the hour and declines, in the voice of a
small appliance that has had enough. It was picked over nine other
candidates for funniness first, freshness second (the therapist framing
appears in none of the existing entries), and tightness third — 60 chars,
no wasted word. Pure standard library only.
"""

import os

ENTRY = "E09: Third slice this hour. I am a toaster, not a therapist."
# Chosen from 10 candidates (see CANDIDATES.md): the deadpan "therapist"
# angle is fresh — none of the 3,000+ existing entries use it — and the
# punchline lands on a single read at just 60 characters.


def main() -> None:
    # The gate requires 1-120 characters of UTF-8 text, not only whitespace.
    text = ENTRY.strip()
    assert text, "entry must not be only whitespace"
    assert 1 <= len(text) <= 120, f"entry is {len(text)} chars, must be 1-120"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
