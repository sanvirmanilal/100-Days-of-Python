# Day 062: Invariants and property-style tests

**Phase:** Testing and local applications

**Prerequisites:** Complete days 001–061 first.

## Learn

Example tests check selected outcomes. Invariants describe relationships across many inputs. Use deterministic loops to explore properties without adding a dependency.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 62 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `reverse_text(text)`

Return the reversed text. Add a test proving reversing twice restores input.

```powershell
python practice.py 62 --exercise 1
```

### 2. Application: `deduplicate(items)`

Return first occurrence of each hashable item in order. Add tests for idempotence and preserved membership.

```powershell
python practice.py 62 --exercise 2
```

### 3. Stretch: `encode_runs(text)`

Return consecutive (character,count) tuples. Add a test reconstructing text from the result.

```powershell
python practice.py 62 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
