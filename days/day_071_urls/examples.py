"""Worked learning example for day 071; independent of the exercises."""

def main():
    from urllib.parse import urlsplit, urlencode
    print(urlsplit("https://example.test/path?q=python").path)
    print(urlencode({"q": "hello world"}))


if __name__ == "__main__":
    main()
