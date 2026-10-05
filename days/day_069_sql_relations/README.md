# Day 069: Relational joins and aggregates

**Phase:** Testing and local applications

**Prerequisites:** Complete days 001–068 first.

## Learn

A join connects rows using keys. LEFT JOIN retains rows without matches. COUNT(column) ignores nulls, while COUNT(*) counts result rows.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 69 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `task_owners(connection)`

Tables users(id,name), tasks(id,user_id,done). Return (task_id,user_name) for matching users only, ordered task_id.

```powershell
python practice.py 69 --exercise 1
```

### 2. Application: `user_task_counts(connection)`

Return (user_id,count) for ALL users including those with zero tasks, ordered user_id. Same schema as above.

```powershell
python practice.py 69 --exercise 2
```

### 3. Stretch: `completion_rates(connection)`

Return (user_id, rate) for all users ordered user_id. rate is completed tasks / all tasks, or 0.0 for none. done is 0 or 1.

```powershell
python practice.py 69 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
