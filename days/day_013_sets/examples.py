"""Worked learning example for day 013; independent of the exercises."""

def main():
    web = {"Ada", "Bo"}
    mobile = {"Bo", "Cy"}
    print(sorted(web | mobile))
    print(sorted(web & mobile))


if __name__ == "__main__":
    main()
