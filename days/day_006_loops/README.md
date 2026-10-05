# Day 006: Loops and accumulators

**Phase:** Foundations

**Prerequisites:** Complete days 001–005 first.

## Learn

A for loop visits items in order. Accumulators collect a running result. range excludes its stop value, so inspect small examples before choosing bounds.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 6 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `sum_to(n)`

Return the sum of integers from 1 through n. n is nonnegative. Practice a loop.

```powershell
python practice.py 6 --exercise 1
```

### 2. Application: `count_multiples(n, divisor)`

Count numbers in 1..n divisible by divisor. n >=0; divisor >0.

```powershell
python practice.py 6 --exercise 2
```

### 3. Stretch: `fizzbuzz(n)`

Return strings for 1..n: Fizz for multiples of 3, Buzz for 5, FizzBuzz for both, otherwise the number. n >=0.

```powershell
python practice.py 6 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
