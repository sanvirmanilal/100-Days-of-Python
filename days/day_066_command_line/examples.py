"""Worked learning example for day 066; independent of the exercises."""

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", default="friend")
    print(parser.parse_args(["--name", "Ada"]).name)


if __name__ == "__main__":
    main()
