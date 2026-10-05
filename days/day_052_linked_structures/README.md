# Day 052: Linked structures

**Phase:** Data structures and algorithms

**Prerequisites:** Complete days 001–051 first.

## Learn

A linked structure follows references rather than contiguous indices. Here a chain is encoded as node ID -> (value, next ID). None terminates it.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 52 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `chain_values(nodes, head)`

Follow an acyclic valid chain and return values in order. head None returns [].

```powershell
python practice.py 52 --exercise 1
```

### 2. Application: `has_cycle(nodes, head)`

Return whether following next references revisits a node. All referenced IDs exist; head may be None.

```powershell
python practice.py 52 --exercise 2
```

### 3. Stretch: `chain_intersection(nodes, first, second)`

For two valid acyclic chains, return the first node ID along second also reachable from first, or None. Compare IDs, not values.

```powershell
python practice.py 52 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
