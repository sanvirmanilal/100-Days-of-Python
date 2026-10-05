# Day 019: Sorting and key functions

**Phase:** Working with collections

**Prerequisites:** Complete days 001–018 first.

## Learn

sorted returns a fresh list. A key function extracts the sort criterion. Python sorting is stable: equal keys retain input order.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 19 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `sort_numbers(numbers)`

Return numbers in ascending order without mutating input.

```powershell
python practice.py 19 --exercise 1
```

### 2. Application: `sort_words(words)`

Return words sorted by length then by case-sensitive lexicographic order.

```powershell
python practice.py 19 --exercise 2
```

### 3. Stretch: `rank_players(players)`

Return records sorted by score descending, then name ascending. Each record has name and score; do not mutate input.

```powershell
python practice.py 19 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
