"""Worked learning example for day 026; independent of the exercises."""

def main():
    from pathlib import Path
    from uuid import uuid4
    scratch = Path(__file__).parent / ".practice_tmp"
    scratch.mkdir(exist_ok=True)
    path = scratch / f"note_{uuid4().hex}.txt"
    try:
        with path.open("w", encoding="utf-8") as handle:
            handle.write("hello")
        with path.open("r", encoding="utf-8") as handle:
            print(handle.read())
    finally:
        path.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
