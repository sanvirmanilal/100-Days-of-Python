# Day 028: JSON serialization

**Phase:** Text, files, and data formats

**Prerequisites:** Complete days 001–027 first.

## Learn

JSON represents portable data with objects, arrays, strings, numbers, booleans, and null. Python tuples become arrays. Decide how strictly to validate the decoded shape.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 28 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `parse_json(text)`

Return json.loads(text); malformed input raises ValueError (JSONDecodeError is a subclass).

```powershell
python practice.py 28 --exercise 1
```

### 2. Application: `canonical_json(value)`

Return json.dumps with sort_keys=True, separators=(",", ":"), ensure_ascii=False. Inputs contain JSON-compatible values.

```powershell
python practice.py 28 --exercise 2
```

### 3. Stretch: `load_users(text)`

Decode a JSON list of objects each with a nonempty string name; return names in order. Reject other shapes and invalid names with ValueError; malformed JSON also raises ValueError.

```powershell
python practice.py 28 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
