"""Worked learning example for day 092; independent of the exercises."""

def main():
    def nonblank(lines):
        for line in lines:
            if line.strip():
                yield line.strip()

    print(list(nonblank(iter([" a ", "", " b "]))))


if __name__ == "__main__":
    main()
