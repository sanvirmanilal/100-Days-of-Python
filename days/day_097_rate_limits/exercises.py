"""Day 097: Rate limiting with logical time. Implement these contracts after attempting them."""

def requests_in_window(times, now, window):
    'Count timestamps satisfying now-window < t <= now. window >0 or ValueError; times need not be sorted.'
    raise NotImplementedError("Attempt day 097, exercise 1: requests_in_window")


def fixed_window_decisions(times, limit, window):
    'times are nondecreasing nonnegative integers. Bucket by t//window, allow first limit in each bucket. Return booleans. limit >=0, window >0 or ValueError.'
    raise NotImplementedError("Attempt day 097, exercise 2: fixed_window_decisions")


def sliding_window_decisions(times, limit, window):
    'For sorted nonnegative timestamps, allow request only if fewer than limit previously ACCEPTED timestamps lie in (t-window,t]. Rejected requests consume no capacity. Return booleans; limit >=0, window >0 or ValueError.'
    raise NotImplementedError("Attempt day 097, exercise 3: sliding_window_decisions")

