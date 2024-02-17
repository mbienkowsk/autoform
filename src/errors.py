class InvalidQuestionTypeError(TypeError):
    """Thrown when a question card does not fit any of the supported types"""


class InvalidAnswerError(ValueError):
    """Thrown when an answer given to a close-ended question does not match any of the possible ones"""
