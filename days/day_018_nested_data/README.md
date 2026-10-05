# Day 018: Nested collections

**Phase:** Working with collections

**Prerequisites:** Complete days 001–017 first.

## Learn

Nested lists and dictionaries describe structured data. Separate navigating a record from aggregating many records. Remember that shallow copies share nested objects.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 18 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `names(records)`

Return each record["name"] in order. All records contain name.

```powershell
python practice.py 18 --exercise 1
```

### 2. Application: `group_by(records, key)`

Return a dictionary mapping each record[key] to a list of matching records in original order. All records have key; do not mutate them.

```powershell
python practice.py 18 --exercise 2
```

### 3. Stretch: `get_nested(record, path, default=None)`

Traverse dictionary keys in path. Return default if a key is absent or an intermediate value is not a dictionary. Empty path returns record.

```powershell
python practice.py 18 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
