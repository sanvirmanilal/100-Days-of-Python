# Day 063: Dependency injection

**Phase:** Testing and local applications

**Prerequisites:** Complete days 001–062 first.

## Learn

Pass changing dependencies such as clocks and external functions explicitly. Tests can then control behavior without network access or wall-clock waits.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 63 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `stamp(message, clock)`

Return {time: clock(), message: message}; call zero-argument clock once.

```powershell
python practice.py 63 --exercise 1
```

### 2. Application: `convert_prices(prices, converter)`

Return converter(price) for each price in order. Propagate exceptions.

```powershell
python practice.py 63 --exercise 2
```

### 3. Stretch: `fetch_or_default(key, fetcher, default)`

Call fetcher(key); return default only when it raises KeyError. Preserve falsy successful values; other errors propagate.

```powershell
python practice.py 63 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
