"""Worked learning example for day 054; independent of the exercises."""

def main():
    from bisect import insort
    ordered = [2, 5, 9]
    insort(ordered, 4)
    print(ordered)


if __name__ == "__main__":
    main()
