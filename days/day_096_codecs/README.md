# Day 096: Encoding and decoding protocols

**Phase:** Integration and capstones

**Prerequisites:** Complete days 001–095 first.

## Learn

An encoding needs a reversible format and validation rules. Base64 represents bytes as ASCII. Length prefixes allow payloads containing delimiter-like data.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 96 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `to_base64(data)`

Return standard base64 encoding of bytes as an ASCII string.

```powershell
python practice.py 96 --exercise 1
```

### 2. Application: `from_base64(text)`

Decode ASCII base64 with validate=True, returning bytes. Convert invalid encoding errors into ValueError.

```powershell
python practice.py 96 --exercise 2
```

### 3. Stretch: `decode_frames(data)`

Parse concatenated frames: two-byte big-endian unsigned byte length followed by that many payload bytes. Return list of byte payloads. Truncated prefix or payload raises ValueError.

```powershell
python practice.py 96 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
