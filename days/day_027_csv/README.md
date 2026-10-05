# Day 027: CSV records

**Phase:** Text, files, and data formats

**Prerequisites:** Complete days 001–026 first.

## Learn

CSV fields may contain commas or newlines inside quotes. Use the csv module rather than splitting on commas. Treat parsed numeric fields explicitly.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 27 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `parse_csv(text)`

Return all CSV rows as lists of strings using csv.reader. Empty text returns [].

```powershell
python practice.py 27 --exercise 1
```

### 2. Application: `csv_records(text)`

Use first CSV row as headers; return remaining rows as dictionaries of strings. Inputs have unique headers and equal row lengths.

```powershell
python practice.py 27 --exercise 2
```

### 3. Stretch: `sum_csv_column(text, column)`

Parse CSV with headers and sum integer values in column. Return 0 for header-only input; raise KeyError for absent column, ValueError for a noninteger value. Input always has a header.

```powershell
python practice.py 27 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
