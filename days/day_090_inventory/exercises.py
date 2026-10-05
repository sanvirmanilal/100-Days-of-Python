"""Day 090: Project: inventory events. Implement these contracts after attempting them."""

def apply_stock(stock, sku, delta):
    'Return a new stock dict applying integer delta to sku (absent starts 0). Negative resulting stock raises ValueError; retain zero entries.'
    raise NotImplementedError("Attempt day 090, exercise 1: apply_stock")


def replay_stock(events):
    'Events have sku and integer delta. Starting empty apply each event with the previous rules; return final stock or raise ValueError for negative intermediate stock.'
    raise NotImplementedError("Attempt day 090, exercise 2: replay_stock")


def inventory_report(events, thresholds):
    'Replay stock as above. Return {stock,low_stock}; low_stock is sorted SKUs in thresholds whose final stock (default 0) is strictly below threshold. Negative intermediate stock raises ValueError.'
    raise NotImplementedError("Attempt day 090, exercise 3: inventory_report")

