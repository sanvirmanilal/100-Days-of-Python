"""Worked learning example for day 069; independent of the exercises."""

def main():
    import sqlite3
    connection = sqlite3.connect(":memory:")
    try:
        print(connection.execute("SELECT COUNT(*) FROM sqlite_master").fetchone()[0])
    finally:
        connection.close()


if __name__ == "__main__":
    main()
