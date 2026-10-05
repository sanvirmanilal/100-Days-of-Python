# Day 094: Atomic updates

**Phase:** Integration and capstones

**Prerequisites:** Complete days 001–093 first.

## Learn

Atomicity means all intended updates succeed together or none take effect. Validate a complete operation before exposing state. These pure functions return committed copies.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 94 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `transfer(balances, source, target, amount)`

Return fresh balances after transfer. Missing account raises KeyError; negative amount or insufficient source raises ValueError. Same source/target is a no-op after validation. Do not mutate input.

```powershell
python practice.py 94 --exercise 1
```

### 2. Application: `batch_transfers(balances, transfers)`

transfers is (source,target,amount) list. Apply previous rules sequentially to a copy; any error propagates without changing input. Return final balances.

```powershell
python practice.py 94 --exercise 2
```

### 3. Stretch: `reserve_order(stock, order)`

Return fresh stock subtracting order sku->quantity. Validate all quantities as nonnegative int excluding bool; bad quantity/insufficient stock raises ValueError, unknown SKU raises KeyError. Input unchanged on failure.

```powershell
python practice.py 94 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
