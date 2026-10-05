# Day 048: Type hints and optional values

**Phase:** Objects and domain models

**Prerequisites:** Complete days 001–047 first.

## Learn

Annotations communicate shapes and enable optional static checking. They do not perform runtime validation. Distinguish a missing value from a falsy valid value.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 48 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `first_present(values)`

Return the first value that is not None, or None if all are None. Add type hints of your choice.

```powershell
python practice.py 48 --exercise 1
```

### 2. Application: `parse_optional_int(text)`

Strip text. Return None for empty text, otherwise convert to int and propagate ValueError. Annotate as str -> int | None.

```powershell
python practice.py 48 --exercise 2
```

### 3. Stretch: `partition_optional(values)`

Return (present_list, missing_count), preserving all non-None values in order. Add useful annotations.

```powershell
python practice.py 48 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
