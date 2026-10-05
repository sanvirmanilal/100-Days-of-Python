"""Worked learning example for day 020; independent of the exercises."""

def main():
    rounds = [{"name": "Ada", "points": 4}, {"name": "Ada", "points": 2}]
    print([row["points"] for row in rounds])


if __name__ == "__main__":
    main()
