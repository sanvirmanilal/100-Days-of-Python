# Day 031: Counter and defaultdict

**Phase:** Iteration and problem solving

**Prerequisites:** Complete days 001–030 first.

## Learn

collections offers common aggregation tools. Counter tracks frequencies; defaultdict creates a value when a missing key is accessed. Return ordinary dicts where required.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 31 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `most_common(items, limit)`

Return up to limit (item, count) pairs, count descending and item lexicographically ascending on ties. Items are strings; limit >=0.

```powershell
python practice.py 31 --exercise 1
```

### 2. Application: `group_lengths(words)`

Return a dict mapping lengths to word lists in input order, including duplicates.

```powershell
python practice.py 31 --exercise 2
```

### 3. Stretch: `inventory_difference(before, after)`

Return a dict of after count minus before count for all items whose counts changed. Inputs are lists of strings; omit zero differences.

```powershell
python practice.py 31 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
