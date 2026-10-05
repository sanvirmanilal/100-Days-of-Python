"""Worked learning example for day 036; independent of the exercises."""

def main():
    def apply_twice(function, value):
        return function(function(value))

    print(apply_twice(str.upper, "ready"))


if __name__ == "__main__":
    main()
