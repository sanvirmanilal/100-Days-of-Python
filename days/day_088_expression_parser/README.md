# Day 088: A tiny expression language

**Phase:** Advanced data processing

**Prerequisites:** Complete days 001–087 first.

## Learn

A parser should accept only its defined grammar. Avoid eval for user-supplied expressions. Today the grammar uses nonnegative integers, +, *, parentheses, and whitespace.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 88 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `tokenize(expression)`

Return integer tokens and single-character + * ( ) tokens; ignore whitespace. Reject every other character with ValueError. Empty returns [].

```powershell
python practice.py 88 --exercise 1
```

### 2. Application: `evaluate_flat(expression)`

Evaluate nonempty integer (+ integer)* with whitespace allowed. No *, parentheses, signs, or adjacent integers. Invalid syntax raises ValueError. Do not use eval.

```powershell
python practice.py 88 --exercise 2
```

### 3. Stretch: `evaluate(expression)`

Evaluate the full grammar: * precedes +, parentheses override precedence. Reject empty/malformed expressions with ValueError. Do not use eval.

```powershell
python practice.py 88 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
