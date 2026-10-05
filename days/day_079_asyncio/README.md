# Day 079: Async functions and gather

**Phase:** Offline APIs and concurrency

**Prerequisites:** Complete days 001–078 first.

## Learn

async def produces a coroutine. await cooperatively suspends it. asyncio.gather preserves argument order in its results. Do not start event loops inside these functions.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 79 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `async_double(value)`

Coroutine returning value*2 after await asyncio.sleep(0).

```powershell
python practice.py 79 --exercise 1
```

### 2. Application: `gather_values(values)`

Use gather to run a coroutine for each value and return the original values in order. Each coroutine awaits sleep(0).

```powershell
python practice.py 79 --exercise 2
```

### 3. Stretch: `async_apply(function, values)`

Create one coroutine per value; each awaits sleep(0), then calls synchronous function(value). Gather results in order and propagate errors.

```powershell
python practice.py 79 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
