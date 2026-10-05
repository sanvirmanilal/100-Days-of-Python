# Day 032: Queues and deques

**Phase:** Iteration and problem solving

**Prerequisites:** Complete days 001–031 first.

## Learn

A deque supports efficient operations at both ends. Queue simulations should define exactly when events are processed and how empty states behave.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 32 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `serve_queue(arrivals)`

Return a fresh list of arrival names in FIFO order. Practice deque append and popleft.

```powershell
python practice.py 32 --exercise 1
```

### 2. Application: `recent_items(items, capacity)`

Return the last capacity items in input order. capacity >=0; zero returns []. Practice deque(maxlen=...).

```powershell
python practice.py 32 --exercise 2
```

### 3. Stretch: `round_robin(queues)`

Return one item from each nonempty queue per round in queue order, until all are exhausted. Do not mutate input.

```powershell
python practice.py 32 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
