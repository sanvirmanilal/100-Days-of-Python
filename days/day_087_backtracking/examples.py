"""Worked learning example for day 087; independent of the exercises."""

def main():
    from itertools import product
    for candidate in product([0, 1], repeat=2):
        print(candidate)


if __name__ == "__main__":
    main()
