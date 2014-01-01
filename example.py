import hypermark

content = "# fuck yea\nhttp://github.com"

>>> d = hypermark.text(content)
'<Content 4e65f3a109>'

>>> d.links
(u'http://github.com')

>>> d.hash
u'b0d842acde1988fa9e3f6dcb15008e4205fe16f5'

>>> print(d.html)
<h1>fuck yea</h1>
http://github.com


# filter('name', key=val)
# filter('name', key=val)
# filter('name', key=val)
# filter(callable, key=val)