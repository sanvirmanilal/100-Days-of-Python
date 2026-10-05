"""Worked learning example for day 028; independent of the exercises."""

def main():
    import json
    encoded = json.dumps({"ready": True, "count": 2})
    print(encoded)
    print(json.loads(encoded))


if __name__ == "__main__":
    main()
