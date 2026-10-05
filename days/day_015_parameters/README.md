# Day 015: Defaults and function parameters

**Phase:** Working with collections

**Prerequisites:** Complete days 001–014 first.

## Learn

Defaults make optional inputs explicit. Avoid mutable default values that can retain state across calls. Keyword arguments improve readability for optional settings.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 15 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `repeat(text, times=2)`

Return text repeated times; reject negative times with ValueError.

```powershell
python practice.py 15 --exercise 1
```

### 2. Application: `join_words(words, separator=" ")`

Return words joined by separator, with no added outer separators.

```powershell
python practice.py 15 --exercise 2
```

### 3. Stretch: `add_item(item, items=None)`

Return a fresh list with item appended. None starts an empty list. Never mutate a supplied list or retain state between calls.

```powershell
python practice.py 15 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
