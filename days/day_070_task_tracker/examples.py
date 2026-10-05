"""Worked learning example for day 070; independent of the exercises."""

def main():
    import json
    task = {"id": 1, "title": "read", "done": False}
    print(json.dumps(task, sort_keys=True))


if __name__ == "__main__":
    main()
