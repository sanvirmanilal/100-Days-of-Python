"""Worked learning example for day 075; independent of the exercises."""

def main():
    entry = {"value": "ready", "expires": 10}
    now = 10
    print(now < entry["expires"])


if __name__ == "__main__":
    main()
