# Day 078: Concurrency with futures

**Phase:** Offline APIs and concurrency

**Prerequisites:** Complete days 001–077 first.

## Learn

ThreadPoolExecutor is useful for independent I/O work. Submission order and completion order differ. Use context managers and let worker exceptions reach the caller.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 78 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `parallel_map(function, items)`

Use ThreadPoolExecutor to apply function to items. Return results in input order; propagate worker exceptions.

```powershell
python practice.py 78 --exercise 1
```

### 2. Application: `parallel_lengths(texts)`

Use threads to compute each text length and return (text,length) pairs in input order.

```powershell
python practice.py 78 --exercise 2
```

### 3. Stretch: `parallel_batches(function, batches)`

Use one thread task per batch, applying function to each item. Return nested result lists in batch order, including empty batches. Propagate errors.

```powershell
python practice.py 78 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
