# Day 026: Reading files safely

**Phase:** Text, files, and data formats

**Prerequisites:** Complete days 001–025 first.

## Learn

Use pathlib and explicit UTF-8 encoding. A context manager closes resources even if processing fails. Tests create temporary files, so your code needs no external data.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 26 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `read_text(path)`

Return the entire UTF-8 file content, preserving line breaks. path is a pathlib.Path.

```powershell
python practice.py 26 --exercise 1
```

### 2. Application: `nonempty_lines(path)`

Read UTF-8 text and return stripped nonempty lines in order.

```powershell
python practice.py 26 --exercise 2
```

### 3. Stretch: `file_stats(path)`

Return {lines, words, characters}. lines uses str.splitlines(), words uses str.split(), characters uses len on the full UTF-8 text.

```powershell
python practice.py 26 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
