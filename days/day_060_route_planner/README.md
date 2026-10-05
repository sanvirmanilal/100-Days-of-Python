# Day 060: Project: weighted route planner

**Phase:** Data structures and algorithms

**Prerequisites:** Complete days 001–059 first.

## Learn

Weighted paths need accumulated costs rather than plain edge counts. Nonnegative weights permit Dijkstra; missing vertices have no outgoing edges.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 60 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `path_cost(graph, path)`

graph maps nodes to (neighbor,weight) lists with unique neighbors and nonnegative weights. Return sum along path; paths of length <=1 cost 0. Missing edge raises ValueError.

```powershell
python practice.py 60 --exercise 1
```

### 2. Application: `dijkstra_distances(graph, start)`

Return minimum costs to all reachable nodes, including start at 0. Weights are nonnegative integers; use a heap.

```powershell
python practice.py 60 --exercise 2
```

### 3. Stretch: `cheapest_route(graph, start, goal)`

Return {cost, path} or None if unreachable. For equal costs choose lexicographically smallest full path. Node names are strings; weights are strictly positive, except zero-edge start==goal.

```powershell
python practice.py 60 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
