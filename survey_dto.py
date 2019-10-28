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
      
        return EmployeeDTO(
            id=id,
            fk_employee=fk_employee,
            fk_client=fk_client,
            fk_survey=fk_survey,
            id_answers=id_answers,
            datetime=datetime,
            email_or_phone=email_or_phone,
            is_completed=is_completed,
        )
