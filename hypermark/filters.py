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