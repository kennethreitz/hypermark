import hashlib
import os
import re
import hashlib

from copy import deepcopy
from mistune import markdown

GRUBER_URLINTEXT_PAT = re.compile(ur'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?\xab\xbb\u201c\u201d\u2018\u2019]))')

def extract_links(text):

    links = set()
    for url in(mgroups[0] for mgroups in GRUBER_URLINTEXT_PAT.findall(text)):
        if url.startswith('http'):
            links.add(url)
    return list(links)

class Hypertext(object):

    def __init__(self):
        self.state = {}
        self.encoding = 'utf-8'

    def __repr__(self):
        return '<Hypertext {}>'.format(self.hash[:10])

    @classmethod
    def _from_text(cls, text):
        # TODO: "Get" the text from the input. (e.g. convert it if not text.)

        self = cls()
        self.text = text
        return self

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, value):
        self.__text = value

    @property
    def content(self):
        return self.text.encode(self.encoding)

    @property
    def links(self):
        return extract_links(self.text)

    @property
    def hash(self):
        return unicode(hashlib.sha256(self.content).hexdigest())

    @property
    def html(self):
        return markdown(self.text)

    def filter(self, **kwargs):
        return deepcopy(self)


def text(content):
    return Hypertext._from_text(content)
