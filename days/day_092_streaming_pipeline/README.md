# Day 092: Streaming data pipelines

**Phase:** Integration and capstones

**Prerequisites:** Complete days 001–091 first.

## Learn

Streaming separates source, transformation, and sink. Process records as they arrive and bound memory where possible. Return iterators for the first two stages today.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 92 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `parse_numbers(lines)`

Yield int(stripped_line) for nonblank lines; malformed integers raise ValueError during iteration.

```powershell
python practice.py 92 --exercise 1
```

### 2. Application: `positive_batches(numbers, size)`

Filter values >0 and yield lists of size, including final partial batch. size <=0 raises ValueError during iteration.

```powershell
python practice.py 92 --exercise 2
```

### 3. Stretch: `stream_summary(lines)`

Ignore blank lines, parse other lines as integers, and return {count,sum,min,max}. No numbers gives count/sum 0 and min/max None; malformed integer raises ValueError. Use one pass.

```powershell
python practice.py 92 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
