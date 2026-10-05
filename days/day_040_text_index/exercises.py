"""Day 040: Project: searchable text index. Implement these contracts after attempting them."""

def tokens(text):
    'Return lowercase ASCII word matches [a-z0-9]+, preserving repetition and order. Lowercase before matching.'
    raise NotImplementedError("Attempt day 040, exercise 1: tokens")


def build_index(documents):
    'Map normalized tokens to sets of document IDs. documents maps string IDs to text; use the preceding token rules.'
    raise NotImplementedError("Attempt day 040, exercise 2: build_index")


def search(index, query):
    'Normalize query with the token rules above and return sorted IDs present in ALL query terms. Empty query or any missing term returns []. Do not mutate index sets.'
    raise NotImplementedError("Attempt day 040, exercise 3: search")

