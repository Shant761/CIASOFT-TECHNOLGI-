#!/usr/bin/env python3
"""Simple HTML parser check for CIA SOFT landing page."""
from html.parser import HTMLParser
from typing import List, Tuple


class RecordingHTMLParser(HTMLParser):
    """HTML parser that records start/end tags to surface structure issues."""

    def __init__(self) -> None:
        super().__init__()
        self.stack: List[Tuple[str, int, int]] = []

    def handle_starttag(self, tag: str, attrs):  # type: ignore[override]
        self.stack.append((tag, self.getpos()[0], self.getpos()[1]))

    def handle_endtag(self, tag: str):  # type: ignore[override]
        if not self.stack:
            raise ValueError(f"Unexpected closing tag </{tag}> at {self.getpos()}")
        last_tag, open_line, open_col = self.stack.pop()
        if last_tag != tag:
            raise ValueError(
                "Mismatched closing tag </{tag}> at line {close_line}, column {close_col}; expected </{expected}> for tag opened at line {open_line}, column {open_col}".format(
                    tag=tag,
                    expected=last_tag,
                    close_line=self.getpos()[0],
                    close_col=self.getpos()[1],
                    open_line=open_line,
                    open_col=open_col,
                )
            )

    def close(self) -> None:  # type: ignore[override]
        super().close()
        if self.stack:
            tag, line, col = self.stack[-1]
            raise ValueError(f"Unclosed tag <{tag}> that started at line {line}, column {col}")


def main() -> None:
    parser = RecordingHTMLParser()
    with open("index.html", "r", encoding="utf-8") as html_file:
        parser.feed(html_file.read())
    parser.close()
    print("index.html parsed successfully with balanced tags")


if __name__ == "__main__":
    main()
