"""Worked learning example for day 094; independent of the exercises."""

def main():
    balances = {"a": 5, "b": 2}
    proposed = balances.copy()
    proposed["a"] -= 1
    proposed["b"] += 1
    print(balances, proposed)


if __name__ == "__main__":
    main()
