from enum import Enum


class QuestionType(Enum):
    """Possible question variants in a google form"""
    SHORT_TEXT = 0
    LONG_TEXT = 1
    RADIO = 2
    SELECT = 3
    CHECKBOX = 4
