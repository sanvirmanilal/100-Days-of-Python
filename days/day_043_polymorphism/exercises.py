"""Day 043: Polymorphism and interfaces. Implement these contracts after attempting them."""

class FixedDiscount:
    'Reject negative cents. apply(total) returns max(0, total-cents); total is nonnegative.'

    def __init__(self, cents):
        raise NotImplementedError("Attempt day 043, exercise 1: FixedDiscount")


class PercentDiscount:
    'Reject integer percent outside 0..100. apply(total) returns total minus floor(total*percent/100); total is nonnegative integer cents.'

    def __init__(self, percent):
        raise NotImplementedError("Attempt day 043, exercise 2: PercentDiscount")


def discounted_total(total, discounts):
    'Apply each callable discount to the running total from left to right; empty returns total. Callables accept and return a number. Practice an interchangeable interface.'
    raise NotImplementedError("Attempt day 043, exercise 3: discounted_total")

