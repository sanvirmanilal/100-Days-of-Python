"""Worked learning example for day 042; independent of the exercises."""

def main():
    from dataclasses import dataclass
    @dataclass(frozen=True)
    class Tag:
        name: str

    print(Tag("python") == Tag("python"))


if __name__ == "__main__":
    main()
