# Day 074: Retry policy without sleeping

**Phase:** Offline APIs and concurrency

**Prerequisites:** Complete days 001–073 first.

## Learn

Retries need an explicit attempt limit and a narrow set of retryable failures. Inject sleep or compute delay schedules instead of waiting in tests.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 74 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `backoff(base, attempts)`

Return base*2**i for i in range(attempts). Reject negative base or attempts with ValueError.

```powershell
python practice.py 74 --exercise 1
```

### 2. Application: `retryable(status)`

Return True only for 408, 429, and 500..599 integer status codes.

```powershell
python practice.py 74 --exercise 2
```

### 3. Stretch: `first_success(outcomes, max_attempts)`

Inspect up to max_attempts status codes. Return 1-based attempt of first 200..299, otherwise None. Stop immediately on a nonretryable failure using previous rules; max_attempts >0 or ValueError.

```powershell
python practice.py 74 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
