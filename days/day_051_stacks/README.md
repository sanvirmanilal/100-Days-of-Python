# Day 051: Stacks and balanced delimiters

**Phase:** Data structures and algorithms

**Prerequisites:** Complete days 001–050 first.

## Learn

A stack is last-in, first-out. It records unfinished work such as opening brackets or operators. Define malformed input behavior before processing tokens.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 51 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `reverse_with_stack(items)`

Return reversed items as a fresh list; practice append/pop.

```powershell
python practice.py 51 --exercise 1
```

### 2. Application: `balanced(text)`

Return whether (), [], {} are properly nested; ignore all other characters.

```powershell
python practice.py 51 --exercise 2
```

### 3. Stretch: `evaluate_rpn(tokens)`

Evaluate reverse Polish tokens with integer literals and operators + - *. Each operator consumes two values, left then right. Return one integer; malformed expression raises ValueError.

```powershell
python practice.py 51 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
