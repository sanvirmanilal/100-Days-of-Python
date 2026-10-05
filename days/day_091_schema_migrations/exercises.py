"""Day 091: Versioned data and migrations. Implement these contracts after attempting them."""

def migrate_user(record):
    'v1 record {version:1,name:nonempty string} becomes {version:2,display_name:name}. v2 requires nonempty display_name and is normalized to those two keys. Invalid or unknown version raises ValueError; bool version invalid.'
    raise NotImplementedError("Attempt day 091, exercise 1: migrate_user")


def migrate_users(records):
    'Migrate each record under previous rules, preserving order; any invalid record raises ValueError. Return fresh records.'
    raise NotImplementedError("Attempt day 091, exercise 2: migrate_users")


def migration_report(records):
    'Try each migration independently. Return {users,errors}; users contains successful normalized records in order, errors contains zero-based indices of invalid records.'
    raise NotImplementedError("Attempt day 091, exercise 3: migration_report")

