"""Day 049: Enums and explicit states. Implement these contracts after attempting them."""

def traffic_next(state):
    'Return next string in cycle red -> green -> amber -> red. Raise ValueError for unknown state.'
    raise NotImplementedError("Attempt day 049, exercise 1: traffic_next")


def order_transition(state, action):
    'Allowed transitions: new/pay -> paid, new/cancel -> cancelled, paid/ship -> shipped, paid/cancel -> cancelled. All others raise ValueError. Return new state.'
    raise NotImplementedError("Attempt day 049, exercise 2: order_transition")


def run_order(actions):
    'Start at new, apply preceding transition rules, and return final state. Empty actions returns new; invalid action at any point raises ValueError.'
    raise NotImplementedError("Attempt day 049, exercise 3: run_order")

