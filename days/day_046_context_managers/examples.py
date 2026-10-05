"""Worked learning example for day 046; independent of the exercises."""

def main():
    from contextlib import contextmanager
    @contextmanager
    def announced():
        print("enter")
        try:
            yield
        finally:
            print("exit")

    with announced():
        print("body")


if __name__ == "__main__":
    main()
