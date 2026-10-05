# Day 071: URLs and query strings

**Phase:** Offline APIs and concurrency

**Prerequisites:** Complete days 001–070 first.

## Learn

urllib.parse separates URL components and handles percent encoding. Network concepts can be practiced with strings offline. Query keys may have multiple values.

Read and predict the example output before running it. Change one input, predict again, and explain the result.

```powershell
python practice.py 71 --examples
```

The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.

## Exercises

### 1. Foundation: `url_host(url)`

Return urlsplit(url).hostname, or None if absent.

```powershell
python practice.py 71 --exercise 1
```

### 2. Application: `query_values(url)`

Return parse_qs of the URL query with keep_blank_values=True.

```powershell
python practice.py 71 --exercise 2
```

### 3. Stretch: `build_url(base, params)`

Append urlencode(params, doseq=True) to base, which has no query or fragment. Empty params returns base. Preserve insertion order.

```powershell
python practice.py 71 --exercise 3
```

## Reflect

- What does each function or object promise, and which boundary was easiest to miss?
- Add at least one meaningful test of your own. Which mistake would it catch?
- Explain your approach without reading your code; include complexity once algorithms appear.
- Record attempts and remaining questions in your journal. Request a hint or review after attempting.
