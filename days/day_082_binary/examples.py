"""Worked learning example for day 082; independent of the exercises."""

def main():
    value = 0b1010
    print(value & 0b0010)
    print((258).to_bytes(2, "big"))
    print(int.from_bytes(b"\x01\x02", "big"))


if __name__ == "__main__":
    main()
