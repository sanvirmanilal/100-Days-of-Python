"""Worked learning example for day 097; independent of the exercises."""

def main():
    times = [1, 3, 5]
    now, window = 5, 3
    print([t for t in times if now - window < t <= now])


if __name__ == "__main__":
    main()
