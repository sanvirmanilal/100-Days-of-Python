# Day 099: Capstone: transaction analytics

**Phase:** Integration and capstones

**Prerequisites:** Complete days 001–098 first.

## Learn

Build an end-to-end normalization and reporting pipeline. Keep records immutable, document rejection policy, and add tests that combine duplicate IDs, invalid records, and ties.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 99 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `normalize_transaction(record)`

Require dict with nonempty string id/category, integer cents excluding bool (negative refunds allowed). Return only those three keys; invalid record raises ValueError.

```powershell
python practice.py 99 --exercise 1
```

### 2. Application: `clean_transactions(records)`

Validate each record independently, skip invalid records, keep first valid record per id, return normalized records in encounter order.

```powershell
python practice.py 99 --exercise 2
```

### 3. Stretch: `analytics_report(records)`

Clean as above. Return {count,total,by_category}; by_category is list of (category,net_cents) sorted net descending then name ascending. Retain zero totals.

```powershell
python practice.py 99 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
