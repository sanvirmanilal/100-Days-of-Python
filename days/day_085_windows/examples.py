"""Worked learning example for day 085; independent of the exercises."""

def main():
    from collections import deque
    window = deque(maxlen=3)
    for item in [1, 2, 3, 4]:
        window.append(item)
        print(list(window))


if __name__ == "__main__":
    main()
