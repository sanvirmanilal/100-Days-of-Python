"""Worked learning example for day 060; independent of the exercises."""

def main():
    roads = {"a": [("b", 4), ("c", 2)]}
    print(min(roads["a"], key=lambda edge: edge[1]))


if __name__ == "__main__":
    main()
