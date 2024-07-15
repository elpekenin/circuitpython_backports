def abstractmethod(func):
    """Decorator marking a function as **must** be overriden."""

    def wrapper(*args, **kwargs):
        raise NotImplementedError

    return wrapper


class ABC:
    """Class used as the base for abstract classes.

    This CircuitPython stub does nothing.
    """
