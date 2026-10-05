# Day 082: Binary data and bit operations

**Phase:** Advanced data processing

**Prerequisites:** Complete days 001–081 first.

## Learn

Bytes store integers 0..255. Bit masks isolate flags. Specify byte order when converting integers to byte sequences.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 82 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `has_flag(value, flag)`

Return whether all bits in nonnegative flag are present in nonnegative value. Zero flag is always present.

```powershell
python practice.py 82 --exercise 1
```

### 2. Application: `pack_u16(value)`

Return exactly two big-endian bytes for integer 0..65535; otherwise raise ValueError.

```powershell
python practice.py 82 --exercise 2
```

### 3. Stretch: `xor_bytes(data, key)`

Return bytes with each byte XORed with integer key in 0..255. Invalid key raises ValueError. Applying twice restores input.

```powershell
python practice.py 82 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
