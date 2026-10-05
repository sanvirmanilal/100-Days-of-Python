# Day 054: Binary search trees

**Phase:** Data structures and algorithms

**Prerequisites:** Complete days 001–053 first.

## Learn

A strict binary search tree has all left descendants smaller and all right descendants larger. Local child comparisons alone cannot prove this invariant.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 54 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `bst_contains(tree, target)`

Search a valid strict BST represented as (value,left,right) or None; return bool.

```powershell
python practice.py 54 --exercise 1
```

### 2. Application: `bst_min(tree)`

Return smallest value in a valid strict BST; None returns None.

```powershell
python practice.py 54 --exercise 2
```

### 3. Stretch: `is_bst(tree)`

Return whether the entire tree satisfies strict BST ordering. Duplicate values are invalid; None is valid.

```powershell
python practice.py 54 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
