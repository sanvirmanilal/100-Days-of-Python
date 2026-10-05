# Day 023: Parsing structured text

**Phase:** Text, files, and data formats

**Prerequisites:** Complete days 001–022 first.

## Learn

Parsing transforms text into structured values. Define whitespace, duplicate fields, and malformed input behavior before building the parser.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 23 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `parse_pair(text)`

Split at the first = and strip both sides; return (key, value). Raise ValueError if = is missing or stripped key is empty.

```powershell
python practice.py 23 --exercise 1
```

### 2. Application: `parse_config(text)`

Parse nonblank lines as key=value with stripping. Ignore lines whose stripped form starts #. Later duplicate keys win. Raise ValueError for malformed lines or empty keys.

```powershell
python practice.py 23 --exercise 2
```

### 3. Stretch: `parse_ranges(text)`

Parse comma-separated positive ASCII integers or ascending ranges such as 2-4. Ignore token-edge whitespace; return sorted unique ints. Empty text returns []; reject malformed, zero, or descending tokens with ValueError.

```powershell
python practice.py 23 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
