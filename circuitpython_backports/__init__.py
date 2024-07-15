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
        _contextlib as contextlib,
        _functools as functools,
        _typing as typing,
    )


__all__ = (
    "abc",
    "contextlib",
    "functools",
    "typing",
)
