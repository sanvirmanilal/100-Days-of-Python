"""Worked learning example for day 017; independent of the exercises."""

def main():
    try:
        int("not-a-number")
    except ValueError as error:
        print(type(error).__name__)


if __name__ == "__main__":
    main()
