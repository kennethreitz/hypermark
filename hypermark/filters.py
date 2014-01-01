from bleach import clean

def import_text(t, text):
    t.text = text
    return t

def bleach(t):
    t.html = clean(t.html)