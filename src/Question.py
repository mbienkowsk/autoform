from selenium.webdriver.remote.webelement import WebElement
from abc import ABC, abstractmethod
from loguru import logger
from selenium.webdriver.common.by import By
from src.classnames import *
from typing import Optional
from selenium.common.exceptions import NoSuchElementException

from src.constants import T
from src.errors import InvalidAnswerError
from src.util import delay


class Question(ABC):
    """Represents a form question and all the data related to it"""

    def __init__(self, card_elem: WebElement):
        self.card_element = card_elem
        self.title = self.find_title()
        self.description = desc if (desc := self.find_description()) else None
        self.required = self.find_whether_required()
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

    def find_whether_required(self) -> bool:
        """Returns a bool indicating whether answering the question is required to
        submit the form"""
        is_required_div_present = len(
            self.card_element.find_elements(by=By.CLASS_NAME, value=GOOGLE_FORM_QUESTION_REQUIRED_DIV_CLASS)) > 0
        return is_required_div_present

    def find_text_input(self) -> Optional[WebElement]:
        """Returns the first text input in the question's card element or None
        if there are none"""
        inputs = self.card_element.find_elements(by=By.TAG_NAME, value="input")
        text_inputs = list(filter(lambda elem: elem.get_attribute("type") == "text", inputs))
        return None if not text_inputs else text_inputs[0]


class OpenEndedQuestion(Question):
    """Question which requires a text-based answer by filling in a textinput or a textarea"""

    def __init__(self, card_elem: WebElement):
        super().__init__(card_elem)
        self.input_element: WebElement = self.find_input_element()

    @delay(T)
    @abstractmethod
    def find_input_element(self) -> WebElement:
        """Finds the input element, where the answer should be entered"""
        ...

    @delay(T)
    def enter_answer(self, answer: str) -> None:
        """Fills in the question's input element with the provided answer"""
        self.input_element.send_keys(answer)


class ShortTextQuestion(OpenEndedQuestion):
    def find_input_element(self) -> WebElement:
        """Finds the input element, where the answer should be entered"""
        text_input = self.find_text_input()
        if text_input is None:
            raise NoSuchElementException("Text input not found in a short text question")
        return text_input


class LongTextQuestion(OpenEndedQuestion):
    def find_input_element(self) -> WebElement:
        """Finds the textarea element, where the answer should be entered"""
        return self.card_element.find_element(by=By.TAG_NAME, value="textarea")


class CloseEndedQuestion(Question):
    """Represents the radio input, select and checkbox questions"""

    def __init__(self, card_elem: WebElement):
        super().__init__(card_elem)
        self.options: dict[str, WebElement] = self.create_answer_mapping()
        self.other_text_input: WebElement = self.find_text_input()  # targets the optional "Other: " field
        self.multi_choice: bool

    @abstractmethod
    def create_answer_mapping(self) -> dict[str, WebElement]:
        """Creates a dictionary with pairs {answer_string: answer_web_element},
        where clicking a given element results in selecting the answer in the key"""
        ...

    @delay(T)
    def answer_other_question(self, answer: str) -> None:
        """Fills in the optional "other" field with the provided answer. The field is automatically
        selected after an answer is entered"""
        if self.other_text_input is None:
            raise NoSuchElementException("This question does not contain an open-ended part")
        self.other_text_input.send_keys(answer)

    @delay(T)
    def select_option(self, option: str) -> None:
        """Selects the chosen option"""
        if option not in list(self.options.keys()):
            raise InvalidAnswerError("Provided answer is not a valid one for this multi-choice question!")
        self.options[option].click()


class RadioQuestion(CloseEndedQuestion):
    """Represents the single-answer radio input question"""

    def __init__(self, card_elem: WebElement):
        super().__init__(card_elem)
        self.multi_choice = False

    def create_answer_mapping(self) -> dict[str, WebElement]:
        """Creates a dictionary with pairs {answer_string: answer_web_element},
        where clicking a given element results in selecting the answer in the key"""
        option_elements = self.card_element.find_elements(by=By.CLASS_NAME, value=GOOGLE_FORM_RADIO_OPTION_CLASS)
        mapping = {element.text: element for element in option_elements if element.text != "Other:"}
        return mapping


class CheckboxQuestion(CloseEndedQuestion):
    """Represents the multi-choice equivalent of the radio question"""

    def __init__(self, card_elem: WebElement):
        super().__init__(card_elem)
        self.multi_choice = True

    def create_answer_mapping(self) -> dict[str, WebElement]:
        """Creates a dictionary with pairs {answer_string: answer_web_element},
        where clicking a given element results in selecting the answer in the key
        """
        option_elements = self.card_element.find_elements(by=By.CLASS_NAME, value=GOOGLE_FORM_CHECKBOX_OPTION_CLASS)
        mapping = {element.text: element for element in option_elements if element.text != "Other:"}
        return mapping


class SelectQuestion(CloseEndedQuestion):
    """Represents the dropdown select question"""

    def __init__(self, card_elem: WebElement):
        self.dropdown = SelectQuestion.find_dropdown(card_elem)
        super().__init__(card_elem)
        self.multi_choice = False

    @staticmethod
    def find_dropdown(card_element: WebElement) -> WebElement:
        """Finds the dropdown in a given select question card element"""
        return card_element.find_element(by=By.CLASS_NAME, value=GOOGLE_FORM_SELECT_CLASS)

    def open_dropdown(self):
        """Clicks the dropdown to open it"""
        self.dropdown.click()

    def create_answer_mapping(self) -> dict[str, WebElement]:
        """Creates a dictionary with pairs {answer_string: answer_web_element},
        where clicking a given element results in selecting the answer in the key
        """
        self.open_dropdown()
        # since there is 2*n divs with the same option class, of which only n are clickable for n answers, find the
        # parent of the clickable ones
        input_parent = self.card_element.find_element(by=By.CLASS_NAME, value=GOOGLE_FORM_SELECT_OPEN_DROPDOWN)
        option_elements = input_parent.find_elements(by=By.CLASS_NAME, value=GOOGLE_FORM_SELECT_OPTION_CLASS)
        mapping = {element.accessible_name: element for element in option_elements if element.text != "Other:"}
        return mapping

    def select_option(self, option: str) -> None:
        """Makes the dropdown visible and selects the chosen option"""
        # self.open_dropdown()
        super().select_option(option)

    # TODO: find separator, implement close_dropdown, clean it up
