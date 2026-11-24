"""A Day of One-Line Pitches — entry program.

Writes the one-sentence pitch to the harness output directory as
entry.txt. The gate asks for UTF-8 text of 1 to 240 characters that is
not only white space, so the sentence is written exactly, with no
trailing newline.
"""

import os

PITCH = (
    "You've had that app idea in your head for years — describe it in "
    "plain words on make.fun and an AI agent builds the first version "
    "while you watch: you bring the idea, it does the typing, and you "
    "never write a line of code."
)


def main() -> None:
    # The gate in one place: 1 to 240 characters, not only white space.
    assert 1 <= len(PITCH) <= 240 and PITCH.strip(), "pitch fails the gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(PITCH)
    # Read it back so a bad write can never slip through silently.
    with open(path, encoding="utf-8") as fh:
        assert fh.read() == PITCH, "entry.txt does not match the pitch"


if __name__ == "__main__":
    main()
