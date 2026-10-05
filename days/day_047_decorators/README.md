# Day 047: Decorators and wrappers

**Phase:** Objects and domain models

**Prerequisites:** Complete days 001–046 first.

## Learn

A decorator receives a function and returns a replacement callable. functools.wraps preserves metadata. Wrappers must forward positional and keyword arguments.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 47 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `call_repeated(function, times, args)`

Call function(*args) times and return the list of results; times >=0. This is the core behavior of a repetition wrapper.

```powershell
python practice.py 47 --exercise 1
```

### 2. Application: `Counted(function)`

Callable wrapper with calls starting at 0. __call__(*args, **kwargs) increments calls BEFORE invoking function and returns its result; count failed calls too.

```powershell
python practice.py 47 --exercise 2
```

### 3. Stretch: `Memoized(function)`

Callable wrapper accepting positional hashable arguments. Cache successful return values by argument tuple; expose cache dict. Never cache exceptions.

```powershell
python practice.py 47 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
