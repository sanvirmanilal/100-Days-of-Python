"""Day 067: Modules and configuration boundaries. Implement these contracts after attempting them."""

def merge_config(defaults, file_config, overrides):
    'Return a new dict; later layers override earlier ones even with None. Do not mutate inputs.'
    raise NotImplementedError("Attempt day 067, exercise 1: merge_config")


def parse_bool(text):
    'Strip and lowercase. true/1/yes return True; false/0/no return False; everything else raises ValueError.'
    raise NotImplementedError("Attempt day 067, exercise 2: parse_bool")


def validate_config(config):
    'Return a new dict containing host and port only. host is a nonempty string; port is an int excluding bool in 1..65535. Missing or invalid values raise ValueError.'
    raise NotImplementedError("Attempt day 067, exercise 3: validate_config")

