from .session import Session
from .filters import bleach

session = Session()
session.register_filter(bleach, 'bleach')
