class Session(object):
    def __init__(self):
        self.filters = {}

    def register_filter(self, filter, label, default=False, *def_args, **def_kwargs):
        """Registers a given filter to the session.

        If default is True, any extra keyboard arguments given are saved
        as default arguments.
        """

        self.filters[label] = {
            'callable': filter,
            'default': default,
            'defaults': (def_args, def_kwargs)
        }

    def _iter_default_filters(self):
        for (label, filter) in self.filters.items():
            if filter['default']:
                yield filter