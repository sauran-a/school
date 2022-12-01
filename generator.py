import json
from app import app
from faker import Faker
from random import randint, sample, choice
from models import GroupModel, StudentModel, CourseModel, engine
from sqlalchemy.orm.session import sessionmaker


fake = Faker()
session = sessionmaker(bind=engine)()


# Populate groups
"""
def generate_groups():
    groups = list()
    for _ in range(10):
        new_group_ = fake.pystr_format(string_format='??-##', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        groups.append(new_group_)
    return groups


groups_obj = list()
for group in generate_groups():
    new_group = GroupModel(name=group)
    groups_obj.append(new_group)

session.add_all(groups_obj)
session.commit()
"""


# Populated students
"""
def generate_first_names():
    first_names = list()
    for _ in range(20):
        first_names.append(fake.first_name())
    return first_names


def generate_last_names():
    last_names = list()
    for _ in range(20):
        last_names.append(fake.last_name())
    return last_names


first_names_list = generate_first_names()
last_names_list = generate_last_names()
students = list()
for _ in range(200):
    student = {'first_name': choice(first_names_list), 'last_name': choice(last_names_list)}
    students.append(student)

students_obj = list()
for student in students:
    group_id = randint(1, 10)
    c = session.query(StudentModel).filter_by(group_id=group_id)
    if len(c.all()) <= 30:
        new_student = StudentModel(first_name=student['first_name'],
                                   last_name=student['last_name'], group_id=group_id)
        students_obj.append(new_student)
    else:
        continue
session.add_all(students_obj)
session.commit()
"""


# Populated courses
"""
courses = ['algebra', 'geometry', 'history', 'english', 'biology',
           'art', 'chemistry', 'physics', 'spanish', 'trigonometry']
courses_obj = list()
for course in courses:
    new_course = CourseModel(name=course, description=None)
    courses_obj.append(new_course)
session.add_all(courses_obj)
session.commit()
"""


# Assign from 1 to 3 courses to each student
"""
students = session.query(StudentModel).all()
courses = session.query(CourseModel).all()
for student in students:
    courses_chosen = sample(courses, randint(1, 3))
    for course in courses_chosen:
        student.courses.append(course)
        session.commit()
"""

session.close()
