# Day 042: Dataclasses and value objects

**Phase:** Objects and domain models

**Prerequisites:** Complete days 001–041 first.

## Learn

Dataclasses generate constructors, repr, and equality for declared fields. Frozen instances protect field assignment. Type annotations document expectations without enforcing them.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 42 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `Point(x, y)`

Implement as a frozen dataclass with x and y fields. distance_from_origin() returns Euclidean distance.

```powershell
python practice.py 42 --exercise 1
```

### 2. Application: `Product(name, price_cents)`

Implement as a frozen dataclass. Reject empty name or negative price_cents with ValueError. total(quantity) returns price times quantity; reject negative quantity.

```powershell
python practice.py 42 --exercise 2
```

### 3. Stretch: `TodoList()`

Implement as a dataclass with independent items list default. add(text) appends and returns None. pending() returns a fresh list of items.

```powershell
python practice.py 42 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
