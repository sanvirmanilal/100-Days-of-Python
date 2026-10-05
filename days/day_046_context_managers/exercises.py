"""Day 046: Context managers. Implement these contracts after attempting them."""

def read_first_line(path):
    'Read a UTF-8 file using a context manager. Return its first line without trailing CR/LF, preserving spaces; empty file returns "".'
    raise NotImplementedError("Attempt day 046, exercise 1: read_first_line")


def capture_output(function):
    'Call a zero-argument function while capturing stdout with contextlib.redirect_stdout; return captured string. Propagate any exception.'
    raise NotImplementedError("Attempt day 046, exercise 2: capture_output")


def temporary_setting(mapping, key, value, function):
    'Temporarily assign mapping[key]=value; call function(mapping) and return its result. Restore previous value or absence even on exceptions. Other keys remain untouched.'
    raise NotImplementedError("Attempt day 046, exercise 3: temporary_setting")

