# Day 044: Properties and invariants

**Phase:** Objects and domain models

**Prerequisites:** Complete days 001–043 first.

## Learn

A property gives attribute-style access to controlled behavior. Validate before mutating state so failed updates preserve a valid instance.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 44 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `Temperature(celsius)`

Expose read-only celsius and fahrenheit properties; fahrenheit = celsius*9/5+32. set_celsius(value) returns None and rejects values below -273.15, including at construction.

```powershell
python practice.py 44 --exercise 1
```

### 2. Application: `BoundedCounter(limit)`

limit is a nonnegative integer. Expose read-only value starting at 0. increment() returns new value or raises ValueError at limit without changing it.

```powershell
python practice.py 44 --exercise 2
```

### 3. Stretch: `Cart()`

add(name, cents) stores or replaces a nonnegative price; reject negatives before changing state. remove(name) returns removed price, raising KeyError if absent. Read-only total sums prices.

```powershell
python practice.py 44 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
