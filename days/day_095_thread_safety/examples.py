"""Worked learning example for day 095; independent of the exercises."""

def main():
    from threading import Lock
    lock = Lock()
    with lock:
        value = 1
    print(value)


if __name__ == "__main__":
    main()
