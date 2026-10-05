"""Worked learning example for day 072; independent of the exercises."""

def main():
    payload = {"items": [{"id": 1}], "next": None}
    print(isinstance(payload["items"], list))
    print(payload["next"] is None)


if __name__ == "__main__":
    main()
