# Day 093: Implementing sorting algorithms

**Phase:** Integration and capstones

**Prerequisites:** Complete days 001–092 first.

## Learn

Implement algorithms to understand their tradeoffs, even though production Python offers sorted. Output tests establish correctness; a written explanation establishes the complexity claim.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 93 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `insertion_sort(items)`

Implement insertion sort, returning a fresh ascending list. Do not use sorted or list.sort.

```powershell
python practice.py 93 --exercise 1
```

### 2. Application: `merge_sort(items)`

Implement stable merge sort, returning a fresh ascending list. Do not use sorted or list.sort.

```powershell
python practice.py 93 --exercise 2
```

### 3. Stretch: `count_inversions(items)`

Return number of i<j pairs with items[i]>items[j]. Aim for O(n log n) using a merge process; do not mutate input.

```powershell
python practice.py 93 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
