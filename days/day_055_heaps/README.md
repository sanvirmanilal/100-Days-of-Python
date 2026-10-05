# Day 055: Heaps and priority queues

**Phase:** Data structures and algorithms

**Prerequisites:** Complete days 001–054 first.

## Learn

heapq maintains a minimum at index zero. A heap is not fully sorted. Include explicit tie-breakers in priority entries when determinism matters.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 55 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `smallest(numbers, k)`

Return up to k smallest numbers sorted ascending, including duplicates; k >=0.

```powershell
python practice.py 55 --exercise 1
```

### 2. Application: `schedule_jobs(jobs)`

jobs is a list of (priority,name). Return names ordered priority ascending then name ascending, preserving duplicates.

```powershell
python practice.py 55 --exercise 2
```

### 3. Stretch: `merge_sorted(lists)`

Return one sorted list merging ascending-sorted input lists without mutating them. Aim for O(n log k).

```powershell
python practice.py 55 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
