"""Worked learning example for day 009; independent of the exercises."""

def main():
    stock = {"tea": 3, "rice": 8}
    print(stock.get("bread", 0))
    for item, count in stock.items():
        print(item, count)


if __name__ == "__main__":
    main()
