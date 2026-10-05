"""Worked learning example for day 037; independent of the exercises."""

def main():
    def countdown(n):
        if n == 0:
            return "done"
        return f"{n} " + countdown(n - 1)

    print(countdown(3))


if __name__ == "__main__":
    main()
