import hypermark

content = "# fuck yea\nhttp://github.com http://wikipedia.org etc. "

d = hypermark.text(content)

print(d.html)
