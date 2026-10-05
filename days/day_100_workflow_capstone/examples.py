"""Worked learning example for day 100; independent of the exercises."""

def main():
    states = {"extract": "success", "transform": "pending"}
    print(all(states.get(name) == "success" for name in ["extract"]))


if __name__ == "__main__":
    main()
