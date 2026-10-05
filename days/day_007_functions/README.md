# Day 007: Functions and decomposition

**Phase:** Foundations

**Prerequisites:** Complete days 001–006 first.

## Learn

Functions make a named operation reusable. Parameters are inputs; the return value is output. Break a multi-step operation into small helpers if that improves clarity.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 7 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `celsius_to_fahrenheit(celsius)`

Return celsius * 9 / 5 + 32.

```powershell
python practice.py 7 --exercise 1
```

### 2. Application: `clamp(value, low, high)`

Return value limited to inclusive bounds. Raise ValueError when low > high.

```powershell
python practice.py 7 --exercise 2
```

### 3. Stretch: `compound_balance(principal, rate, years)`

Return principal after years of annual multiplication by 1+rate. principal >=0, rate >=0, years is a nonnegative integer.

```powershell
python practice.py 7 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
