"""Day 023: Parsing structured text. Implement these contracts after attempting them."""

def parse_pair(text):
    'Split at the first = and strip both sides; return (key, value). Raise ValueError if = is missing or stripped key is empty.'
    raise NotImplementedError("Attempt day 023, exercise 1: parse_pair")


def parse_config(text):
    'Parse nonblank lines as key=value with stripping. Ignore lines whose stripped form starts #. Later duplicate keys win. Raise ValueError for malformed lines or empty keys.'
    raise NotImplementedError("Attempt day 023, exercise 2: parse_config")


def parse_ranges(text):
    'Parse comma-separated positive ASCII integers or ascending ranges such as 2-4. Ignore token-edge whitespace; return sorted unique ints. Empty text returns []; reject malformed, zero, or descending tokens with ValueError.'
    raise NotImplementedError("Attempt day 023, exercise 3: parse_ranges")

