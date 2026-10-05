"""Worked learning example for day 033; independent of the exercises."""

def main():
    stream = iter([10, 20])
    print(next(stream))
    print(next(stream))
    print(next(stream, "finished"))


if __name__ == "__main__":
    main()
