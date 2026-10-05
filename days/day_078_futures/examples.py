"""Worked learning example for day 078; independent of the exercises."""

def main():
    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=2) as pool:
        print(list(pool.map(abs, [-2, -4, 3])))


if __name__ == "__main__":
    main()
