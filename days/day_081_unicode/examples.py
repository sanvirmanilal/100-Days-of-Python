"""Worked learning example for day 081; independent of the exercises."""

def main():
    import unicodedata
    print("Straße".casefold())
    print(unicodedata.normalize("NFC", "e\u0301"))


if __name__ == "__main__":
    main()
