"""Day 073: Pagination and cursors. Implement these contracts after attempting them."""

def page(items, offset, limit):
    'Return a fresh slice; offset >=0 and limit >0 required or ValueError.'
    raise NotImplementedError("Attempt day 073, exercise 1: page")


def paginate(items, size):
    'Return {items,next_offset} pages from offset 0. next_offset is next start or None for final page. Empty input returns []; size <=0 raises ValueError.'
    raise NotImplementedError("Attempt day 073, exercise 2: paginate")


def collect_pages(pages, start):
    'pages maps cursor strings to {items,next} records. Follow next until None and concatenate items. Revisited cursor raises ValueError; missing cursor raises KeyError.'
    raise NotImplementedError("Attempt day 073, exercise 3: collect_pages")

