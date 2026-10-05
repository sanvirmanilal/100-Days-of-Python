"""Worked learning example for day 040; independent of the exercises."""

def main():
    documents = {"a": "Python learning", "b": "Python testing"}
    print(sorted(documents))
    print(documents["a"].lower().split())


if __name__ == "__main__":
    main()
