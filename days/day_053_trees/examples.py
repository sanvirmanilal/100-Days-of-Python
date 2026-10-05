"""Worked learning example for day 053; independent of the exercises."""

def main():
    tree = (4, (2, None, None), (7, None, None))
    value, left, right = tree
    print(value, left[0], right[0])


if __name__ == "__main__":
    main()
