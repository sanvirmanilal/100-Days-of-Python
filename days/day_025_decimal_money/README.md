# Day 025: Decimal arithmetic

**Phase:** Text, files, and data formats

**Prerequisites:** Complete days 001–024 first.

## Learn

Decimal constructed from strings avoids binary floating-point conversion. Specify the rounding rule when converting money to a fixed precision.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 25 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `money(text)`

Return a two-decimal string rounded with Decimal ROUND_HALF_UP. text is a valid finite decimal string.

```powershell
python practice.py 25 --exercise 1
```

### 2. Application: `add_money(amounts)`

Sum valid finite decimal strings exactly, then round HALF_UP once to a two-decimal string.

```powershell
python practice.py 25 --exercise 2
```

### 3. Stretch: `allocate_cents(total, people)`

Split nonnegative integer cents evenly into people shares. First total % people shares get one extra cent. Raise ValueError for negative total or people <=0.

```powershell
python practice.py 25 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
