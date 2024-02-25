from enum import Enum


class QuestionType(Enum):
    """Possible question variants in a google form"""
    SHORT_TEXT = 0
    LONG_TEXT = 1
    RADIO = 2
    SELECT = 3
    CHECKBOX = 4


class QuestionTopic(Enum):
    """Topic of the question regarding the debating tournament signups"""
    # these questions appear once, they regard the team as a whole
    TEAM_NAME = 0,
    AGREE_FOR_DATA_COLLECTION = 1,
    NECESSARY_AGREEMENT = 2,
    ANYTHING_ELSE = 3,

    # these usually appear twice as they regard either one of the two members
    NAME_SURNAME = 4,
    NOVICE_OR_NOT = 5,
    EMAIL_ADDRESS = 6,
    PHONE_NUMBER = 7,
    DIET = 8,
    CLUB_MEMBERSHIP = 9,
    FACEBOOK_PROFILE = 10,
    PLACE_TO_SLEEP = 11,


class PersonRegardedByQuestion(Enum):
    """Some of the questions appear twice in the form as a team
    usually consists of two people and regard one of the members. This
    is represented by this enum"""
    NONE = 0,
    PERSON_ONE = 1,
    PERSON_TWO = 2
