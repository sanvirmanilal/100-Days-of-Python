"""Worked learning example for day 080; independent of the exercises."""

def main():
    response = {"status": 200, "body": {"items": [1, 2], "next": None}}
    print(response["status"], response["body"]["items"])


if __name__ == "__main__":
    main()
