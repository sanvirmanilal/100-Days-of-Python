# Day 010: Project: a receipt calculator

**Phase:** Foundations

**Prerequisites:** Complete days 001–009 first.

## Learn

Combine functions, loops, and mappings into a small calculation pipeline. Work in integer cents so this first project needs no floating-point rounding.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 10 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `line_total(price_cents, quantity)`

Return price times quantity. Both are nonnegative integers; reject negative inputs with ValueError.

```powershell
python practice.py 10 --exercise 1
```

### 2. Application: `subtotal(lines)`

lines is a list of (price_cents, quantity) pairs. Return their combined cost; raise ValueError for any negative price or quantity.

```powershell
python practice.py 10 --exercise 2
```

### 3. Stretch: `receipt(lines, discount_cents)`

Return {subtotal, discount, total}. Reject negative line values or negative discount. Applied discount cannot exceed subtotal.

```powershell
python practice.py 10 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
