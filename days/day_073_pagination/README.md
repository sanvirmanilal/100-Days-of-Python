# Day 073: Pagination and cursors

**Phase:** Offline APIs and concurrency

**Prerequisites:** Complete days 001–072 first.

## Learn

Pagination bounds each response. Define offset semantics and cursor termination so loops cannot repeat indefinitely. Test empty and partial final pages.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 73 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `page(items, offset, limit)`

Return a fresh slice; offset >=0 and limit >0 required or ValueError.

```powershell
python practice.py 73 --exercise 1
```

### 2. Application: `paginate(items, size)`

Return {items,next_offset} pages from offset 0. next_offset is next start or None for final page. Empty input returns []; size <=0 raises ValueError.

```powershell
python practice.py 73 --exercise 2
```

### 3. Stretch: `collect_pages(pages, start)`

pages maps cursor strings to {items,next} records. Follow next until None and concatenate items. Revisited cursor raises ValueError; missing cursor raises KeyError.

```powershell
python practice.py 73 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
