"""Worked learning example for day 035; independent of the exercises."""

def main():
    from itertools import chain, combinations
    print(list(chain([1, 2], [3])))
    print(list(combinations("ABC", 2)))


if __name__ == "__main__":
    main()
