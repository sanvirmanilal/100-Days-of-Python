# Day 090: Project: inventory events

**Phase:** Advanced data processing

**Prerequisites:** Complete days 001–089 first.

## Learn

Derive inventory from events while preventing negative stock. Use integer quantities and explicit ordering. Add your own tests for failed events and repeated IDs.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 90 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `apply_stock(stock, sku, delta)`

Return a new stock dict applying integer delta to sku (absent starts 0). Negative resulting stock raises ValueError; retain zero entries.

```powershell
python practice.py 90 --exercise 1
```

### 2. Application: `replay_stock(events)`

Events have sku and integer delta. Starting empty apply each event with the previous rules; return final stock or raise ValueError for negative intermediate stock.

```powershell
python practice.py 90 --exercise 2
```

### 3. Stretch: `inventory_report(events, thresholds)`

Replay stock as above. Return {stock,low_stock}; low_stock is sorted SKUs in thresholds whose final stock (default 0) is strictly below threshold. Negative intermediate stock raises ValueError.

```powershell
python practice.py 90 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
