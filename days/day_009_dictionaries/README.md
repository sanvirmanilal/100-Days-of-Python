# Day 009: Dictionaries and lookups

**Phase:** Foundations

**Prerequisites:** Complete days 001–008 first.

## Learn

Dictionaries map unique keys to values. Use get when a missing key has a default. Iteration order follows insertion order, but equality compares mappings.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 9 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `lookup(mapping, key, default)`

Return the value for key, or default when key is absent. Stored None is a real value.

```powershell
python practice.py 9 --exercise 1
```

### 2. Application: `frequencies(items)`

Return a dictionary counting hashable items.

```powershell
python practice.py 9 --exercise 2
```

### 3. Stretch: `merge_totals(left, right)`

Return a new dictionary adding numeric values for shared keys and retaining others. Do not change either input.

```powershell
python practice.py 9 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
