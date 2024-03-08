import re
from enums import QuestionTopic, PersonRegardedByQuestion
from dataclasses import dataclass

"""Keyphrases and question templates used to determine how to answer them"""


@dataclass(frozen=True)
class QuestionClassification:
    """Combines the enums defined to describe a question's semantic meaning.
    Based on the QuestionClassification, an answer is chosen"""
    topic: QuestionTopic | None
    person: PersonRegardedByQuestion | None


# DATA COLLECTION
TEAM_NAME_KEYPHRASES = ["nazwa drużyny"]
TEAM_NAME_QUESTIONS = ["nazwa drużyny"]
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

# ANYTHING ELSE?
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


# NAME AND SURNAME
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

NAME_SURNAME_SECOND_PERSON_QUESTIONS = ["imię i nazwisko drugiej osoby"]

NAME_SURNAME_SECOND_PERSON_CLASSIFICATION = QuestionClassification(QuestionTopic.NAME_SURNAME,
                                                                   PersonRegardedByQuestion.PERSON_TWO)

# DEBATING STATUS
DEBATING_STATUS_KEYPHRASES = [
    "status debatancki",
    "status novice",
    "novice"
]

# EMAIL ADDRESS
EMAIL_ADDRESS_KEYPHRASES = [
    "e-mail,"
    "email",
    "adres e-mail",
    "adres email"  # todo: regex
]

EMAIL_ADDRESS_FIRST_PERSON_QUESTIONS = [
    "adres email pierwszej osoby",
    "adres e-mail pierwszej osoby",
]
EMAIL_ADDRESS_FIRST_PERSON_CLASSIFICATION = QuestionClassification(QuestionTopic.EMAIL_ADDRESS,
                                                                   PersonRegardedByQuestion.PERSON_ONE)
EMAIL_ADDRESS_SECOND_PERSON_QUESTIONS = [
    "adres email drugiej osoby",
    "adres e-mail drugiej osoby",
]

EMAIL_ADDRESS_SECOND_PERSON_CLASSIFICATION = QuestionClassification(QuestionTopic.EMAIL_ADDRESS,
                                                                    PersonRegardedByQuestion.PERSON_TWO)
PHONE_NUMBER_KEYPHRASES = [
    "numer telefonu",
    "nr telefonu"  # todo: regex
]

PHONE_NUMBER_FIRST_PERSON_QUESTIONS = [
    "numer telefonu pierwszej osoby",
]
PHONE_NUMBER_FIRST_PERSON_CLASSIFICATION = QuestionClassification(QuestionTopic.PHONE_NUMBER,
                                                                  PersonRegardedByQuestion.PERSON_ONE)
PHONE_NUMBER_SECOND_PERSON_QUESTIONS = [
    "numer telefonu drugiej osoby"
]
PHONE_NUMBER_SECOND_PERSON_CLASSIFICATION = QuestionClassification(QuestionTopic.PHONE_NUMBER,
                                                                   PersonRegardedByQuestion.PERSON_TWO)

DIET_KEYPHRASES = [
    "żywieniowe",
    "dieta",
    "dietetyczne"
]

DIET_FIRST_PERSON_QUESTIONS = [
    "preferencje żywieniowe pierwszej osoby",  # todo: regex - startswith?
]
DIET_FIRST_PERSON_CLASSIFICATION = QuestionClassification(QuestionTopic.DIET, PersonRegardedByQuestion.PERSON_ONE)

DIET_SECOND_PERSON_QUESTIONS = [
    "preferencje żywieniowe drugiej osoby",  # todo: regex - startswith?
]
DIET_SECOND_PERSON_CLASSIFICATION = QuestionClassification(QuestionTopic.DIET, PersonRegardedByQuestion.PERSON_TWO)

CLUB_MEMBERSHIP_KEYPHRASES = [
    "przynależność do klubu",
    "przynależność klubowa",
    "przynależność instytucjonalna",
    "członkiem",
    "członek"
]

CLUB_MEMBERSHIP_FIRST_PERSON_QUESTIONS = [
    "przynależność klubowa pierwszej osoby"
    "przynależność instytucjonalna pierwszej osoby"
]
CLUB_MEMBERSHIP_FIRST_PERSON_CLASSIFICATION = QuestionClassification(QuestionTopic.CLUB_MEMBERSHIP,
                                                                     PersonRegardedByQuestion.PERSON_ONE)

