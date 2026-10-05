"""Worked learning example for day 039; independent of the exercises."""

def main():
    values = [4, 8, 4]
    seen = set()
    for value in values:
        print(value in seen)
        seen.add(value)


if __name__ == "__main__":
    main()
