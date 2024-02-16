from typing import Optional
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from src.constants import *
from src.util import delay, concatenate_classname, Question


class FormFiller(Firefox):
    """Utility for automating the process of filling forms.
    Extends the selenium's firefox driver, because chrome bad"""

    @delay(T)
    def __find_element(self, by=By.ID, value: Optional[str] = None) -> WebElement:
        """Delays the find_element operation for debugging purposes"""
        return super().find_element(by, value)

    @delay(T)
    def __find_elements(self, by=By.ID, value: Optional[str] = None) -> list[WebElement]:
        """Delays the find_element operation for debugging purposes"""
        return super().find_elements(by, value)

    @delay(T)
    def click(self, element: WebElement) -> None:
        """Delays the element clicking operation for debugging purposes"""
        return element.click()

    def get_all_questions(self) -> list[Question]:
        """Finds all questions in a form"""
        question_cards = self.__find_elements_by_classname(GOOGLE_FORM_QUESTION_CARD_CLASS)
        # Find label and input elements for each card TODO: radio inputs etc
        label_elements = [card.find_element(by=By.CLASS_NAME, value=GOOGLE_FORM_QUESTION_LABEL_CLASS)
                          for card in question_cards]
        input_elements = [card.find_element(by=By.TAG_NAME, value="input") for card in question_cards]

        return [Question(label_elem, input_elem, input_elem.accessible_name) for label_elem, input_elem in
                zip(label_elements, input_elements)]

    def __find_elements_by_classname(self, classname: str) -> list[WebElement]:
        """Finds elements by the given classname, basically a wrapper which takes care of
        choosing the correct By and formatting the classname"""
        return self.find_elements(by=By.CLASS_NAME, value=concatenate_classname(classname))

    def find_element_by_classname(self, classname: str) -> WebElement:
        """Finds an element by the given classname, basically a wrapper which takes care of
        choosing the correct By and formatting the classname"""
        return self.find_element(by=By.CLASS_NAME, value=concatenate_classname(classname))

    def __find_submit_button(self) -> WebElement:
        """Finds the form's submit button"""
        # todo: error handling
        return self.find_element_by_classname(GOOGLE_FORM_SUBMIT_BUTTON_CLASS)

    def submit(self) -> None:
        """Submits the form"""
        submit_button = self.__find_submit_button()
        return self.click(submit_button)
