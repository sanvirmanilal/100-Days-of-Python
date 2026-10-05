# Day 046: Context managers

**Phase:** Objects and domain models

**Prerequisites:** Complete days 001–045 first.

## Learn

A context manager brackets resource use with setup and cleanup. contextlib provides helpers. Cleanup must happen even when the body raises.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 46 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `read_first_line(path)`

Read a UTF-8 file using a context manager. Return its first line without trailing CR/LF, preserving spaces; empty file returns "".

```powershell
python practice.py 46 --exercise 1
```

### 2. Application: `capture_output(function)`

Call a zero-argument function while capturing stdout with contextlib.redirect_stdout; return captured string. Propagate any exception.

```powershell
python practice.py 46 --exercise 2
```

### 3. Stretch: `temporary_setting(mapping, key, value, function)`

Temporarily assign mapping[key]=value; call function(mapping) and return its result. Restore previous value or absence even on exceptions. Other keys remain untouched.

```powershell
python practice.py 46 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
