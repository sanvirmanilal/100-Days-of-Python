"""Worked learning example for day 038; independent of the exercises."""

def main():
    from bisect import bisect_left
    values = [2, 4, 4, 8]
    print(bisect_left(values, 4))
    print(bisect_left(values, 5))


if __name__ == "__main__":
    main()
