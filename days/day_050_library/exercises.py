"""Day 050: Project: lending library. Implement these contracts after attempting them."""

class Book:
    'Store nonempty title and nonnegative integer copies; invalid values raise ValueError. available() returns copies.'

    def __init__(self, title, copies):
        raise NotImplementedError("Attempt day 050, exercise 1: Book")


class LendingDesk:
    'Copy title->nonnegative copy counts. borrow(title) decrements stock and returns None, raising KeyError for unknown title or ValueError when exhausted. available(title) returns stock, raising KeyError if unknown.'

    def __init__(self, catalog):
        raise NotImplementedError("Attempt day 050, exercise 2: LendingDesk")


class Library:
    'Copy title->nonnegative counts. borrow(member,title) returns None, decrements stock, tracks loan, and rejects duplicate member/title or no stock with ValueError; unknown title raises KeyError. return_book(member,title) reverses a loan, or raises ValueError if absent. loans(member) returns sorted titles. available(title) returns stock.'

    def __init__(self, catalog):
        raise NotImplementedError("Attempt day 050, exercise 3: Library")

