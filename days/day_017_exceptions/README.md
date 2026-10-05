# Day 017: Exceptions and validation

**Phase:** Working with collections

**Prerequisites:** Complete days 001–016 first.

## Learn

Exceptions communicate invalid operations. Catch only errors you can handle and validate at a clear boundary. Returning None is different from raising an exception.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 17 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `parse_integer(text)`

Return int(text), accepting whitespace and signs. Return None if conversion raises ValueError. text is a string.

```powershell
python practice.py 17 --exercise 1
```

### 2. Application: `divide(a, b)`

Return a / b. Explicitly raise ValueError when b is zero.

```powershell
python practice.py 17 --exercise 2
```

### 3. Stretch: `require_keys(record, required)`

Return a new dictionary of requested keys and their values; raise KeyError if any requested key is absent.

```powershell
python practice.py 17 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
