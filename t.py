import hypermark

from hypermark.bootstrap import session
content = "# fuck yea\n\n<script></script>\n\nhttp://github.com"


d = hypermark.text(content)

print d.filter('transpose_headers', levels=2).html
