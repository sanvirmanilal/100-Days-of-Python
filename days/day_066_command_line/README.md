# Day 066: Command-line arguments

**Phase:** Testing and local applications

**Prerequisites:** Complete days 001–065 first.

## Learn

argparse converts argument lists into structured options. Accept an explicit argv list so tests avoid process-global arguments. Use SystemExit for argparse validation failures.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 66 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `parse_name(argv)`

Use argparse with optional --name defaulting to world. Return parsed name. Unknown options raise SystemExit.

```powershell
python practice.py 66 --exercise 1
```

### 2. Application: `parse_count(argv)`

Use argparse with optional --count integer defaulting to 1. Return count; invalid integer or missing option value raises SystemExit.

```powershell
python practice.py 66 --exercise 2
```

### 3. Stretch: `parse_cli(argv)`

Use argparse: positional action in {add,list}; optional --limit integer default 10; --verbose boolean flag. Return dict with action, limit, verbose. Invalid choice raises SystemExit.

```powershell
python practice.py 66 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
