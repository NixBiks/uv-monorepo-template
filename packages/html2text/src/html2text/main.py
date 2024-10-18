import typing as t

from attrs import define, field
from selectolax.parser import HTMLParser

DEFAULT_UNWRAP_TAGS = [
    "em",
    "strong",
    "b",
    "i",
    "span",
    "a",
    "code",
    "kbd",
    "font",
    "u",
]
DEFAULT_STRIP_TAGS = [
    "script",
    "style",
    "table",
    "sub",
    "sup",
    "head",
    "xmp",
    "iframe",
    "noembed",
    "noframes",
]


@define
class HTMLToText:
    unwrap_tags: list[str] = field(default=DEFAULT_UNWRAP_TAGS)
    strip_tags: list[str] = DEFAULT_STRIP_TAGS
    detect_encoding: bool = True
    use_meta_tags: bool = True
    decode_errors: t.Literal["strict", "ignore", "replace"] = "ignore"

    def parse(self, html: str) -> str:
        parsed_html = HTMLParser(
            html=html.replace("\n", ""),
            detect_encoding=self.detect_encoding,
            use_meta_tags=self.use_meta_tags,
            decode_errors=self.decode_errors,
        )
        if len(self.unwrap_tags) > 0:
            parsed_html.unwrap_tags(self.unwrap_tags)
        if len(self.strip_tags) > 0:
            parsed_html.strip_tags(self.strip_tags)

        body = parsed_html.body
        if body is None:
            raise Exception("No body")

        # parse to text
        text = body.text(separator="\n\n", strip=True)

        return text.strip()
