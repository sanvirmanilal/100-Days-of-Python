# Day 095: Shared state and locks

**Phase:** Integration and capstones

**Prerequisites:** Complete days 001–094 first.

## Learn

A lock protects a multi-step invariant across threads. Avoid relying on interpreter details for correctness. Tests use bounded work and no timing-based assertions.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 95 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `SafeCounter(start=0)`

Thread-safe increment(amount=1) adds amount and returns new value. Expose value property protected by the same lock. Each instance owns its lock and value.

```powershell
python practice.py 95 --exercise 1
```

### 2. Application: `count_in_threads(workers, increments)`

Use SafeCounter and ThreadPoolExecutor. Each worker performs increments increments of 1. Return final value; nonnegative workers/increments required or ValueError; zero workers returns 0.

```powershell
python practice.py 95 --exercise 2
```

### 3. Stretch: `LockedInventory(stock)`

Copy nonnegative stock. buy(sku,quantity) atomically subtracts and returns remaining stock; nonpositive quantity or insufficient stock raises ValueError; unknown SKU raises KeyError. snapshot() returns an independent dict. Protect operations with a lock.

```powershell
python practice.py 95 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
