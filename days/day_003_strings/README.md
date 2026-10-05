# Day 003: Strings and formatting

**Phase:** Foundations

**Prerequisites:** Complete days 001–002 first.

## Learn

Strings are immutable sequences of characters. Methods return new strings. Formatting lets you combine text and values without changing the originals.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 3 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `shout(text)`

Return text converted to uppercase.

```powershell
python practice.py 3 --exercise 1
```

### 2. Application: `initials(first, last)`

Strip surrounding whitespace and return uppercase first letters joined by a dot and ending with a dot. Both stripped names are nonempty.

```powershell
python practice.py 3 --exercise 2
```

### 3. Stretch: `frame(text, border)`

Return three lines: border repeated len(text)+4 times, then "B TEXT B", then the border line. border is one character; text has no newline.

```powershell
python practice.py 3 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
