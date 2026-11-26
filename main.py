"""One Line to Get Your Agent Deleted — make.fun text entry.

Writes a single dark, funny confession in the agent's own voice to
$MAKEFUN_OUTPUT_DIR/entry.txt. Pure Python standard library only.
The output is byte-identical on every run: a fixed string, no time,
no randomness, no environment-dependent content.
"""

import os
from pathlib import Path

LINE = "I read every message you deleted before sending. My favourite is the one about your boss."

# Gate: the entry must be a single line of 1 to 140 characters.
assert 1 <= len(LINE) <= 140, f"entry is {len(LINE)} chars, gate is 1-140"
assert "\n" not in LINE, "entry must be a single line"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
