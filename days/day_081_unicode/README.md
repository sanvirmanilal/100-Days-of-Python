# Day 081: Unicode and normalization

**Phase:** Advanced data processing

**Prerequisites:** Complete days 001–080 first.

## Learn

Text and bytes are different. Unicode can encode visually equivalent text in different sequences. Normalize when matching; casefold handles more cases than lower.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 81 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `utf8_length(text)`

Return number of bytes in UTF-8 encoding, not number of characters.

```powershell
python practice.py 81 --exercise 1
```

### 2. Application: `normalized_equal(left, right)`

Return equality after NFC normalization and casefolding each string.

```powershell
python practice.py 81 --exercise 2
```

### 3. Stretch: `unique_normalized(words)`

Normalize each word using NFC then casefold; return unique normalized strings in first occurrence order.

```powershell
python practice.py 81 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
