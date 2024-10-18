def test_core():
    try:
        import core

        core.ping()
    except ImportError:
        assert False, "core package not found"


def test_import_html2text():
    try:
        import html2text

    except ImportError:
        assert False, "html2text package not found"
        pass
