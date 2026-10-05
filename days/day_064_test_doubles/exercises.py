"""Day 064: Fakes, spies, and mocks. Implement these contracts after attempting them."""

def notify_all(names, notifier):
    'Call notifier(name) once for each name in order and return number called. Stop and propagate any exception.'
    raise NotImplementedError("Attempt day 064, exercise 1: notify_all")


class Spy:
    'Callable wrapper: record positional argument tuples in calls before forwarding to function, even if it raises. Expose calls list.'

    def __init__(self, function):
        raise NotImplementedError("Attempt day 064, exercise 2: Spy")


def fallback_call(primary, secondary, value):
    'Call primary(value); call secondary(value) only if primary raises LookupError. Other errors propagate.'
    raise NotImplementedError("Attempt day 064, exercise 3: fallback_call")

