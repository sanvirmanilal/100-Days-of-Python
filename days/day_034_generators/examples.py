"""Worked learning example for day 034; independent of the exercises."""

def main():
    def countdown(start):
        while start > 0:
            yield start
            start -= 1

    print(list(countdown(3)))


if __name__ == "__main__":
    main()
