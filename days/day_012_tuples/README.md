# Day 012: Tuples and unpacking

**Phase:** Working with collections

**Prerequisites:** Complete days 001–011 first.

## Learn

Tuples group related values without supporting item assignment. Unpacking gives each position a name. Structured return values can describe more than one result.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 12 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `move(point, delta)`

Return the 2D point plus delta coordinate by coordinate as a tuple.

```powershell
python practice.py 12 --exercise 1
```

### 2. Application: `bounds(numbers)`

Return (minimum, maximum), or None if empty.

```powershell
python practice.py 12 --exercise 2
```

### 3. Stretch: `zip_strict(left, right)`

Return a list of paired tuples; raise ValueError for unequal lengths.

```powershell
python practice.py 12 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
