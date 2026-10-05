# Day 061: Choosing boundary tests

**Phase:** Testing and local applications

**Prerequisites:** Complete days 001–060 first.

## Learn

Good tests separate partitions and inspect boundaries: empty, one, many, just below, at, and just above a threshold. Add at least one learner-authored test per exercise today.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 61 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `password_length_ok(text)`

Return whether length is between 8 and 64 inclusive. Only length matters.

```powershell
python practice.py 61 --exercise 1
```

### 2. Application: `ticket_price(age)`

Reject negative age. Return 0 for under 5, 8 for 5..17, 12 for 18..64, and 6 for >=65.

```powershell
python practice.py 61 --exercise 2
```

### 3. Stretch: `chunk_count(length, size)`

Return number of chunks needed for nonnegative length and positive size. Reject invalid bounds with ValueError.

```powershell
python practice.py 61 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
