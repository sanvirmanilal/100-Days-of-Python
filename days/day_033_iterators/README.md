# Day 033: Iterator protocols

**Phase:** Iteration and problem solving

**Prerequisites:** Complete days 001–032 first.

## Learn

iter obtains an iterator and next consumes it. Iterators can be exhausted and need not support len or indexing. Today inputs are generic iterables.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 33 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `first_or(iterable, default=None)`

Return first item or default if empty; consume no more than one item.

```powershell
python practice.py 33 --exercise 1
```

### 2. Application: `take(iterable, n)`

Return a list of the first up to n items; n >=0. Accept generators and avoid consuming items after the selected prefix.

```powershell
python practice.py 33 --exercise 2
```

### 3. Stretch: `pairwise(iterable)`

Return a list of adjacent pairs from a single pass over iterable.

```powershell
python practice.py 33 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
