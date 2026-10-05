"""Day 041: Classes and instance state. Implement these contracts after attempting them."""

class Counter:
    'Expose value initialized to start. increment() adds 1 and returns the new value; reset() sets value to start and returns None.'

    def __init__(self, start=0):
        raise NotImplementedError("Attempt day 041, exercise 1: Counter")


class Rectangle:
    'Store nonnegative width and height, rejecting negatives with ValueError. area() returns width*height; perimeter() returns 2*(width+height).'

    def __init__(self, width, height):
        raise NotImplementedError("Attempt day 041, exercise 2: Rectangle")


class BankAccount:
    'Expose nonnegative integer balance. deposit(amount) and withdraw(amount) return new balance; reject negative amounts, negative initial balance, or overdraft with ValueError, leaving balance unchanged.'

    def __init__(self, balance=0):
        raise NotImplementedError("Attempt day 041, exercise 3: BankAccount")

