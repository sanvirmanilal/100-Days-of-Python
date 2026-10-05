# Day 064: Fakes, spies, and mocks

**Phase:** Testing and local applications

**Prerequisites:** Complete days 001–063 first.

## Learn

A fake implements simplified behavior; a spy records calls. Assert interactions only when they are part of the contract. unittest.mock can control side effects.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 64 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `notify_all(names, notifier)`

Call notifier(name) once for each name in order and return number called. Stop and propagate any exception.

```powershell
python practice.py 64 --exercise 1
```

### 2. Application: `Spy(function)`

Callable wrapper: record positional argument tuples in calls before forwarding to function, even if it raises. Expose calls list.

```powershell
python practice.py 64 --exercise 2
```

### 3. Stretch: `fallback_call(primary, secondary, value)`

Call primary(value); call secondary(value) only if primary raises LookupError. Other errors propagate.

```powershell
python practice.py 64 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
