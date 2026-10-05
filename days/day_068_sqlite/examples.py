"""Worked learning example for day 068; independent of the exercises."""

def main():
    import sqlite3
    with sqlite3.connect(":memory:") as connection:
        connection.execute("CREATE TABLE notes (text TEXT)")
        connection.execute("INSERT INTO notes VALUES (?)", ("hello",))
        print(connection.execute("SELECT text FROM notes").fetchall())


if __name__ == "__main__":
    main()
