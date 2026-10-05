"""Worked learning example for day 047; independent of the exercises."""

def main():
    from functools import wraps
    def announce(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            print("calling", function.__name__)
            return function(*args, **kwargs)
        return wrapper

    @announce
    def ping():
        return "pong"

    print(ping())


if __name__ == "__main__":
    main()
