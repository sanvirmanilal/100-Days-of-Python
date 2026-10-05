"""Day 068: SQLite and parameterized queries. Implement these contracts after attempting them."""

def user_names(connection):
    'Table users(id INTEGER, name TEXT) exists. Return names ordered by id ascending. Do not close the supplied connection.'
    raise NotImplementedError("Attempt day 068, exercise 1: user_names")


def find_user(connection, name):
    'Query users(id INTEGER,name TEXT) using a parameter. Return smallest matching id or None.'
    raise NotImplementedError("Attempt day 068, exercise 2: find_user")


def score_totals(connection):
    'Table scores(name TEXT,points INTEGER) exists. Return (name,total) tuples grouped by name ordered total descending then name ascending.'
    raise NotImplementedError("Attempt day 068, exercise 3: score_totals")

