"""Worked learning example for day 043; independent of the exercises."""

def main():
    class Plain:
        def render(self):
            return "plain"

    class Fancy:
        def render(self):
            return "**fancy**"

    print([obj.render() for obj in [Plain(), Fancy()]])


if __name__ == "__main__":
    main()
