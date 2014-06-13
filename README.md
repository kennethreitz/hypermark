# Hypermark!

Markdown is Hypertext.

Inspirational, fast, reversible,
extendable, and filterable.

ॐ


## Current Usage

```pycon
>>> import hypermark

>>> content = "# fuck yea\nhttp://github.com\n\nemail@example.com"

>>> d = hypermark.text(content)
'<HyperText 4e65f3a109>'

>>> d.links
[u'http://github.com']

>>> d.emails
[u'email@example.com']

>>> d.hash
u'ddac9cac1b432719c5931e04bf8d97b43045b0b7'

>>> print(d.html)
<h1>fuck yea</h1>
http://github.com
```

## Filters!

```pycon
>>> d.filters('bleach').html
u'&lt;h1&gt;fuck yea&lt;/h1&gt;\n&lt;p&gt;http://github.com&lt;/p&gt;'
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
