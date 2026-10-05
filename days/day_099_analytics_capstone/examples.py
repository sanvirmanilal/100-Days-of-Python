"""Worked learning example for day 099; independent of the exercises."""

def main():
    row = {"id": "t1", "category": "food", "cents": 125}
    print(tuple(row[key] for key in ("id", "category", "cents")))


if __name__ == "__main__":
    main()
