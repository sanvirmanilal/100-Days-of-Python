"""Worked learning example for day 058; independent of the exercises."""

def main():
    stack = ["a"]
    stack.extend(reversed(["b", "c"]))
    print(stack.pop())
    print(stack.pop())


if __name__ == "__main__":
    main()
