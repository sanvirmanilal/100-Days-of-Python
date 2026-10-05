"""Worked learning example for day 059; independent of the exercises."""

def main():
    ways = [1, 1]
    for index in range(2, 6):
        ways.append(ways[index - 1] + ways[index - 2])
    print(ways)


if __name__ == "__main__":
    main()
