"""Day 095: Shared state and locks. Implement these contracts after attempting them."""

class SafeCounter:
    'Thread-safe increment(amount=1) adds amount and returns new value. Expose value property protected by the same lock. Each instance owns its lock and value.'

    def __init__(self, start=0):
        raise NotImplementedError("Attempt day 095, exercise 1: SafeCounter")


def count_in_threads(workers, increments):
    'Use SafeCounter and ThreadPoolExecutor. Each worker performs increments increments of 1. Return final value; nonnegative workers/increments required or ValueError; zero workers returns 0.'
    raise NotImplementedError("Attempt day 095, exercise 2: count_in_threads")


class LockedInventory:
    'Copy nonnegative stock. buy(sku,quantity) atomically subtracts and returns remaining stock; nonpositive quantity or insufficient stock raises ValueError; unknown SKU raises KeyError. snapshot() returns an independent dict. Protect operations with a lock.'

    def __init__(self, stock):
        raise NotImplementedError("Attempt day 095, exercise 3: LockedInventory")

