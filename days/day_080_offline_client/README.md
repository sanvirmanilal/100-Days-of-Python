# Day 080: Project: offline API client

**Phase:** Offline APIs and concurrency

**Prerequisites:** Complete days 001–079 first.

## Learn

Build a client pipeline from local response fixtures: pagination, validation, and normalization. No network is needed to verify API behavior.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 80 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `unwrap_response(response)`

Require status integer excluding bool in 200..299 and body dict with items list and next string or None. Return body; invalid shape raises ValueError.

```powershell
python practice.py 80 --exercise 1
```

### 2. Application: `fetch_all(responses, start)`

responses maps cursors to valid response records under preceding contract. Follow body.next, concatenate body.items. Invalid response or repeated cursor raises ValueError; missing cursor raises KeyError.

```powershell
python practice.py 80 --exercise 2
```

### 3. Stretch: `sync_items(responses, start)`

Fetch all pages under preceding rules; validate items with positive int id excluding bool and nonempty string name. Later duplicates by id replace earlier; return normalized {id,name} records sorted by id. Invalid items raise ValueError.

```powershell
python practice.py 80 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
