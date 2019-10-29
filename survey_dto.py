import random
from random import randrange
from datetime import datetime
from faker import Faker
from faker.providers import date_time
import uuid


class ConductedSurveyDTO:
    def __init__(
        self,
        id,
        fk_employee=None,
        fk_client=None,
        fk_survey=None,
        id_answers=None,
        datetime=None,
        email_or_phone=None,
        is_completed=None,
    ):
        self.id = id
        self.fk_employee = fk_employee
        self.fk_client = fk_client
        self.fk_survey = fk_survey
        self.id_answers = id_answers
        self.datetime = datetime
        self.email_or_phone = email_or_phone
        self.is_completed = is_completed


class ConductedSurveyFactory:
    @staticmethod
    def generate_conducted_survey():
        faker = Faker()
        id = uuid.uuid4()
        fk_employee = None
        fk_client = None
        fk_survey = None
        id_answers = None
        datetime = None
        email_or_phone = None
        is_completed = None
        return ConductedSurveyDTO(
            id=id,
            fk_employee=fk_employee,
            fk_client=fk_client,
            fk_survey=fk_survey,
            id_answers=id_answers,
            datetime=datetime,
            email_or_phone=email_or_phone,
            is_completed=is_completed,
        )
    
class SurveyDTO:
    def __init__(
        self,
        id,
        survey_content=None,
        title=None,
        company_name=None,
        survey_html=None,
    ):
        self.id = id
        self.survey_content = survey_content
        self.title = title
        self.company_name = company_name
        self.survey_html = survey_html


class SurveyFactory:
    @staticmethod
    def generate_survey():
        faker = Faker()
        id = uuid.uuid4()
        survey_content = None
        title = None
        company_name = faker.company()
        survey_html = None

        return SurveyDTO(
            id,
            survey_content=survey_content,
            title=title,
            company_name=company_name,
            survey_html=survey_html
        )

