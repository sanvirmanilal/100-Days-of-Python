"""Day 042: Dataclasses and value objects. Implement these contracts after attempting them."""

class Point:
    'Implement as a frozen dataclass with x and y fields. distance_from_origin() returns Euclidean distance.'

    def __init__(self, x, y):
        raise NotImplementedError("Attempt day 042, exercise 1: Point")


class Product:
    'Implement as a frozen dataclass. Reject empty name or negative price_cents with ValueError. total(quantity) returns price times quantity; reject negative quantity.'

    def __init__(self, name, price_cents):
        raise NotImplementedError("Attempt day 042, exercise 2: Product")


class TodoList:
    'Implement as a dataclass with independent items list default. add(text) appends and returns None. pending() returns a fresh list of items.'

    def __init__(self):
        raise NotImplementedError("Attempt day 042, exercise 3: TodoList")

