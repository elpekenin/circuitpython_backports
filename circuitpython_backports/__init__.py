"""Port/re-implement some utilities available on CPython's standard library
that aren't part of CircuitPython.

Some will actually work the same (or similar) but others are just no-ops
so that you can get code completion developing on computer and you can
run the same code over both interpreters.

For example:
```py
from circuitpython_backports import contextlib
```
Is equivalent, when running on computer, to:
```py
import contextlib
```
While it will only provide a subset on CircuitPython
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
