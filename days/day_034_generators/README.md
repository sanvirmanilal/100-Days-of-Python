# Day 034: Generator functions

**Phase:** Iteration and problem solving

**Prerequisites:** Complete days 001–033 first.

## Learn

yield suspends a function and produces one value at a time. Generator pipelines avoid materializing intermediate lists. These exercises must return iterators, not lists.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 34 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `evens(limit)`

Yield even integers from 0 through limit-1; limit >=0.

```powershell
python practice.py 34 --exercise 1
```

### 2. Application: `chunks(iterable, size)`

Yield lists of up to size items, including a final partial chunk. Raise ValueError for size <=0 when iterated.

```powershell
python practice.py 34 --exercise 2
```

### 3. Stretch: `unique_everseen(iterable)`

Yield each hashable item only on its first occurrence, preserving order.

```powershell
python practice.py 34 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
