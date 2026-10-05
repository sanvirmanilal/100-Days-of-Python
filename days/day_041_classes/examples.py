"""Worked learning example for day 041; independent of the exercises."""

def main():
    class Label:
        def __init__(self, text):
            self.text = text

        def render(self):
            return f"[{self.text}]"

    print(Label("ready").render())


if __name__ == "__main__":
    main()
