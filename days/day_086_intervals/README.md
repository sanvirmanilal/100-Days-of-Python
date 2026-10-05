# Day 086: Intervals and sweep lines

**Phase:** Advanced data processing

**Prerequisites:** Complete days 001–085 first.

## Learn

Represent intervals as half-open [start,end). Touching intervals do not overlap, but merging may deliberately combine them. State that policy in the contract.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 86 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `overlap(left, right)`

Return whether valid nonempty half-open intervals overlap with positive length.

```powershell
python practice.py 86 --exercise 1
```

### 2. Application: `merge_intervals(intervals)`

Return sorted merged (start,end) tuples, combining overlapping OR touching intervals. Each interval has start<end. Do not mutate input.

```powershell
python practice.py 86 --exercise 2
```

### 3. Stretch: `max_concurrent(intervals)`

Return maximum number of simultaneously active half-open intervals. Process endings before starts at equal times; all start<end.

```powershell
python practice.py 86 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
