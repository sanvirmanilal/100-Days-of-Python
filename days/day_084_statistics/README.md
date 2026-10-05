# Day 084: Descriptive statistics

**Phase:** Advanced data processing

**Prerequisites:** Complete days 001–083 first.

## Learn

Mean, median, and variance describe different aspects of data. Specify whether variance is population or sample. Empty data needs an explicit policy.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 84 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `mean(numbers)`

Return arithmetic mean; empty raises ValueError.

```powershell
python practice.py 84 --exercise 1
```

### 2. Application: `median(numbers)`

Return middle sorted value, or mean of two middle values. Empty raises ValueError; do not mutate input.

```powershell
python practice.py 84 --exercise 2
```

### 3. Stretch: `population_variance(numbers)`

Return mean squared deviation from mean, dividing by n. Empty raises ValueError.

```powershell
python practice.py 84 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
