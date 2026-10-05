"""Day 094: Atomic updates. Implement these contracts after attempting them."""

def transfer(balances, source, target, amount):
    'Return fresh balances after transfer. Missing account raises KeyError; negative amount or insufficient source raises ValueError. Same source/target is a no-op after validation. Do not mutate input.'
    raise NotImplementedError("Attempt day 094, exercise 1: transfer")


def batch_transfers(balances, transfers):
    'transfers is (source,target,amount) list. Apply previous rules sequentially to a copy; any error propagates without changing input. Return final balances.'
    raise NotImplementedError("Attempt day 094, exercise 2: batch_transfers")


def reserve_order(stock, order):
    'Return fresh stock subtracting order sku->quantity. Validate all quantities as nonnegative int excluding bool; bad quantity/insufficient stock raises ValueError, unknown SKU raises KeyError. Input unchanged on failure.'
    raise NotImplementedError("Attempt day 094, exercise 3: reserve_order")

