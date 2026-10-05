# Day 037: Recursion and base cases

**Phase:** Iteration and problem solving

**Prerequisites:** Complete days 001–036 first.

## Learn

Recursive functions solve a smaller version of the same problem. Every path needs a base case. These exercises use small inputs; trace the call stack by hand.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 37 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `factorial(n)`

Return n! recursively; 0! is 1. Raise ValueError for negative n.

```powershell
python practice.py 37 --exercise 1
```

### 2. Application: `nested_sum(value)`

Recursively sum integers in arbitrarily nested lists. value is an integer or a list of such values.

```powershell
python practice.py 37 --exercise 2
```

### 3. Stretch: `flatten_nested(value)`

Return all non-list leaves from nested lists in order. A scalar input becomes a one-item list.

```powershell
python practice.py 37 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
