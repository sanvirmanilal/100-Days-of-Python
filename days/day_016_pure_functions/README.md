# Day 016: Scope and pure functions

**Phase:** Working with collections

**Prerequisites:** Complete days 001–015 first.

## Learn

Local variables belong to a call. Pure functions depend on inputs and return results without hidden state. Copy mutable values when the contract requires independence.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 16 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `increment_all(numbers, amount)`

Return a new list adding amount to each value. Do not mutate numbers.

```powershell
python practice.py 16 --exercise 1
```

### 2. Application: `with_setting(settings, key, value)`

Return a new dictionary with key assigned value. Do not mutate settings.

```powershell
python practice.py 16 --exercise 2
```

### 3. Stretch: `normalize_scores(scores)`

Return a fresh list divided by the largest score. Scores are nonnegative; if maximum is zero, return a same-length list of zeros.

```powershell
python practice.py 16 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
