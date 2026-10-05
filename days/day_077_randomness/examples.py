"""Worked learning example for day 077; independent of the exercises."""

def main():
    import random
    rng = random.Random(7)
    print([rng.randint(1, 6) for _ in range(3)])


if __name__ == "__main__":
    main()
