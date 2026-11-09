"""Port/re-implement some utilities available on CPython's standard library
that aren't part of CircuitPython.
"""

try:
    # CPython
    import abc
    import contextlib
    import functools
    import typing
except ImportError:
    # CircuitPython
    from . import (
        _abc as abc,
    )
    from . import (
        _contextlib as contextlib,
    )
    from . import (
        _functools as functools,
    )
    from . import (
        _typing as typing,
    )


__all__ = (
    "abc",
    "contextlib",
    "functools",
    "typing",
)
