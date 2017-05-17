from .session import Session
from .filters import bleach, strip_markup, strip_comments, transpose_headers, anchors

session = Session()

# Register the filters.
session.register_filter(filter=bleach, label='bleach', default=True)
session.register_filter(filter=strip_markup, label='strip_markup', default=True)
session.register_filter(filter=strip_comments, label='strip_comments', default=True)
session.register_filter(filter=transpose_headers, label='transpose_headers', default=True)
session.register_filter(filter=anchors, label='anchors', default=True)


# session.register_filter(bleach, 'bleach')
