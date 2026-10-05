# Day 035: Combining iterables

**Phase:** Iteration and problem solving

**Prerequisites:** Complete days 001–034 first.

## Learn

itertools supplies lazy building blocks for chaining, grouping, and combinations. groupby groups consecutive keys, so sorting and grouping solve different problems.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 35 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `all_pairs(items)`

Return all index-order two-item combinations as tuples. Preserve duplicate values when they occupy different positions.

```powershell
python practice.py 35 --exercise 1
```

### 2. Application: `run_lengths(items)`

Return (item, count) tuples for consecutive equal runs.

```powershell
python practice.py 35 --exercise 2
```

### 3. Stretch: `cartesian_product(left, right)`

Return all (left_item, right_item) pairs in nested-loop order, left outermost.

```powershell
python practice.py 35 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
