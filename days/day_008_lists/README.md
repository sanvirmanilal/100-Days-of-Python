# Day 008: Lists and mutation

**Phase:** Foundations

**Prerequisites:** Complete days 001–007 first.

## Learn

Lists keep ordered values and can be changed. Distinguish returning a new list from mutating an input. The contracts today require fresh results.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 8 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `double_all(numbers)`

Return a new list with each number doubled. Do not mutate numbers.

```powershell
python practice.py 8 --exercise 1
```

### 2. Application: `positives(numbers)`

Return a new list containing only values >0 in original order.

```powershell
python practice.py 8 --exercise 2
```

### 3. Stretch: `running_totals(numbers)`

Return a new list of cumulative sums, preserving order.

```powershell
python practice.py 8 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
