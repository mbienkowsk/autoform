from selenium.webdriver.remote.webelement import WebElement
from abc import ABC
from loguru import logger
from selenium.webdriver.common.by import By
from src.classnames import GOOGLE_FORM_QUESTION_TITLE_CLASS, GOOGLE_FORM_QUESTION_DESCRIPTION_CLASS


class Question(ABC):
    """Represents a form question and all the data related to it"""

    def __init__(self, card_elem: WebElement):
        self.card_element = card_elem
        self.required = "Required question" in card_elem.accessible_name
        self.title = self.find_title()
        self.description = desc if (desc := self.find_description()) else None
        logger.debug(self.card_element)

    def find_title(self) -> str:
        """Finds the title of the question"""
        label_element = self.card_element.find_element(by=By.CLASS_NAME, value=GOOGLE_FORM_QUESTION_TITLE_CLASS)
        return label_element.text

    def find_description(self) -> str:
        """Finds the description of the question"""
        description_element = self.card_element.find_element(by=By.CLASS_NAME,
                                                             value=GOOGLE_FORM_QUESTION_DESCRIPTION_CLASS)
        return description_element.text
