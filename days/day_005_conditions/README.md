# Day 005: Conditional decisions

**Phase:** Foundations

**Prerequisites:** Complete days 001–004 first.

## Learn

An if/elif/else chain chooses one branch. Put narrower conditions before broader ones when they overlap. Define boundary behavior before coding.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 5 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `sign(number)`

Return "positive", "negative", or "zero".

```powershell
python practice.py 5 --exercise 1
```

### 2. Application: `grade(score)`

For an integer score in 0..100, return A for >=90, B for >=80, C for >=70, D for >=60, otherwise F. Raise ValueError outside 0..100.

```powershell
python practice.py 5 --exercise 2
```

### 3. Stretch: `shipping_cost(total, member)`

Reject negative totals with ValueError. Shipping is 0 for totals >=50, otherwise 2 for members and 5 for others.

```powershell
python practice.py 5 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
