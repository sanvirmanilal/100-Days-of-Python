# Day 085: Sliding windows

**Phase:** Advanced data processing

**Prerequisites:** Complete days 001–084 first.

## Learn

A fixed-size window updates as one item enters and another leaves. Reuse partial results rather than recomputing every slice. Handle windows larger than the input.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 85 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `window_sums(numbers, size)`

Return sums of every full consecutive size window. size >0 or ValueError; no full windows returns []. Aim for O(n).

```powershell
python practice.py 85 --exercise 1
```

### 2. Application: `moving_average(numbers, size)`

Return averages of full consecutive windows. Same size validation as above.

```powershell
python practice.py 85 --exercise 2
```

### 3. Stretch: `window_maxima(numbers, size)`

Return maximum of each full consecutive window; size >0 or ValueError. Aim for O(n) with a monotonic deque.

```powershell
python practice.py 85 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
