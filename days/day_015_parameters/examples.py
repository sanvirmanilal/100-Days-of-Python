"""Worked learning example for day 015; independent of the exercises."""

def main():
    def label(text, prefix="Info"):
        return f"{prefix}: {text}"

    print(label("ready"))
    print(label("done", prefix="Status"))


if __name__ == "__main__":
    main()
