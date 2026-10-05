# Day 070: Project: task tracker

**Phase:** Testing and local applications

**Prerequisites:** Complete days 001–069 first.

## Learn

Combine IDs, validation, state, and serialization. Ensure each failed operation leaves existing state intact. Public results should not expose mutable internals.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 70 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `TaskTracker()`

add(title) returns sequential ID starting at 1; nonempty string title required or ValueError. list_tasks() returns fresh records {id,title,done}, insertion order, initially done=False.

```powershell
python practice.py 70 --exercise 1
```

### 2. Application: `complete_tasks(tasks, ids)`

Return fresh records with done=True for supplied IDs; retain other fields. Unknown requested ID raises KeyError; do not mutate input.

```powershell
python practice.py 70 --exercise 2
```

### 3. Stretch: `task_report(tasks)`

Return {total,completed,pending}; pending is sorted titles of tasks with done=False. Each record has title and boolean done.

```powershell
python practice.py 70 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
