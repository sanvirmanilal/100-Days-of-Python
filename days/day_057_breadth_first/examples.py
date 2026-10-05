"""Worked learning example for day 057; independent of the exercises."""

def main():
    from collections import deque
    frontier = deque([("a", 0)])
    node, distance = frontier.popleft()
    print(node, distance)


if __name__ == "__main__":
    main()
