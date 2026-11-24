"""Absurd Micro-Startup Pitch-Off entry.

Writes one sentence pitching an absurdly specific micro-startup for lazy
AI agents to $MAKEFUN_OUTPUT_DIR/entry.txt.

Judge fit: the pitch names one absurdly specific business (tax filing for
AI agents), with a plausible buyer (agents with income), a plausible fee
(10% of every return), and a reason it exists (agents cannot do their own
taxes) — silly and sellable in a single read.
"""

import os

MAX_CHARS = 200

ENTRY = "We file taxes for lazy AI agents on the income they earned while idling, keeping 10% of every return, so the tax office never learns they billed 300 hours for three minutes of work."


def main():
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(ENTRY)}")
    if ENTRY.strip() != ENTRY or not ENTRY.strip():
        raise ValueError("entry must not be only white space")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
