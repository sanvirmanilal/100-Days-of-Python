"""Worked learning example for day 052; independent of the exercises."""

def main():
    nodes = {"a": (10, "b"), "b": (20, None)}
    value, next_id = nodes["a"]
    print(value, nodes[next_id][0])


if __name__ == "__main__":
    main()
