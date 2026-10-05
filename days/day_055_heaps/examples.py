"""Worked learning example for day 055; independent of the exercises."""

def main():
    import heapq
    queue = [5, 2, 8]
    heapq.heapify(queue)
    print(heapq.heappop(queue))
    print(queue)


if __name__ == "__main__":
    main()
