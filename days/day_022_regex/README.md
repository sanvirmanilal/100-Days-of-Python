# Day 022: Regular expressions

**Phase:** Text, files, and data formats

**Prerequisites:** Complete days 001–021 first.

## Learn

Regular expressions describe text patterns. Use raw string literals for backslashes. fullmatch validates an entire string; findall extracts repeated matches.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 22 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `extract_integers(text)`

Extract signed decimal integers matching -?[0-9]+ in encounter order and return ints. A plus sign is not part of the match.

```powershell
python practice.py 22 --exercise 1
```

### 2. Application: `valid_identifier(text)`

Return whether text matches ASCII [A-Za-z_][A-Za-z0-9_]*. Keywords such as class are allowed in this exercise.

```powershell
python practice.py 22 --exercise 2
```

### 3. Stretch: `redact_emails(text)`

Replace matches of [A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,} with [redacted]. Preserve other text. This is a deliberately limited pattern.

```powershell
python practice.py 22 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
