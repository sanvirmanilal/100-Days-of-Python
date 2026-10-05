"""Worked learning example for day 027; independent of the exercises."""

def main():
    import csv
    import io
    rows = csv.reader(io.StringIO('name,city\nAda,"New York"\n'))
    print(list(rows))


if __name__ == "__main__":
    main()
