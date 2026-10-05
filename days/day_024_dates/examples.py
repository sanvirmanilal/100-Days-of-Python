"""Worked learning example for day 024; independent of the exercises."""

def main():
    from datetime import date, timedelta
    start = date(2024, 2, 28)
    print(start + timedelta(days=2))
    print(start.isoformat())


if __name__ == "__main__":
    main()
