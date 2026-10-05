# Day 030: Project: expense report

**Phase:** Text, files, and data formats

**Prerequisites:** Complete days 001–029 first.

## Learn

Build a deterministic report from structured transactions. Keep cents as integers, validate records, and distinguish aggregation from presentation.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 30 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `validate_expense(record)`

Return True if record is a dict with a nonempty string category and nonnegative integer cents (bool is invalid), otherwise False. Extra keys are allowed.

```powershell
python practice.py 30 --exercise 1
```

### 2. Application: `category_totals(records)`

Return summed cents by category. Raise ValueError for any record failing the preceding contract.

```powershell
python practice.py 30 --exercise 2
```

### 3. Stretch: `expense_report(records)`

Validate as above, then return {total, categories}; categories is a list of (category, cents) sorted by total descending then category ascending.

```powershell
python practice.py 30 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
