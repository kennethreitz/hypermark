import hypermark

content1 = "# fuck yea\n\n<script></script>\n\nhttp://github.com"
content2 = "<h1>fuck yea</h1>"

# d = hypermark.text(content1)
# print d.html
d = hypermark.html(content2).filter('anchors')
print d.html
# print d.filter('transpose_headers', levels=2).html

