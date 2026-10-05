# Day 041: Classes and instance state

**Phase:** Objects and domain models

**Prerequisites:** Complete days 001–040 first.

## Learn

A class combines state and behavior. Each instance should own its mutable state. Constructors establish valid initial values; methods operate on that instance.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 41 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `Counter(start=0)`

Expose value initialized to start. increment() adds 1 and returns the new value; reset() sets value to start and returns None.

```powershell
python practice.py 41 --exercise 1
```

### 2. Application: `Rectangle(width, height)`

Store nonnegative width and height, rejecting negatives with ValueError. area() returns width*height; perimeter() returns 2*(width+height).

```powershell
python practice.py 41 --exercise 2
```

### 3. Stretch: `BankAccount(balance=0)`

Expose nonnegative integer balance. deposit(amount) and withdraw(amount) return new balance; reject negative amounts, negative initial balance, or overdraft with ValueError, leaving balance unchanged.

```powershell
python practice.py 41 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
