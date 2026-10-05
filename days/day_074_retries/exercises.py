"""Day 074: Retry policy without sleeping. Implement these contracts after attempting them."""

def backoff(base, attempts):
    'Return base*2**i for i in range(attempts). Reject negative base or attempts with ValueError.'
    raise NotImplementedError("Attempt day 074, exercise 1: backoff")


def retryable(status):
    'Return True only for 408, 429, and 500..599 integer status codes.'
    raise NotImplementedError("Attempt day 074, exercise 2: retryable")


def first_success(outcomes, max_attempts):
    'Inspect up to max_attempts status codes. Return 1-based attempt of first 200..299, otherwise None. Stop immediately on a nonretryable failure using previous rules; max_attempts >0 or ValueError.'
    raise NotImplementedError("Attempt day 074, exercise 3: first_success")

