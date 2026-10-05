# Day 029: Portable paths

**Phase:** Text, files, and data formats

**Prerequisites:** Complete days 001–028 first.

## Learn

pathlib separates path operations from string manipulation. PurePosixPath is useful for platform-independent logical paths. A suffix describes only the final extension.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 29 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `file_extension(path)`

Treat path as PurePosixPath and return its final suffix lowercased, including dot.

```powershell
python practice.py 29 --exercise 1
```

### 2. Application: `replace_extension(path, suffix)`

Return str(PurePosixPath(path).with_suffix(suffix)). suffix is empty or starts with a dot and is valid.

```powershell
python practice.py 29 --exercise 2
```

### 3. Stretch: `safe_relative(path)`

For a logical POSIX path, return False if absolute or if any part is ..; otherwise True. Empty path and . are allowed.

```powershell
python practice.py 29 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
