# Day 039: Algorithmic complexity

**Phase:** Iteration and problem solving

**Prerequisites:** Complete days 001–038 first.

## Learn

Complexity describes how work grows with input size. Dictionaries and sets often replace repeated scans. Correctness tests do not prove a complexity bound; explain your approach.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 39 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `has_duplicate(items)`

Return whether hashable items contain a duplicate. Aim for expected O(n) time.

```powershell
python practice.py 39 --exercise 1
```

### 2. Application: `two_sum(numbers, target)`

Return (i, j) with i < j whose values sum to target, or None. Scan j ascending; pick the earliest matching i for the first valid j. Aim for O(n).

```powershell
python practice.py 39 --exercise 2
```

### 3. Stretch: `longest_unique(text)`

Return length of the longest substring with no repeated characters. Aim for O(n) with a sliding window.

```powershell
python practice.py 39 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
