import re
from enums import QuestionTopic, PersonRegardedByQuestion
from dataclasses import dataclass

"""Keyphrases and question templates used to determine how to answer them"""


@dataclass(frozen=True)
class QuestionClassification:
    """Combines the enums defined to describe a question's semantic meaning.
    Based on the QuestionClassification, an answer is chosen"""
    topic: QuestionTopic
    person: PersonRegardedByQuestion


TEAM_NAME_KEYPHRASES = [
    "nazwa drużyny"
]

TEAM_NAME_QUESTIONS = [
    "nazwa drużyny"
]

TEAM_NAME_CLASSIFICATION = QuestionClassification(QuestionTopic.TEAM_NAME, PersonRegardedByQuestion.NONE)

DATA_COLLECTION_KEYPHRASES = [
    "wyrażam zgodę",
    "przetwarzanie",
    "danych osobowych",
    "dane osobowe",
    "podmioty trzecie"
]

DATA_COLLECTION_CLASSIFICATION = QuestionClassification(QuestionTopic.AGREE_FOR_DATA_COLLECTION,
                                                        PersonRegardedByQuestion.NONE)

ANYTHING_ELSE_KEYPHRASES = [
    "coś jeszcze",
    "nas poinformować",
    "poinformować nas",
    "nam przekazać",
    "przekazać nam"
]

ANYTHING_ELSE_QUESTIONS = [
    "czy jest coś o czym chcielibyście nas poinformować?",
    "czy chcecie nam przekazać coś jeszcze?"
]

ANYTHING_ELSE_CLASSIFICATION = QuestionClassification(QuestionTopic.ANYTHING_ELSE, PersonRegardedByQuestion.NONE)

NAME_SURNAME_KEYPHRASES = [
    "imię i nazwisko",
    "nazwisko"
]
# todo: either not make it frozen or define some addition operation to combine the person and question classif?
NAME_SURNAME_CLASSIFICATION = QuestionClassification(QuestionTopic.NAME_SURNAME, PersonRegardedByQuestion.NONE)

NAME_SURNAME_FIRST_PERSON_QUESTIONS = [
    "imię i nazwisko pierwszej osoby",
]
NAME_SURNAME_FIRST_PERSON_CLASSIFICATION = QuestionClassification(QuestionTopic.NAME_SURNAME,
                                                                  PersonRegardedByQuestion.PERSON_ONE)

NAME_SURNAME_SECOND_PERSON_QUESTIONS = [
    "imię i nazwisko drugiej osoby",
]
NAME_SURNAME_SECOND_PERSON_CLASSIFICATION = QuestionClassification(QuestionTopic.NAME_SURNAME,
                                                                   PersonRegardedByQuestion.PERSON_TWO)

DEBATING_STATUS_KEYPHRASES = [
    "status debatancki",
    "status novice",
    "novice"
]

EMAIL_ADDRESS_KEYPHRASES = [
    "e-mail,"
    "email",
    "adres e-mail",
    "adres email"  # todo: regex
]

PHONE_NUMBER_KEYPHRASES = [
    "numer telefonu",
    "nr telefonu"  # todo: regex
]

DIET_KEYPHRASES = [
    "żywieniowe",
    "dieta",
    "dietetyczne"
]

CLUB_MEMBERSHIP_KEYPHRASES = [
    "przynależność do klubu",
    "przynależność klubowa",
    "przynależność instytucjonalna",
    "członkiem",
    "członek"
]

FACEBOOK_PROFILE_KEYPHREASES = [
    "fb",
    "profil",
    "facebook",
    "facebooka"  # todo: maybe regex
]

PLACE_TO_SLEEP_KEYPHRASES = [
    "nocleg",
    "noclegowe",
]

REGARDS_FIRST_PERSON_KEYPHRASES = [
    "pierwsza osoba",
    "pierwszej osoby",
    "pierwszą osobę"  # todo: regex
]

# --------------------------------------------------------------


EMAIL_ADDRESS_FIRST_PERSON_QUESTIONS = [
    "adres email pierwszej osoby",
    "adres e-mail pierwszej osoby",
]

EMAIL_ADDRESS_SECOND_PERSON_QUESTIONS = [
    "adres email drugiej osoby",
    "adres e-mail drugiej osoby",
]

DIET_FIRST_PERSON_QUESTIONS = [
    "preferencje żywieniowe pierwszej osoby",  # todo: regex - startswith?
]

DIET_SECOND_PERSON_QUESTIONS = [
    "preferencje żywieniowe drugiej osoby",  # todo: regex - startswith?
]

CLUB_MEMBERSHIP_FIRST_PERSON_QUESTIONS = [
    "przynależność klubowa pierwszej osoby"
    "przynależność instytucjonalna pierwszej osoby"
]

CLUB_MEMBERSHIP_SECOND_PERSON_QUESTIONS = [
    "przynależność klubowa drugiej osoby"
    "przynależność instytucjonalna drugiej osoby"
]

PLACE_TO_SLEEP_FIRST_PERSON_QUESTIONS = [
    "nocleg w przypadku pierwszej osoby"
]

PLACE_TO_SLEEP_SECOND_PERSON_QUESTIONS = [
    "nocleg w przypadku drugiej osoby"
]

QUESTIONS_AND_KEYPHRASES_MAPPED = {

}
