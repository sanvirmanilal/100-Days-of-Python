"""Worked learning example for day 025; independent of the exercises."""

def main():
    from decimal import Decimal, ROUND_HALF_UP
    value = Decimal("1.005")
    print(value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))


if __name__ == "__main__":
    main()
