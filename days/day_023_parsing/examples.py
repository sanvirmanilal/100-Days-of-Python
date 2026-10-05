"""Worked learning example for day 023; independent of the exercises."""

def main():
    line = "name = Ada"
    key, value = line.split("=", 1)
    print(key.strip(), value.strip())


if __name__ == "__main__":
    main()
