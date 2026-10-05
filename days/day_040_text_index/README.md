# Day 040: Project: searchable text index

**Phase:** Iteration and problem solving

**Prerequisites:** Complete days 001–039 first.

## Learn

Build an inverted index that maps terms to documents. Separate tokenization, indexing, and queries. Normalize consistently at every stage.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 40 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `tokens(text)`

Return lowercase ASCII word matches [a-z0-9]+, preserving repetition and order. Lowercase before matching.

```powershell
python practice.py 40 --exercise 1
```

### 2. Application: `build_index(documents)`

Map normalized tokens to sets of document IDs. documents maps string IDs to text; use the preceding token rules.

```powershell
python practice.py 40 --exercise 2
```

### 3. Stretch: `search(index, query)`

Normalize query with the token rules above and return sorted IDs present in ALL query terms. Empty query or any missing term returns []. Do not mutate index sets.

```powershell
python practice.py 40 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
