def cast(type, value):
    """Mark a value to be a specific type for type checkers."""
    return value


def final(func):
    """This marks a method as 'should not get overriden' for type checkers.
    But does not affect functionality
    """
    return func


TYPE_CHECKING = False
"""This would be True when type checking, always False at runtime."""
