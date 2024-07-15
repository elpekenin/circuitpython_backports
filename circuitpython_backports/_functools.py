class partial:
    """Create a new function by storing some arguments to be passed into
    an existing function.
    """

    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def __call__(self, *args, **kwargs):
        kw = self.kwargs | kwargs
        return self.func(*self.args, *args, **kw)


def wraps(func):
    """Decorator to maintain func's metadata when decorating it.

    This CircuitPython stub does nothing.
    """

    def wrapper(x):
        return x

    return wrapper
