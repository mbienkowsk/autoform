from loguru import logger
from src.FormFiller import FormFiller
from src.constants import FORM1, FORM2, FORM3

def main():
    with FormFiller() as driver:
        # for form in [FORM1, FORM2, FORM3]:
        # form = "https://forms.gle/ExpQWBJPevGmL8K48"
        driver.get(FORM1)
        driver.implicitly_wait(.5)
        questions = driver.get_all_questions()
        logger.debug(questions)


if __name__ == "__main__":
    main()
