"""Worked learning example for day 044; independent of the exercises."""

def main():
    class Constant:
        @property
        def value(self):
            return 42

    print(Constant().value)


if __name__ == "__main__":
    main()
