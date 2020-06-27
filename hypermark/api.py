import hashlib
import os
import re
import hashlib

import html2markdown
from copy import deepcopy
from mistune import markdown

from .bootstrap import session

GRUBER_URLINTEXT_PAT = re.compile(
    r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?\xab\xbb\u201c\u201d\u2018\u2019]))"
)


EMAIL_PAT = re.compile(
ur"([a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)")

def extract_links(text):

    links = set()
    for url in (mgroups[0] for mgroups in GRUBER_URLINTEXT_PAT.findall(text)):
        if url.startswith("http"):
            links.add(url)
    return list(links)
    
    
def extract_emails(text):
    
    emails = set()
    for email in EMAIL_PAT.findall(text):
        emails.add(email)
    return list(emails)


class HyperText(object):
    def __init__(self):
        self.__html = None
        self.__text = None
        self.encoding = "utf-8"

    def __repr__(self):
        return "<HyperText {}>".format(self.hash[:10])

    @classmethod
    def _from_text(cls, text):
        # TODO: "Get" the text from the input. (e.g. convert it if not text.)

        self = cls()
        self.text = text
        return self

    @classmethod
    def _from_html(cls, html):
        self = cls()
        self.html = html
        self.text = html2markdown.convert(html)
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
    def emails(self):
        return extract_emails(self.text)

    @property
    def hash(self):
        return hashlib.sha256(self.content).hexdigest().encode("utf-8")

    @property
    def html(self):
        return markdown(self.text)

    def filter(self, label, _session=None, **kwargs):
        if _session is None:
            _session = session

        filter = session.filters[label]
        copy = deepcopy(self)

        args = filter["defaults"][0] or {}
        kwargs.update(filter["defaults"][1]) or {}

        copy = filter["callable"](copy, *args, **kwargs)

        return copy


def text(content):
    return HyperText._from_text(content)


def html(html):
    return HyperText._from_html(html)
