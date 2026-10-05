# Day 021: Cleaning text

**Phase:** Text, files, and data formats

**Prerequisites:** Complete days 001–020 first.

## Learn

Normalize only what the specification allows. Splitting on whitespace handles tabs and repeated spaces. Preserve meaningful punctuation unless asked to remove it.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 21 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `collapse_spaces(text)`

Return whitespace-separated words joined by single spaces.

```powershell
python practice.py 21 --exercise 1
```

### 2. Application: `slugify(text)`

Lowercase text, split on whitespace, and join with hyphens. Keep punctuation unchanged.

```powershell
python practice.py 21 --exercise 2
```

### 3. Stretch: `word_counts(text)`

Split on whitespace, lowercase words, strip only . , ! ? from both ends of each word, ignore empty results, and count.

```powershell
python practice.py 21 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
