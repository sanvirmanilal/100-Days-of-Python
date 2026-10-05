# Day 098: Dependency planning

**Phase:** Integration and capstones

**Prerequisites:** Complete days 001–097 first.

## Learn

Build systems map each task to prerequisites. A plan must include transitive dependencies and detect cycles. Avoid confusing prerequisite edges with execution-order edges.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 98 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `dependency_closure(dependencies, target)`

Return set of all transitive prerequisites, excluding target. Referenced missing keys have no prerequisites. Raise ValueError for a cycle reachable from target.

```powershell
python practice.py 98 --exercise 1
```

### 2. Application: `build_plan(dependencies, target)`

Return prerequisites plus target in valid execution order. Among available nodes choose lexicographically smallest string. Only include target closure; reachable cycle raises ValueError.

```powershell
python practice.py 98 --exercise 2
```

### 3. Stretch: `affected_targets(dependencies, changed)`

Return sorted keys OR referenced nodes that are changed or transitively depend on a changed node. Include changed nodes even if absent. Handle cycles without looping.

```powershell
python practice.py 98 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
