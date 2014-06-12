# Hypermark!

Markdown is Hypertext.

Inspirational, fast, reversible,
extendable, and filterable.

ॐ


## Current Usage

```pycon
>>> import hypermark

>>> content = "# fuck yea\nhttp://github.com"

>>> d = hypermark.text(content)
'<HyperText 4e65f3a109>'

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
```

## Vision (Work in Progress)

Feature ideas:

1. link extraction
2. diff generation
3. sha generation
4. md->html, html->md
5. liting?
6. header transposing
6. stripping?
7. targets for headers

This could, potentially, contain a lot of the basic functionality of wikis.org
itself — would help explain the core concepts to the world, perhaps.
