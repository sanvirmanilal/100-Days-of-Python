# Day 043: Polymorphism and interfaces

**Phase:** Objects and domain models

**Prerequisites:** Complete days 001–042 first.

## Learn

Different objects can implement the same method. Callers depend on that interface rather than concrete type. Composition often keeps designs simpler than deep inheritance.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 43 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `FixedDiscount(cents)`

Reject negative cents. apply(total) returns max(0, total-cents); total is nonnegative.

```powershell
python practice.py 43 --exercise 1
```

### 2. Application: `PercentDiscount(percent)`

Reject integer percent outside 0..100. apply(total) returns total minus floor(total*percent/100); total is nonnegative integer cents.

```powershell
python practice.py 43 --exercise 2
```

### 3. Stretch: `discounted_total(total, discounts)`

Apply each callable discount to the running total from left to right; empty returns total. Callables accept and return a number. Practice an interchangeable interface.

```powershell
python practice.py 43 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
