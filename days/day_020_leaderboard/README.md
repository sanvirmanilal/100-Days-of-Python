# Day 020: Project: leaderboard

**Phase:** Working with collections

**Prerequisites:** Complete days 001–019 first.

## Learn

Compose validation, aggregation, and sorting. Decide how duplicate names and tied scores behave, and keep the output deterministic.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 20 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `total_points(rounds)`

rounds contains (name, points) pairs. Return summed points by name. Negative points are allowed.

```powershell
python practice.py 20 --exercise 1
```

### 2. Application: `top_players(totals, limit)`

Return up to limit (name, score) tuples ordered by score descending then name ascending. Raise ValueError for negative limit.

```powershell
python practice.py 20 --exercise 2
```

### 3. Stretch: `competition_ranks(totals)`

Return (name, score, rank) tuples in descending score/name ascending order. Ties share rank and leave gaps: 1,1,3.

```powershell
python practice.py 20 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
