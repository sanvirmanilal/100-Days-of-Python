# Day 068: SQLite and parameterized queries

**Phase:** Testing and local applications

**Prerequisites:** Complete days 001–067 first.

## Learn

sqlite3 works locally without a server. Use placeholders for data values, never SQL string interpolation. Tests supply an in-memory connection and own its lifetime.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 68 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `user_names(connection)`

Table users(id INTEGER, name TEXT) exists. Return names ordered by id ascending. Do not close the supplied connection.

```powershell
python practice.py 68 --exercise 1
```

### 2. Application: `find_user(connection, name)`

Query users(id INTEGER,name TEXT) using a parameter. Return smallest matching id or None.

```powershell
python practice.py 68 --exercise 2
```

### 3. Stretch: `score_totals(connection)`

Table scores(name TEXT,points INTEGER) exists. Return (name,total) tuples grouped by name ordered total descending then name ascending.

```powershell
python practice.py 68 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
