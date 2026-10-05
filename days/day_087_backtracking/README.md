# Day 087: Backtracking search

**Phase:** Advanced data processing

**Prerequisites:** Complete days 001–086 first.

## Learn

Backtracking builds candidates and abandons invalid prefixes. Restore state after exploring a branch. Ordering rules make otherwise equivalent outputs testable.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 87 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `subsets(items)`

Return subsets by ascending bitmask, with bit i selecting items[i]; each subset is a list in original order. Input items are distinct.

```powershell
python practice.py 87 --exercise 1
```

### 2. Application: `balanced_parentheses(n)`

Return all balanced strings with n pairs sorted lexicographically. n >=0; n=0 returns [""]. Use backtracking.

```powershell
python practice.py 87 --exercise 2
```

### 3. Stretch: `n_queens_count(n)`

Count placements of n nonattacking queens on n*n board; n >=0, empty board has one placement. Use backtracking.

```powershell
python practice.py 87 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
