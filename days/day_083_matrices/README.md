# Day 083: Matrices and shape validation

**Phase:** Advanced data processing

**Prerequisites:** Complete days 001–082 first.

## Learn

A rectangular matrix has equal row lengths. Validate shapes before combining data. Today empty matrix [] is allowed, but nonempty matrices have at least one column.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 83 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `matrix_shape(matrix)`

Return (rows,columns). [] gives (0,0). Ragged rows or nonempty matrices with zero columns raise ValueError.

```powershell
python practice.py 83 --exercise 1
```

### 2. Application: `transpose(matrix)`

Return a new transposed matrix, validating with preceding rules. [] gives [].

```powershell
python practice.py 83 --exercise 2
```

### 3. Stretch: `matrix_multiply(left, right)`

Return matrix product after shape validation. Inner dimensions must match or ValueError. Both empty returns []; exactly one empty raises ValueError.

```powershell
python practice.py 83 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
