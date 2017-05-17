import mistune
from bleach import clean


def import_text(t, text):
    t.text = text
    return t

def bleach(t, *args, **kwargs):
    t.html = clean(t.html, *args, **kwargs)
    return t

def strip_markup(t):
    t.html = clean(t.html, strip=True)
    return t

def strip_comments(t):
    t.html = clean(t.html, strip_comments=True)
    return t

def transpose_headers(t, levels=1):
    class HeaderTransposingRenderer(mistune.Renderer):
        def header(self, text, level, raw=None):
            level += levels
            return super(HeaderTransposingRenderer, self).header(text, level, raw=raw)

    renderer = HeaderTransposingRenderer()
    markdown = mistune.Markdown(renderer=renderer)
    t.html = markdown(t.text)
    return t
