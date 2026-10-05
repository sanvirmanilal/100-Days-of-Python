"""Worked learning example for day 031; independent of the exercises."""

def main():
    from collections import Counter, defaultdict
    print(Counter("banana"))
    groups = defaultdict(list)
    groups["fruit"].append("pear")
    print(dict(groups))


if __name__ == "__main__":
    main()
