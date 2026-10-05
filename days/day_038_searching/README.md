# Day 038: Linear and binary search

**Phase:** Iteration and problem solving

**Prerequisites:** Complete days 001–037 first.

## Learn

Linear search checks each item. Binary search halves a sorted range at each step. Empty ranges and duplicate values need explicit behavior.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 38 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `linear_find(items, target)`

Return first matching index or -1 when absent.

```powershell
python practice.py 38 --exercise 1
```

### 2. Application: `binary_find(sorted_items, target)`

Return the first matching index or -1. Input is sorted ascending; implement binary search.

```powershell
python practice.py 38 --exercise 2
```

### 3. Stretch: `insertion_index(sorted_items, target)`

Return leftmost insertion position preserving ascending order. Implement binary search.

```powershell
python practice.py 38 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
