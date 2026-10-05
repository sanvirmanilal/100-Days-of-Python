# Day 059: Dynamic programming

**Phase:** Data structures and algorithms

**Prerequisites:** Complete days 001–058 first.

## Learn

Dynamic programming reuses overlapping subproblems. Choose a state, recurrence, and base cases before coding. Avoid measuring correctness by timing thresholds.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 59 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `fibonacci(n)`

Return F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2); n >=0. Use iterative O(n) work.

```powershell
python practice.py 59 --exercise 1
```

### 2. Application: `min_coins(coins, amount)`

Return minimum coins needed for amount, or None if impossible. Unlimited positive integer coin denominations; amount >=0.

```powershell
python practice.py 59 --exercise 2
```

### 3. Stretch: `edit_distance(left, right)`

Return Levenshtein distance with insert/delete/replace each costing 1.

```powershell
python practice.py 59 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
