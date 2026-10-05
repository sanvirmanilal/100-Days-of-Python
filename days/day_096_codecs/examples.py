"""Worked learning example for day 096; independent of the exercises."""

def main():
    import base64
    encoded = base64.b64encode(b"hello")
    print(encoded)
    print(base64.b64decode(encoded, validate=True))


if __name__ == "__main__":
    main()
