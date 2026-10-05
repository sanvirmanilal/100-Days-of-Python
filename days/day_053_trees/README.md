# Day 053: Binary trees

**Phase:** Data structures and algorithms

**Prerequisites:** Complete days 001–052 first.

## Learn

Represent a tree as None or (value, left, right). Recursion mirrors this structure. Distinguish tree height in nodes from height in edges.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 53 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `tree_size(tree)`

Return total node count; None has size 0.

```powershell
python practice.py 53 --exercise 1
```

### 2. Application: `tree_height(tree)`

Return longest root-to-leaf node count; None has height 0.

```powershell
python practice.py 53 --exercise 2
```

### 3. Stretch: `inorder(tree)`

Return values in left-root-right traversal order.

```powershell
python practice.py 53 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
