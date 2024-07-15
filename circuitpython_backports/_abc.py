def abstractmethod(func):
    """Decorator marking a function as **must** be overriden."""
    raise NotImplementedError


class ABC:
    """Class used as the base for abstract classes.

    This CircuitPython stub does nothing.
    """
