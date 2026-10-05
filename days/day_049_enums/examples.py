"""Worked learning example for day 049; independent of the exercises."""

def main():
    from enum import Enum
    class Light(Enum):
        RED = "red"
        GREEN = "green"

    print(Light.RED.value)
    print(Light("green").name)


if __name__ == "__main__":
    main()
