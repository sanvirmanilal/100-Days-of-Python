# Day 045: Python object protocols

**Phase:** Objects and domain models

**Prerequisites:** Complete days 001–044 first.

## Learn

Special methods connect your objects to len, iteration, and containment. Implement the expected protocol rather than requiring callers to know internal storage.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 45 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `Playlist(songs)`

Copy songs at construction. Implement __len__, __iter__, and __contains__ with ordinary list behavior.

```powershell
python practice.py 45 --exercise 1
```

### 2. Application: `RangeBox(low, high)`

Reject low > high. Implement __contains__ for inclusive numeric bounds and __len__ as high-low+1. Bounds are integers.

```powershell
python practice.py 45 --exercise 2
```

### 3. Stretch: `Polynomial(coefficients)`

Copy coefficients in ascending power order. __call__(x) evaluates the polynomial; __len__ returns coefficient count (including trailing zeros). Empty evaluates to 0.

```powershell
python practice.py 45 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
