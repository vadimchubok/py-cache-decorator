from typing import Callable


def cache(func: Callable) -> Callable:
    cache_storage = {}

    def wrapper(*args, **kwargs) -> Callable:
        nonlocal cache_storage
        res = (args,)
        key = (args, tuple(kwargs.items()))
        if key in cache_storage:
            print("Getting from cache")
            res = cache_storage[key]
        else:
            print("Calculating new result")
            res = func(*args)
            cache_storage[key] = res
        return res

    return wrapper
