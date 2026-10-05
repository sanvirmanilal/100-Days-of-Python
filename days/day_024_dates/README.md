# Day 024: Dates and timedeltas

**Phase:** Text, files, and data formats

**Prerequisites:** Complete days 001–023 first.

## Learn

The datetime module handles calendar rules. A date has no time zone; a timedelta expresses duration. Use ISO dates for unambiguous inputs.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 24 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `next_day(iso_date)`

Parse YYYY-MM-DD using date.fromisoformat and return the next date in ISO form; propagate ValueError for invalid dates.

```powershell
python practice.py 24 --exercise 1
```

### 2. Application: `days_between(start, end)`

Return end minus start in days for ISO dates; negative differences are allowed.

```powershell
python practice.py 24 --exercise 2
```

### 3. Stretch: `business_days(start, end)`

Count Monday-Friday dates in the inclusive ISO interval. Ignore holidays; return 0 when end precedes start.

```powershell
python practice.py 24 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
