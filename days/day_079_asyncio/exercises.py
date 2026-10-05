"""Day 079: Async functions and gather. Implement these contracts after attempting them."""

async def async_double(value):
    'Coroutine returning value*2 after await asyncio.sleep(0).'
    raise NotImplementedError("Attempt day 079, exercise 1: async_double")


async def gather_values(values):
    'Use gather to run a coroutine for each value and return the original values in order. Each coroutine awaits sleep(0).'
    raise NotImplementedError("Attempt day 079, exercise 2: gather_values")


async def async_apply(function, values):
    'Create one coroutine per value; each awaits sleep(0), then calls synchronous function(value). Gather results in order and propagate errors.'
    raise NotImplementedError("Attempt day 079, exercise 3: async_apply")

