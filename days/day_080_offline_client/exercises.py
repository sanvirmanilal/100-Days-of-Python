"""Day 080: Project: offline API client. Implement these contracts after attempting them."""

def unwrap_response(response):
    'Require status integer excluding bool in 200..299 and body dict with items list and next string or None. Return body; invalid shape raises ValueError.'
    raise NotImplementedError("Attempt day 080, exercise 1: unwrap_response")


def fetch_all(responses, start):
    'responses maps cursors to valid response records under preceding contract. Follow body.next, concatenate body.items. Invalid response or repeated cursor raises ValueError; missing cursor raises KeyError.'
    raise NotImplementedError("Attempt day 080, exercise 2: fetch_all")


def sync_items(responses, start):
    'Fetch all pages under preceding rules; validate items with positive int id excluding bool and nonempty string name. Later duplicates by id replace earlier; return normalized {id,name} records sorted by id. Invalid items raise ValueError.'
    raise NotImplementedError("Attempt day 080, exercise 3: sync_items")

