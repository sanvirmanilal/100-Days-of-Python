# Day 089: Event sourcing

**Phase:** Advanced data processing

**Prerequisites:** Complete days 001–088 first.

## Learn

Events record facts in order; reducers derive current state. Replaying the same event stream should produce the same state. Reject invalid events explicitly.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 89 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `balance_events(events)`

Events are (kind,amount), kind deposit or withdraw, amount nonnegative. Starting at 0, return balance. Unknown kind, negative amount, or overdraft raises ValueError.

```powershell
python practice.py 89 --exercise 1
```

### 2. Application: `replay_counter(events)`

Start at 0. Events are (kind,value): set assigns value, add adds value. Return history including initial 0; unknown kind raises ValueError.

```powershell
python practice.py 89 --exercise 2
```

### 3. Stretch: `deduplicate_events(events)`

Records contain id (hashable) and arbitrary other fields. Return first record for each id in original order; do not mutate records.

```powershell
python practice.py 89 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
