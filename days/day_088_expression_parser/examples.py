"""Worked learning example for day 088; independent of the exercises."""

def main():
    import re
    print(re.findall(r"[0-9]+|[+*()]", "12 + (3 * 4)"))


if __name__ == "__main__":
    main()
