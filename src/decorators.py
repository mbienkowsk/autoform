import functools
from time import sleep
from time import perf_counter
from loguru import logger


def delay(t: float):
    """Delays the function's return by t seconds, used to debug the formfiller"""

    def inner(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            rv = func(*args, **kwargs)
            sleep(t)
            return rv

        return wrapper

    return inner


def timer(func):
    """Measures the time taken by the execution of a function"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        before = perf_counter()
        rv = func(*args, **kwargs)
        after = perf_counter()
        logger.info(f"{func.__name__} took {after - before:02f} seconds.")
        return rv

    return wrapper
