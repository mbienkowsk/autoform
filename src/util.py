import functools
from time import sleep
from enum import Enum
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from src.constants import GOOGLE_FORM_RADIO_INPUT_CLASS, GOOGLE_FORM_SELECT_CLASS
from src.errors import InvalidQuestionTypeError

"""Various utilities"""


class QuestionType(Enum):
    """Possible question variants in a google form"""
    SHORT_TEXT = 0
    LONG_TEXT = 1
    RADIO = 2
    SELECT = 3


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


def assign_question_type(question_card: WebElement) -> QuestionType:
    """Based on the contents of a question card, assigns it a type"""
    select_present = len(
        question_card.find_elements(by=By.CLASS_NAME, value=concatenate_classname(GOOGLE_FORM_SELECT_CLASS)))
    if select_present:
        return QuestionType.SELECT

    text_area_present = len(question_card.find_elements(by=By.TAG_NAME, value="textarea"))
    if text_area_present:
        return QuestionType.LONG_TEXT

    radio_input_present = len(
        question_card.find_elements(by=By.CLASS_NAME, value=concatenate_classname(GOOGLE_FORM_RADIO_INPUT_CLASS)))
    if radio_input_present:
        return QuestionType.RADIO

    text_input_present = any(map(lambda x: x.get_attribute("type") == "text",
                                 question_card.find_elements(By.TAG_NAME, "input")))
    if text_input_present:
        return QuestionType.SHORT_TEXT

    # the only ones not covered are file uploads, grids, dates, etc, don't need those for now
    raise InvalidQuestionTypeError("Autoform only supports short/long text inputs, select and radio questions! ")
