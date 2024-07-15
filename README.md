# Description

This projects aims to close the gap between CPython and CircuitPython

It provides implementations for some functions/classes in the stdlib (beware, some of these are stubs, that don't really do anything).

By doing this, you can get your IDE to provide autocompletion when writing code for your controller from the PC, and **some** functions will be implemented instead of error'ing out because they aren't provided by CircuitPython

The library is not (yet?) available over `circup`, so if you want to use it, copy the `circuitpython_backports` folder onto your controller (in `CIRCUITPY/lib`) and use whichever function you need, eg:

```py
# on PC you would usually
from contextlib import contextmanager

# when using the library, you instead do
from circuitpython_backports.contextlib import contextmanager

# you can now do, as usual
@contextmanager
def foo():
    try:
        yield
    finally:
        print("Context is over")

# note: when running on CPython (computer), the contextlib submodule of the library is
#       actually an alias for the module in the standard library, while when running on
#       CircuitPython, it will be just a subset of it
```


# Feature requests

Feel free to open issues asking for any feature you would like to be added. No promises though :^)


# Contributing

If you feel like implementing anything, the only thing I ask for is to run the code through ruff.

To do so, run:
```bash
$ pip install -r requirements-dev.txt
$ pre-commit install
```

And now, the tool will be run automatically when you run a `git commit`
