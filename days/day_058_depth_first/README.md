# Day 058: Depth-first search and dependencies

**Phase:** Data structures and algorithms

**Prerequisites:** Complete days 001–057 first.

## Learn

Depth-first search explores one branch before returning. Track active vertices to detect directed cycles. A topological ordering respects every dependency edge.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 58 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `dfs_order(graph, start)`

Return recursive preorder DFS, following neighbors in stored order and visiting each vertex once.

```powershell
python practice.py 58 --exercise 1
```

### 2. Application: `directed_cycle(graph)`

Return whether any component contains a directed cycle. Include vertices mentioned only as neighbors.

```powershell
python practice.py 58 --exercise 2
```

### 3. Stretch: `topological_order(graph)`

Return a topological ordering of all keys and neighbors. Among currently zero-indegree vertices always choose the lexicographically smallest string. Raise ValueError for cycles.

```powershell
python practice.py 58 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
