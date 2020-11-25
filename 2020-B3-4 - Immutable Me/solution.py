
class ImmutableMeansImmutableError(Exception):
    pass


class ImmutableParent(object):
    def __init__(self, **kwargs):
        vars(self).update(kwargs)

    def __setattr__(self, name, value):
        raise ImmutableMeansImmutableError(f"Cannot set {name}")
        