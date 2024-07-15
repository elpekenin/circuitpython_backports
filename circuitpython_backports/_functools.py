def lru_cache(maxsize=None):
    """Add memoization to a function, with at most `maxsize` entries (unlimited if `None`).

    When (if) maxsize is reached, the element who hasn't been used for the longest time is removed.

    Note: Only some types of arguments will be supported, due to the basic args->key conversion.
    """

    def wrapper(func):
        _cache = {}

        def inner(*args, **kwargs):
            key = str(args) + str(kwargs)

            if key in _cache:
                # edit dict to "move" key into most recent
                # (last position)
                ret = _cache.pop(key)
                _cache[key] = ret
                return ret

            ret = func(*args, **kwargs)

            # remove item if size reached
            if len(_cache) == maxsize:
                # first key == oldest
                _cache.pop(_cache.keys()[0])

            # save in cache
            _cache[key] = ret
            return ret

        return inner

    return wrapper


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


def reduce(func, iterable, initializer=None):
    iterator = iter(iterable)

    if initializer is None:
        val = next(iterator)
    else:
        val = initializer

    for i in iterator:
        val = func(val, i)

    return val


def wraps(func):
    """Decorator to maintain func's metadata when decorating it.

    This CircuitPython stub does nothing.
    """

    def wrapper(x):
        return x

    return wrapper
