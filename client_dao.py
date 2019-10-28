from random_data import education
import random
from random import randrange
from datetime import datetime
from faker import Faker
from faker.providers import date_time
import uuid


class ClientDAO:
    def __init__(
        self,
        id,
        first_name=None,
        last_name=None,
        dob=None,
        gender=None,
        profession=None,
        has_kids=None,
        education=None,
        email=None,
        phone = None,
        last_called= None,
        is_married=None
    ):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.gender = gender
        self.profession = profession
        self.has_kids = has_kids
        self.education = education
        self.email = email
        self.phone = phone
        self.last_called = last_called
        self.is_married = is_married


class EmployeeFactory:
    @staticmethod
    def generate_employee():
        faker = Faker()
        id = uuid.uuid4()
        random_gender = randrange(0, 2)
        if random_gender:
            gender = 1
            first_name = faker.first_name_male()
            # first_name = random.choice(male_first_names)
        else:
            gender = 0
            # first_name = random.choice(female_first_names)
            first_name = faker.first_name_female()
        last_name = faker.last_name()
        dob = faker.date_of_birth(minimum_age=18, maximum_age=70)
        profession = faker.job()
        email = faker.email()
        phone = faker.phone()
        last_called = faker.date.past(2,"2019-09-01")
        if random_married:
            is_married = 
        return EmployeeDAO(
            id=id,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            dob=dob,
            employment_date=employment_date,
            dismissal_date=dismissal_date,
            education=random.choice(education),
            salary=randrange(2000, 5000, 100),
        )
