"""Day 072: Validating API payloads. Implement these contracts after attempting them."""

def valid_status(code):
    'Return whether code is an integer excluding bool in HTTP success range 200..299.'
    raise NotImplementedError("Attempt day 072, exercise 1: valid_status")


def validate_item(item):
    'Return a fresh {id,name} dict if item is a dict with positive integer id excluding bool and nonempty string name. Otherwise raise ValueError; ignore extra keys.'
    raise NotImplementedError("Attempt day 072, exercise 2: validate_item")


def decode_response(status, text):
    'Reject non-success status with ValueError. Decode JSON object containing items list, validate each item as above, and return normalized records. Malformed JSON or shape raises ValueError.'
    raise NotImplementedError("Attempt day 072, exercise 3: decode_response")

