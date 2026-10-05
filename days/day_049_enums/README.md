# Day 049: Enums and explicit states

**Phase:** Objects and domain models

**Prerequisites:** Complete days 001–048 first.

## Learn

Enums give states meaningful identities. State transitions should reject unsupported actions rather than silently producing impossible combinations.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 49 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `traffic_next(state)`

Return next string in cycle red -> green -> amber -> red. Raise ValueError for unknown state.

```powershell
python practice.py 49 --exercise 1
```

### 2. Application: `order_transition(state, action)`

Allowed transitions: new/pay -> paid, new/cancel -> cancelled, paid/ship -> shipped, paid/cancel -> cancelled. All others raise ValueError. Return new state.

```powershell
python practice.py 49 --exercise 2
```

### 3. Stretch: `run_order(actions)`

Start at new, apply preceding transition rules, and return final state. Empty actions returns new; invalid action at any point raises ValueError.

```powershell
python practice.py 49 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
