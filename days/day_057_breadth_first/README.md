# Day 057: Breadth-first search

**Phase:** Data structures and algorithms

**Prerequisites:** Complete days 001–056 first.

## Learn

Breadth-first search uses a queue and finds shortest paths in unweighted graphs. Mark discovered vertices once and retain predecessors to reconstruct a path.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 57 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `bfs_order(graph, start)`

Return discovery order using a FIFO queue and neighbor order from adjacency lists; include start and visit each vertex once.

```powershell
python practice.py 57 --exercise 1
```

### 2. Application: `distances(graph, start)`

Return reachable vertex -> minimum directed edge count from start.

```powershell
python practice.py 57 --exercise 2
```

### 3. Stretch: `shortest_path(graph, start, goal)`

Return a shortest path as vertex list, or None. Break ties by FIFO discovery and stored neighbor order. start==goal returns [start].

```powershell
python practice.py 57 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
