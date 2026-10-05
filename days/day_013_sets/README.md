# Day 013: Sets and uniqueness

**Phase:** Working with collections

**Prerequisites:** Complete days 001–012 first.

## Learn

Sets store unique hashable values. Union, intersection, and difference model relationships between collections. Set iteration order is not a contract.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 13 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `unique_count(items)`

Return the number of distinct hashable items.

```powershell
python practice.py 13 --exercise 1
```

### 2. Application: `common_items(left, right)`

Return a set of items present in both inputs.

```powershell
python practice.py 13 --exercise 2
```

### 3. Stretch: `missing_numbers(numbers, n)`

Return sorted integers in 1..n absent from numbers. Ignore input values outside that range; n >=0.

```powershell
python practice.py 13 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
