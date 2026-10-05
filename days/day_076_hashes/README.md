# Day 076: Hashes and content identity

**Phase:** Offline APIs and concurrency

**Prerequisites:** Complete days 001–075 first.

## Learn

Cryptographic hashes produce stable content fingerprints. Python hash() is unsuitable for persistent identifiers. Hashing is not encryption or a password storage recipe.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 76 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `sha256_text(text)`

Return SHA-256 hex digest of UTF-8 text.

```powershell
python practice.py 76 --exercise 1
```

### 2. Application: `same_content(left, right)`

Return whether two byte strings have identical content. Compare SHA-256 digests for this exercise.

```powershell
python practice.py 76 --exercise 2
```

### 3. Stretch: `duplicate_files(files)`

files maps filenames to byte contents. Return groups of identical content with at least two filenames; sort names inside groups and groups lexicographically.

```powershell
python practice.py 76 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
