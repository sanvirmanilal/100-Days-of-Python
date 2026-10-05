"""Day 047: Decorators and wrappers. Implement these contracts after attempting them."""

def call_repeated(function, times, args):
    'Call function(*args) times and return the list of results; times >=0. This is the core behavior of a repetition wrapper.'
    raise NotImplementedError("Attempt day 047, exercise 1: call_repeated")


class Counted:
    'Callable wrapper with calls starting at 0. __call__(*args, **kwargs) increments calls BEFORE invoking function and returns its result; count failed calls too.'

    def __init__(self, function):
        raise NotImplementedError("Attempt day 047, exercise 2: Counted")


class Memoized:
    'Callable wrapper accepting positional hashable arguments. Cache successful return values by argument tuple; expose cache dict. Never cache exceptions.'

    def __init__(self, function):
        raise NotImplementedError("Attempt day 047, exercise 3: Memoized")

