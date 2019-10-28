import argparse
import uuid
import psycopg2
import csv
import os
from employee_dao import EmployeeFactory


NUMBER_OF_RECORDS = 10
CHANGE_PERCENT = 5


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate information for Employees, Clients, Survey to insert into database"
    )
    parser.add_argument(
        "basic_info",
        metavar="J",
        nargs=2,
        type=int,
        help="Usage:\n"
        "- first integer: how much data to create range 1-1.000.000\n"
        "- second integer: change percent \n"

    )
    args = parser.parse_args()
    NUMBER_OF_RECORDS = (args.basic_info[0])
    CHANGE_PERCENT = (args.basic_info[0])
    employees = [EmployeeFactory.generate_employee() for i in range(NUMBER_OF_RECORDS)]
    clients = []
    # print([employee.dismissal_date for employee in employees])
    with open("employee_file.csv", mode="w") as employee_file:
        employee_writer = csv.writer(
            employee_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
        )
        employee_writer.writerow(
            [
                "employee_id",
                "first_name",
                "last_name",
                "dob",
                "gender",
                "employment_date",
                "dismissal_date",
                "education",
                "salary",
            ]
        )
        for employee in employees:
            employee_writer.writerow(vars(employee).values())

    # try:
    #     connection = psycopg2.connect(
    #         user="datawarehouses",
    #         password="datawarehouses",
    #         host="127.0.0.1",
    #         port="5432",
    #         database="datawarehouses",
    #     )
    #     with connection.cursor() as cursor:
    #         base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #         fixture_path = os.path.join(base, "generator/employee_file.csv")
    #         with open(fixture_path) as f:
    #             try:
    #                 next(f)
    #                 cursor.copy_from(f, "employee", sep=",")
    #                 connection.commit()
    #             except UniqueViolation:
    #                 pass
    #         print("copied")
    # except (Exception, psycopg2.Error) as error:
    #     print("Error while connecting to PostgreSQL", error)
