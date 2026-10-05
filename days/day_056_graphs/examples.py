"""Worked learning example for day 056; independent of the exercises."""

def main():
    graph = {"a": ["b", "c"], "b": ["c"]}
    print(graph.get("c", []))
    print(graph["a"])


if __name__ == "__main__":
    main()
