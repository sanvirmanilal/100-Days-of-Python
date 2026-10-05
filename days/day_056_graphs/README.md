# Day 056: Graphs and reachability

**Phase:** Data structures and algorithms

**Prerequisites:** Complete days 001–055 first.

## Learn

An adjacency mapping represents a directed graph. Referenced vertices without keys have no outgoing edges. A visited set prevents infinite traversal through cycles.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 56 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `neighbors(graph, node)`

Return a fresh list of outgoing neighbors in stored order, or [] if absent.

```powershell
python practice.py 56 --exercise 1
```

### 2. Application: `reachable(graph, start)`

Return the set of vertices reachable by directed edges, including start even when absent from mapping.

```powershell
python practice.py 56 --exercise 2
```

### 3. Stretch: `has_path(graph, start, goal)`

Return whether goal is reachable from start. A zero-edge path to itself exists.

```powershell
python practice.py 56 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
