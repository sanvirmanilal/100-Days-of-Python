# Day 097: Rate limiting with logical time

**Phase:** Integration and capstones

**Prerequisites:** Complete days 001–096 first.

## Learn

Rate limits operate on time windows. Inject timestamps so tests are instant and deterministic. State exactly which side of a window boundary is included.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 97 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `requests_in_window(times, now, window)`

Count timestamps satisfying now-window < t <= now. window >0 or ValueError; times need not be sorted.

```powershell
python practice.py 97 --exercise 1
```

### 2. Application: `fixed_window_decisions(times, limit, window)`

times are nondecreasing nonnegative integers. Bucket by t//window, allow first limit in each bucket. Return booleans. limit >=0, window >0 or ValueError.

```powershell
python practice.py 97 --exercise 2
```

### 3. Stretch: `sliding_window_decisions(times, limit, window)`

For sorted nonnegative timestamps, allow request only if fewer than limit previously ACCEPTED timestamps lie in (t-window,t]. Rejected requests consume no capacity. Return booleans; limit >=0, window >0 or ValueError.

```powershell
python practice.py 97 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
