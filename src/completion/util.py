from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from src.matching.classnames import *
from src.decorators import timer
from src.completion.enums import QuestionType
from src.completion.errors import InvalidQuestionTypeError

"""Various utilities"""


@timer
def assign_question_type(question_card: WebElement) -> QuestionType:
    """Based on the contents of a question card, assigns it a type"""
    short_input_present = any(map(lambda x: x.get_attribute("type") == "text",
                                  question_card.find_elements(By.CLASS_NAME, value=GOOGLE_FORM_SHORT_INPUT_CLASS)))
    if short_input_present:
        return QuestionType.SHORT_TEXT

    radio_input_present = len(
        question_card.find_elements(by=By.CLASS_NAME, value=GOOGLE_FORM_RADIO_OPTION_CLASS))
    if radio_input_present:
        return QuestionType.RADIO

    long_input_present = len(question_card.find_elements(by=By.CLASS_NAME, value=GOOGLE_FORM_LONG_INPUT_CLASS))
    if long_input_present:
        return QuestionType.LONG_TEXT

    checkbox_present = len(question_card.find_elements(by=By.CLASS_NAME, value=GOOGLE_FORM_CHECKBOX_CONTAINER_CLASS))
    if checkbox_present:
        return QuestionType.CHECKBOX

    select_present = len(
        question_card.find_elements(by=By.CLASS_NAME, value=GOOGLE_FORM_OPEN_CLOSE_SELECT_CLASS))
    if select_present:
        return QuestionType.SELECT

    # the only ones not covered are file uploads, grids, dates, etc, don't need those for now
    raise InvalidQuestionTypeError("Autoform only supports short/long text inputs, select and radio questions! ")
