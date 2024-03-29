from typing import Optional
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from src.completion.constants import *
from src.completion.util import assign_question_type
from src.decorators import delay
from src.completion.enums import QuestionType
from src.matching.classnames import GOOGLE_FORM_QUESTION_CARD_CLASS, GOOGLE_FORM_SUBMIT_BUTTON_CLASS
from src.completion.Question import Question, ShortTextQuestion, LongTextQuestion, RadioQuestion, SelectQuestion, CheckboxQuestion


class AFWebDriver(Firefox):
    """Extension of the selenium's webdriver for automating form completion"""

    @delay(0)
    def find_element(self, by=By.ID, value: Optional[str] = None) -> WebElement:
        """Delays the find_element operation for debugging purposes"""
        return super().find_element(by, value)

    @delay(0)
    def find_elements(self, by=By.ID, value: Optional[str] = None) -> list[WebElement]:
        """Delays the find_element operation for debugging purposes"""
        return super().find_elements(by, value)

    @delay(T)
    def click(self, element: WebElement) -> None:
        """Delays the element clicking operation for debugging purposes"""
        return element.click()

    def get_all_question_cards(self) -> list[WebElement]:
        # todo: probably delete later
        return self.find_elements(by=By.CLASS_NAME, value=GOOGLE_FORM_QUESTION_CARD_CLASS)

    def get_all_questions(self) -> list[Question]:
        """Finds all questions in a form and creates corresponding instances"""
        question_cards = self.get_all_question_cards()
        constructor_from_type = {
            QuestionType.SHORT_TEXT: ShortTextQuestion,
            QuestionType.LONG_TEXT: LongTextQuestion,
            QuestionType.RADIO: RadioQuestion,
            QuestionType.SELECT: SelectQuestion,
            QuestionType.CHECKBOX: CheckboxQuestion
        }
        return [constructor_from_type[assign_question_type(card)](card) for card in question_cards]

    def find_submit_button(self) -> WebElement:
        """Finds the form's submit button"""
        # todo: error handling?
        return self.find_element(by=By.CLASS_NAME, value=GOOGLE_FORM_SUBMIT_BUTTON_CLASS)

    def submit(self) -> None:
        """Submits the form"""
        submit_button = self.find_submit_button()
        return self.click(submit_button)
