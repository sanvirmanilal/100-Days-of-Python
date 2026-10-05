# Day 036: Higher-order functions

**Phase:** Iteration and problem solving

**Prerequisites:** Complete days 001–035 first.

## Learn

Functions are values that can be passed and returned. A higher-order function accepts a callable or returns one. Tests supply functions as inputs.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 36 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `apply_all(function, items)`

Return a list of function(item) for each item in order.

```powershell
python practice.py 36 --exercise 1
```

### 2. Application: `filter_by(predicate, items)`

Return items whose predicate result is truthy, preserving order.

```powershell
python practice.py 36 --exercise 2
```

### 3. Stretch: `compose_apply(functions, value)`

Apply functions from right to left to value; empty functions returns value.

```powershell
python practice.py 36 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
