"""Worked learning example for day 089; independent of the exercises."""

def main():
    events = [{"kind": "add", "amount": 3}, {"kind": "add", "amount": 2}]
    print([event["amount"] for event in events])


if __name__ == "__main__":
    main()
