"""One-line joke entry for make.fun's "The Meeting That Should Have Been
an Email" bounty.

The program writes a single funny line, at most 200 characters, to
/output/entry.txt. The draft said the meeting produced an email; the final
line tightens it into a drumbeat — minutes, people, one decision — and
lands the turn on the last word: the meeting existed so nobody had to
write the email.
"""

from pathlib import Path

JOKE = (
    "Forty-five minutes, twelve people, one decision: to send the email "
    "we were all in this meeting to avoid writing."
)


def main() -> None:
    # The gate takes 1-200 characters of real text, and the judge reads one
    # cold line, so normalise whitespace before writing it out.
    text = " ".join(JOKE.split())
    assert "\n" not in text, "joke must be a single line"
    assert 1 <= len(text) <= 200, f"joke must be 1-200 chars, got {len(text)}"
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
