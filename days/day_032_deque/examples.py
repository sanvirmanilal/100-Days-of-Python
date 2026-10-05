"""Worked learning example for day 032; independent of the exercises."""

def main():
    from collections import deque
    queue = deque(["Ada", "Bo"])
    queue.append("Cy")
    print(queue.popleft())
    print(list(queue))


if __name__ == "__main__":
    main()
