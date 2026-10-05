"""Worked learning example for day 029; independent of the exercises."""

def main():
    from pathlib import PurePosixPath
    p = PurePosixPath("reports/annual.csv")
    print(p.name, p.stem, p.suffix)
    print(p.parent)


if __name__ == "__main__":
    main()
