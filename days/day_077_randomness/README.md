# Day 077: Deterministic random simulations

**Phase:** Offline APIs and concurrency

**Prerequisites:** Complete days 001–076 first.

## Learn

A local random.Random instance isolates pseudo-random state. Seeding makes a simulation reproducible. Tests should avoid global state and statistical flakiness.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 77 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `roll_dice(seed, count)`

Use local random.Random(seed); return count randint(1,6) draws. count >=0.

```powershell
python practice.py 77 --exercise 1
```

### 2. Application: `shuffled(items, seed)`

Copy items and shuffle once with local random.Random(seed); return the copy without changing input.

```powershell
python practice.py 77 --exercise 2
```

### 3. Stretch: `dice_histogram(seed, count)`

Draw count dice using the same rules above and return counts for ALL faces 1..6, including zeros.

```powershell
python practice.py 77 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
