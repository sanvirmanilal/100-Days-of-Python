# Day 072: Validating API payloads

**Phase:** Offline APIs and concurrency

**Prerequisites:** Complete days 001–071 first.

## Learn

An external payload needs validation before use. Keep error handling deterministic and avoid coercing surprising types. These exercises process local values only.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 72 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `valid_status(code)`

Return whether code is an integer excluding bool in HTTP success range 200..299.

```powershell
python practice.py 72 --exercise 1
```

### 2. Application: `validate_item(item)`

Return a fresh {id,name} dict if item is a dict with positive integer id excluding bool and nonempty string name. Otherwise raise ValueError; ignore extra keys.

```powershell
python practice.py 72 --exercise 2
```

### 3. Stretch: `decode_response(status, text)`

Reject non-success status with ValueError. Decode JSON object containing items list, validate each item as above, and return normalized records. Malformed JSON or shape raises ValueError.

```powershell
python practice.py 72 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
