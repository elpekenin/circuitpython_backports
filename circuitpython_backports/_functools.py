class partial:
    """Create a new function by storing some arguments to be passed into
    an existing function.
    """

    def __init__(self, func, *args, **kwargs):
        self._func = func
        self._args = args
        self._kwargs = kwargs

    def __call__(self, *args, **kwargs):
        kw = self._kwargs | kwargs
        return self._func(*self._args, *args, **kw)


def wraps(func):
    """Decorator to maintain func's metadata when decorating it.

    This CircuitPython stub does nothing.
    """

    def wrapper(x):
        return x

    return wrapper
