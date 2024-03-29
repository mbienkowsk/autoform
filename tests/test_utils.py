from src.completion.AFWebDriver import AFWebDriver
from src.completion.constants import TEST_FORM
from src.completion.util import assign_question_type
from src.completion.enums import QuestionType


def test_assigns_correct_types():
    with AFWebDriver() as driver:
        driver.get(TEST_FORM)
        cards = driver.get_all_question_cards()
        assert len(cards) == 5

        question_types = [assign_question_type(card) for card in cards]
        assert question_types[0] == QuestionType.SELECT
        assert question_types[1] == QuestionType.LONG_TEXT
        assert question_types[2] == QuestionType.SHORT_TEXT
        assert question_types[3] == QuestionType.RADIO
        assert question_types[4] == QuestionType.CHECKBOX
