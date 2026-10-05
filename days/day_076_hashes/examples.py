"""Worked learning example for day 076; independent of the exercises."""

def main():
    import hashlib
    print(hashlib.sha256(b"example").hexdigest())
    print(hashlib.sha256(b"example").digest_size)


if __name__ == "__main__":
    main()
