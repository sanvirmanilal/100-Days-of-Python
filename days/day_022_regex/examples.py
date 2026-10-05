"""Worked learning example for day 022; independent of the exercises."""

def main():
    import re
    print(re.findall(r"[A-Z]+", "ID 42: OK"))
    print(bool(re.fullmatch(r"[a-z]+", "python")))


if __name__ == "__main__":
    main()