CLUB_MEMBERSHIP_SECOND_PERSON_QUESTIONS = [
    "przynależność klubowa drugiej osoby"
    "przynależność instytucjonalna drugiej osoby"
]
CLUB_MEMBERSHIP_SECOND_PERSON_CLASSIFICATION = QuestionClassification(QuestionTopic.CLUB_MEMBERSHIP,
                                                                      PersonRegardedByQuestion.PERSON_TWO)

FACEBOOK_PROFILE_KEYPHRASES = [
    "fb",
    "profil",
    "facebook",
    "facebooka"  # todo: maybe regex
]

PLACE_TO_SLEEP_KEYPHRASES = [
    "nocleg",
    "noclegowe",
]

PLACE_TO_SLEEP_FIRST_PERSON_QUESTIONS = [
    "nocleg w przypadku pierwszej osoby"
]
PLACE_TO_SLEEP_FIRST_PERSON_CLASSIFICATION = QuestionClassification(QuestionTopic.PLACE_TO_SLEEP,
                                                                    PersonRegardedByQuestion.PERSON_ONE)

PLACE_TO_SLEEP_SECOND_PERSON_QUESTIONS = [
    "nocleg w przypadku drugiej osoby"
]
PLACE_TO_SLEEP_SECOND_PERSON_CLASSIFICATION = QuestionClassification(QuestionTopic.PLACE_TO_SLEEP,
                                                                     PersonRegardedByQuestion.PERSON_TWO)

REGARDS_FIRST_PERSON_KEYPHRASES = [
    "pierwsza osoba",
    "pierwszej osoby",
    "pierwszą osobę"  # todo: regex
]

REGARDS_SECOND_PERSON_KEYPHRASES = [
    "druga osoba",
    "drugiej osoby",
    "drugą osobę"
]

questions_to_classifications = {
    # Maps questions to respective classifications; if a question is equal to any in the list, it gets classified
    TEAM_NAME_QUESTIONS: TEAM_NAME_CLASSIFICATION,
    ANYTHING_ELSE_QUESTIONS: ANYTHING_ELSE_CLASSIFICATION,
    NAME_SURNAME_FIRST_PERSON_QUESTIONS: NAME_SURNAME_FIRST_PERSON_CLASSIFICATION,
    NAME_SURNAME_SECOND_PERSON_QUESTIONS: NAME_SURNAME_SECOND_PERSON_CLASSIFICATION,
    EMAIL_ADDRESS_FIRST_PERSON_QUESTIONS: EMAIL_ADDRESS_FIRST_PERSON_CLASSIFICATION,
    EMAIL_ADDRESS_SECOND_PERSON_QUESTIONS: EMAIL_ADDRESS_SECOND_PERSON_CLASSIFICATION,
    PHONE_NUMBER_FIRST_PERSON_QUESTIONS: PHONE_NUMBER_FIRST_PERSON_CLASSIFICATION,
    PHONE_NUMBER_SECOND_PERSON_QUESTIONS: PHONE_NUMBER_SECOND_PERSON_CLASSIFICATION,
    DIET_FIRST_PERSON_QUESTIONS: DIET_FIRST_PERSON_CLASSIFICATION,
    DIET_SECOND_PERSON_QUESTIONS: DIET_SECOND_PERSON_CLASSIFICATION,
    CLUB_MEMBERSHIP_FIRST_PERSON_QUESTIONS: CLUB_MEMBERSHIP_FIRST_PERSON_CLASSIFICATION,
    CLUB_MEMBERSHIP_SECOND_PERSON_QUESTIONS: CLUB_MEMBERSHIP_SECOND_PERSON_CLASSIFICATION,
    PLACE_TO_SLEEP_FIRST_PERSON_QUESTIONS: PLACE_TO_SLEEP_FIRST_PERSON_CLASSIFICATION,
    PLACE_TO_SLEEP_SECOND_PERSON_QUESTIONS: PLACE_TO_SLEEP_SECOND_PERSON_CLASSIFICATION
}

keywords_to_classifications = {
    TEAM_NAME_KEYPHRASES: TEAM_NAME_CLASSIFICATION,
    DATA_COLLECTION_KEYPHRASES: DATA_COLLECTION_CLASSIFICATION,
    ANYTHING_ELSE_KEYPHRASES: ANYTHING_ELSE_CLASSIFICATION,
}
