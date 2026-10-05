"""Worked learning example for day 045; independent of the exercises."""

def main():
    class Words:
        def __init__(self, text):
            self.words = text.split()

        def __len__(self):
            return len(self.words)

    print(len(Words("hello world")))


if __name__ == "__main__":
    main()
