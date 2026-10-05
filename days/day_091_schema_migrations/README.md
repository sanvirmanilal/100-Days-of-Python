# Day 091: Versioned data and migrations

**Phase:** Integration and capstones

**Prerequisites:** Complete days 001–090 first.

## Learn

Persisted data outlives code versions. Migration converts old shapes into a documented current shape without mutating the source. Reject unknown versions.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 91 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `migrate_user(record)`

v1 record {version:1,name:nonempty string} becomes {version:2,display_name:name}. v2 requires nonempty display_name and is normalized to those two keys. Invalid or unknown version raises ValueError; bool version invalid.

```powershell
python practice.py 91 --exercise 1
```

### 2. Application: `migrate_users(records)`

Migrate each record under previous rules, preserving order; any invalid record raises ValueError. Return fresh records.

```powershell
python practice.py 91 --exercise 2
```

### 3. Stretch: `migration_report(records)`

Try each migration independently. Return {users,errors}; users contains successful normalized records in order, errors contains zero-based indices of invalid records.

```powershell
python practice.py 91 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
