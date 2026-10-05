# Day 067: Modules and configuration boundaries

**Phase:** Testing and local applications

**Prerequisites:** Complete days 001–066 first.

## Learn

Modules group related functions. Keep parsing and validation separate from use. Make precedence rules explicit so configuration changes are predictable.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 67 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `merge_config(defaults, file_config, overrides)`

Return a new dict; later layers override earlier ones even with None. Do not mutate inputs.

```powershell
python practice.py 67 --exercise 1
```

### 2. Application: `parse_bool(text)`

Strip and lowercase. true/1/yes return True; false/0/no return False; everything else raises ValueError.

```powershell
python practice.py 67 --exercise 2
```

### 3. Stretch: `validate_config(config)`

Return a new dict containing host and port only. host is a nonempty string; port is an int excluding bool in 1..65535. Missing or invalid values raise ValueError.

```powershell
python practice.py 67 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
