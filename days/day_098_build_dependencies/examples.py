"""Worked learning example for day 098; independent of the exercises."""

def main():
    dependencies = {"package": ["test"], "test": ["compile"], "compile": []}
    print(dependencies["package"])


if __name__ == "__main__":
    main()
