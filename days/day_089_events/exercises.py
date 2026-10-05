"""Day 089: Event sourcing. Implement these contracts after attempting them."""

def balance_events(events):
    'Events are (kind,amount), kind deposit or withdraw, amount nonnegative. Starting at 0, return balance. Unknown kind, negative amount, or overdraft raises ValueError.'
    raise NotImplementedError("Attempt day 089, exercise 1: balance_events")


def replay_counter(events):
    'Start at 0. Events are (kind,value): set assigns value, add adds value. Return history including initial 0; unknown kind raises ValueError.'
    raise NotImplementedError("Attempt day 089, exercise 2: replay_counter")


def deduplicate_events(events):
    'Records contain id (hashable) and arbitrary other fields. Return first record for each id in original order; do not mutate records.'
    raise NotImplementedError("Attempt day 089, exercise 3: deduplicate_events")

