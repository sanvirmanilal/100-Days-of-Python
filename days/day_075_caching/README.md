# Day 075: Caches and expiration

**Phase:** Offline APIs and concurrency

**Prerequisites:** Complete days 001–074 first.

## Learn

A cache stores reusable results. Expiry compares a supplied logical time rather than the system clock. Decide whether the exact expiry boundary counts as expired.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 75 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `fresh(entry, now)`

entry has expires numeric. Return whether now < expires; equality is expired.

```powershell
python practice.py 75 --exercise 1
```

### 2. Application: `cache_get(cache, key, now)`

cache maps keys to {value,expires}. Return value if present and fresh, otherwise None. Do not remove entries.

```powershell
python practice.py 75 --exercise 2
```

### 3. Stretch: `LRUCache(capacity)`

capacity >0 or ValueError. get(key) returns value or None and marks hits most recent. put(key,value) returns None, updates recency, and evicts least recent if over capacity. keys() returns least-to-most-recent keys.

```powershell
python practice.py 75 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
