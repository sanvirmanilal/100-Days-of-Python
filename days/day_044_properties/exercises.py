"""Day 044: Properties and invariants. Implement these contracts after attempting them."""

class Temperature:
    'Expose read-only celsius and fahrenheit properties; fahrenheit = celsius*9/5+32. set_celsius(value) returns None and rejects values below -273.15, including at construction.'

    def __init__(self, celsius):
        raise NotImplementedError("Attempt day 044, exercise 1: Temperature")


class BoundedCounter:
    'limit is a nonnegative integer. Expose read-only value starting at 0. increment() returns new value or raises ValueError at limit without changing it.'

    def __init__(self, limit):
        raise NotImplementedError("Attempt day 044, exercise 2: BoundedCounter")


class Cart:
    'add(name, cents) stores or replaces a nonnegative price; reject negatives before changing state. remove(name) returns removed price, raising KeyError if absent. Read-only total sums prices.'

    def __init__(self):
        raise NotImplementedError("Attempt day 044, exercise 3: Cart")

