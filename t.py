import hypermark

content = "# fuck yea\n\n<script></script>\n\nhttp://github.com"
content = "<h1>fuck yea</h1>"

# d = hypermark.text(content)
d = hypermark.html(content)
print d.text
# print d.filter('transpose_headers', levels=2).html

