"""Day 045: Python object protocols. Implement these contracts after attempting them."""

class Playlist:
    'Copy songs at construction. Implement __len__, __iter__, and __contains__ with ordinary list behavior.'

    def __init__(self, songs):
        raise NotImplementedError("Attempt day 045, exercise 1: Playlist")


class RangeBox:
    'Reject low > high. Implement __contains__ for inclusive numeric bounds and __len__ as high-low+1. Bounds are integers.'

    def __init__(self, low, high):
        raise NotImplementedError("Attempt day 045, exercise 2: RangeBox")


class Polynomial:
    'Copy coefficients in ascending power order. __call__(x) evaluates the polynomial; __len__ returns coefficient count (including trailing zeros). Empty evaluates to 0.'

    def __init__(self, coefficients):
        raise NotImplementedError("Attempt day 045, exercise 3: Polynomial")

