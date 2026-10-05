# Day 065: Structured log processing

**Phase:** Testing and local applications

**Prerequisites:** Complete days 001–064 first.

## Learn

Logging records events for diagnosis. Separate parsing from filtering and aggregation. Avoid testing timestamps or output that depends on the machine.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 65 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `parse_log(line)`

Parse LEVEL|message at first |. Allowed levels DEBUG INFO WARNING ERROR; return {level,message}. Reject malformed or unknown level with ValueError. Preserve message.

```powershell
python practice.py 65 --exercise 1
```

### 2. Application: `filter_logs(records, minimum)`

Return records at or above minimum using DEBUG<INFO<WARNING<ERROR. Inputs have valid levels; invalid minimum raises ValueError.

```powershell
python practice.py 65 --exercise 2
```

### 3. Stretch: `error_summary(lines)`

Parse lines with the preceding rules, ignore malformed lines, and return counts of ERROR messages only.

```powershell
python practice.py 65 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
