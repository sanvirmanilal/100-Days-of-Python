"""Worked learning example for day 062; independent of the exercises."""

def main():
    for number in range(-5, 6):
        assert abs(number) >= 0
        assert abs(-number) == abs(number)
    print("properties checked")


if __name__ == "__main__":
    main()
