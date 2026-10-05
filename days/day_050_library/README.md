# Day 050: Project: lending library

**Phase:** Objects and domain models

**Prerequisites:** Complete days 001–049 first.

## Learn

Model a small domain with explicit invariants. Keep available copies separate from outstanding loans and prevent invalid operations from partially updating state.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 50 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `Book(title, copies)`

Store nonempty title and nonnegative integer copies; invalid values raise ValueError. available() returns copies.

```powershell
python practice.py 50 --exercise 1
```

### 2. Application: `LendingDesk(catalog)`

Copy title->nonnegative copy counts. borrow(title) decrements stock and returns None, raising KeyError for unknown title or ValueError when exhausted. available(title) returns stock, raising KeyError if unknown.

```powershell
python practice.py 50 --exercise 2
```

### 3. Stretch: `Library(catalog)`

Copy title->nonnegative counts. borrow(member,title) returns None, decrements stock, tracks loan, and rejects duplicate member/title or no stock with ValueError; unknown title raises KeyError. return_book(member,title) reverses a loan, or raises ValueError if absent. loans(member) returns sorted titles. available(title) returns stock.

```powershell
python practice.py 50 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
