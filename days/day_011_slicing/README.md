# Day 011: Indexing and slicing

**Phase:** Working with collections

**Prerequisites:** Complete days 001–010 first.

## Learn

Indices start at zero; negative indices count from the end. Slices can select ranges and strides without failing on short sequences.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 11 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `first_last(items)`

Return (first, last), or None for an empty list.

```powershell
python practice.py 11 --exercise 1
```

### 2. Application: `every_other(items)`

Return a list containing indices 0, 2, 4, ... without mutating input.

```powershell
python practice.py 11 --exercise 2
```

### 3. Stretch: `rotate(items, steps)`

Return a new list rotated right by steps. Negative steps rotate left; normalize steps for list length; empty stays empty.

```powershell
python practice.py 11 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
