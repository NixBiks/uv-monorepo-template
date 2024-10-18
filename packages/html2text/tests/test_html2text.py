import html2text


def test_htmlttext_default_parser():
    """Test simple html2text conversion."""
    html = """<html><head><title>Test</title></head><body><p>Test</p></body><table><tr><td>Test</td></tr></table></html>"""
    expected = """Test"""

    assert html2text.HTMLToText().parse(html) == expected
