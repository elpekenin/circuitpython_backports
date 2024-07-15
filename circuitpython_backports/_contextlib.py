def contextmanager(__func):
    """Create a generator-based context manager"""

    def wrapper(*args, **kwargs):
        return ContextManager(__func(*args, **kwargs))

    return wrapper


class suppress:
    """Context manager to ignore some exceptions."""

    def __init__(self, *exceptions):
        self._exc = exceptions

    def __enter__(self):
        return None

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        if exc_type is None:  # there was no exception
            return

        if issubclass(exc_type, self._exc):
            return True  # ignore expected error


class ContextManager:
    """Convenience class to create a context manager based on a generator."""

    def __init__(self, __generator):
        self._gen = __generator

    def __enter__(self) -> None:
        next(self._gen)
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        if exc_type is None:  # there was no exception
            try:
                next(self._gen)
            except StopIteration:
                return False
            else:
                raise RuntimeError("generator didn't stop")

    def __call__(self, func):
        """Support using this context manager to make a decorator."""

        def wrapper(*args, **kwargs):
            with self:
                return func(*args, **kwargs)

        return wrapper
