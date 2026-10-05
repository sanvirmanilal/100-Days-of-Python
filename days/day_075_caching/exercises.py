"""Day 075: Caches and expiration. Implement these contracts after attempting them."""

def fresh(entry, now):
    'entry has expires numeric. Return whether now < expires; equality is expired.'
    raise NotImplementedError("Attempt day 075, exercise 1: fresh")


def cache_get(cache, key, now):
    'cache maps keys to {value,expires}. Return value if present and fresh, otherwise None. Do not remove entries.'
    raise NotImplementedError("Attempt day 075, exercise 2: cache_get")


class LRUCache:
    'capacity >0 or ValueError. get(key) returns value or None and marks hits most recent. put(key,value) returns None, updates recency, and evicts least recent if over capacity. keys() returns least-to-most-recent keys.'

    def __init__(self, capacity):
        raise NotImplementedError("Attempt day 075, exercise 3: LRUCache")

