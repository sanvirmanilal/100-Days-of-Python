"""Worked learning example for day 048; independent of the exercises."""

def main():
    def length(text: str) -> int:
        return len(text)

    print(length("typed"))
    print(length.__annotations__)


if __name__ == "__main__":
    main()
