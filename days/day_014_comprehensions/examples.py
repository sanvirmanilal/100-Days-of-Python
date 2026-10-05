"""Worked learning example for day 014; independent of the exercises."""

def main():
    names = ["Ada", "Bo", "Celia"]
    print([len(name) for name in names])
    print({name: len(name) for name in names})


if __name__ == "__main__":
    main()
