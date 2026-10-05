"""Worked learning example for day 063; independent of the exercises."""

def main():
    def timestamped(message, clock):
        return (clock(), message)

    print(timestamped("ready", lambda: 100))


if __name__ == "__main__":
    main()
