import functools
from time import sleep
from dataclasses import dataclass
from selenium.webdriver.remote.webelement import WebElement

"""Various utilities"""


@dataclass
class Question:
    """Represents a form question and all the data related to it"""
    label_element: WebElement
    input_element: WebElement
    label: str

    def __str__(self):
        return self.label
    # todo: input_type for selects and text inputs


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


def concatenate_classname(classname: str):
    """Concatenates multiple css classes using dots"""
    return '.'.join(classname.split())
