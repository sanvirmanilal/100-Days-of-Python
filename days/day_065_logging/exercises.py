"""Day 065: Structured log processing. Implement these contracts after attempting them."""

def parse_log(line):
    'Parse LEVEL|message at first |. Allowed levels DEBUG INFO WARNING ERROR; return {level,message}. Reject malformed or unknown level with ValueError. Preserve message.'
    raise NotImplementedError("Attempt day 065, exercise 1: parse_log")


def filter_logs(records, minimum):
    'Return records at or above minimum using DEBUG<INFO<WARNING<ERROR. Inputs have valid levels; invalid minimum raises ValueError.'
    raise NotImplementedError("Attempt day 065, exercise 2: filter_logs")


def error_summary(lines):
    'Parse lines with the preceding rules, ignore malformed lines, and return counts of ERROR messages only.'
    raise NotImplementedError("Attempt day 065, exercise 3: error_summary")

