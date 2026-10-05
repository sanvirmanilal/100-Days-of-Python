"""Day 099: Capstone: transaction analytics. Implement these contracts after attempting them."""

def normalize_transaction(record):
    'Require dict with nonempty string id/category, integer cents excluding bool (negative refunds allowed). Return only those three keys; invalid record raises ValueError.'
    raise NotImplementedError("Attempt day 099, exercise 1: normalize_transaction")


def clean_transactions(records):
    'Validate each record independently, skip invalid records, keep first valid record per id, return normalized records in encounter order.'
    raise NotImplementedError("Attempt day 099, exercise 2: clean_transactions")


def analytics_report(records):
    'Clean as above. Return {count,total,by_category}; by_category is list of (category,net_cents) sorted net descending then name ascending. Retain zero totals.'
    raise NotImplementedError("Attempt day 099, exercise 3: analytics_report")

