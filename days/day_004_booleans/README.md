# Day 004: Booleans and comparisons

**Phase:** Foundations

**Prerequisites:** Complete days 001–003 first.

## Learn

Comparisons produce True or False. Use and, or, and not to combine conditions. Pay attention to inclusive and exclusive boundaries.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 4 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `is_even(number)`

Return whether integer number is even.

```powershell
python practice.py 4 --exercise 1
```

### 2. Application: `in_range(value, low, high)`

Return whether low <= value <= high. Assume low <= high.

```powershell
python practice.py 4 --exercise 2
```

### 3. Stretch: `can_enter(age, has_ticket, accompanied)`

Return whether a person has a ticket and is at least 18 or is accompanied. Accompaniment never replaces a ticket.

```powershell
python practice.py 4 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
