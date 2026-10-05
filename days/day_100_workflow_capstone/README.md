# Day 100: Capstone: workflow engine

**Phase:** Integration and capstones

**Prerequisites:** Complete days 001–099 first.

## Learn

Combine dependencies, deterministic planning, and failure propagation. Finish with a design review explaining state transitions, complexity, and what your tests cannot prove.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 100 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `ready_tasks(dependencies, completed)`

dependencies maps task names to prerequisite name lists; all prerequisites are keys. Return sorted uncompleted tasks whose prerequisites are ALL completed. Do not mutate inputs.

```powershell
python practice.py 100 --exercise 1
```

### 2. Application: `workflow_layers(dependencies)`

Return execution layers: each contains ALL currently ready tasks sorted, then mark whole layer complete. All prerequisites must be keys or KeyError. Cycles raise ValueError.

```powershell
python practice.py 100 --exercise 2
```

### 3. Stretch: `run_workflow(dependencies, outcomes)`

Validate full graph as above before running. outcomes maps every task to boolean success (missing raises KeyError). Process valid layers. State success/failed by outcome when all prerequisites succeeded; otherwise blocked. Return task->state dict. Empty graph returns {}.

```powershell
python practice.py 100 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
