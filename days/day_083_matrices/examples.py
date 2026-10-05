"""Worked learning example for day 083; independent of the exercises."""

def main():
    matrix = [[1, 2], [3, 4]]
    print([row[0] for row in matrix])
    print([sum(row) for row in matrix])


if __name__ == "__main__":
    main()
