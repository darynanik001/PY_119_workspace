from typing import List
from enum import StrEnum, Enum
import random


class WeekDay(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6


WEEK = (WeekDay.MONDAY, WeekDay.TUESDAY, WeekDay.WEDNESDAY, WeekDay.THURSDAY, WeekDay.FRIDAY, WeekDay.SATURDAY)

random_week_days = random.choices(WEEK)


class Subject(StrEnum):
    DATABASES = "Databases"
    DATA_STRUCTURES = "Data Structures"
    ALGORITHMS = "Algorithms"
    DISCRETE_MATHEMATICS = "Discrete mathematics"
    NETWORKING = "Networking"
    OPERATING_SYSTEMS = "Operating Systems"
    OBJECT_ORIENTED_PROGRAMMING = "Object Oriented Programming"
    PROGRAMMING_LANGUAGES = "Programming Languages"
    WEB_DEVELOPMENT = "Web Development"


class Person:

    def __init__(self, first_name: str, last_name: str, age: int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


class Teacher(Person):

    def __init__(self, first_name: str, last_name: str, age: int, salary: float, subjects: list):
        super().__init__(first_name, last_name, age)
        self.salary = salary
        self.subjects = subjects

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Student(Person):
    def __init__(self, first_name: str, last_name: str, age: int, subjects: List, got_internship: bool):
        super().__init__(first_name, last_name, age)
        self.subjects = subjects
        self.got_internship = got_internship

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Schedule:

    def __init__(self, student: Student):
        self.student = student

    def get_student_schedule(self, student: Student, teachers_lessons_per_week: List):
        schedule = {}

        for student_subject in student.subjects:
            for teacher_full_name, teacher_lessons, week_day in teachers_lessons_per_week:
                if student_subject in teacher_lessons:
                    if teacher_full_name in schedule:
                        schedule[teacher_full_name].append(student_subject)
                    else:
                        schedule[teacher_full_name] = [student_subject]

        return schedule


class University:

    def __init__(self, name: str, location: str, students: List[Student], teachers: List[Teacher]):
        self.name = name
        self.location = location
        self.students = students
        self.teachers = teachers
        self.teachers_lessons_list_per_week = None

    def get_total_students_number(self):
        return len(self.students)

    def get_total_teachers_number(self):
        return len(self.teachers)

    def construct_teachers_to_lessons_list(self):
        self.teachers_lessons_list_per_week = list((teacher.full_name, teacher.subjects,
                                                    WEEK[random.randint(0, len(WEEK) - 1)]) for teacher in
                                                   self.teachers)


if __name__ == "__main__":
    student_1 = Student("Maritza", "Rivers", 18, [Subject.ALGORITHMS, Subject.DATABASES, Subject.NETWORKING,
                                                  Subject.WEB_DEVELOPMENT], True)
    student_2 = Student("Alex", "Compton", 19,
                        [Subject.WEB_DEVELOPMENT, Subject.PROGRAMMING_LANGUAGES, Subject.ALGORITHMS,
                         Subject.DATABASES], True)
    student_3 = Student("Catalina", "Potter", 21,
                        [Subject.PROGRAMMING_LANGUAGES, Subject.WEB_DEVELOPMENT, Subject.OBJECT_ORIENTED_PROGRAMMING,
                         Subject.ALGORITHMS], True)

    teacher_1 = Teacher("Bruno", "Morton", 25, 23000, [Subject.ALGORITHMS, Subject.DATA_STRUCTURES])
    teacher_2 = Teacher("Olive", "Wise", 27, 23000, [Subject.PROGRAMMING_LANGUAGES, Subject.DISCRETE_MATHEMATICS])
    teacher_3 = Teacher("Leonard", "Bernard", 29, 23000, [Subject.WEB_DEVELOPMENT, Subject.DATABASES])
    teacher_4 = Teacher("Rico", "Hodge", 25, 23000, [Subject.NETWORKING, Subject.OPERATING_SYSTEMS])
    university = University("Harvard", "Cambridge", [student_1, student_2, student_3],
                            [teacher_1, teacher_2, teacher_3, teacher_4])
    university.construct_teachers_to_lessons_list()
    print(university.teachers_lessons_list_per_week)
    schedule = Schedule(student_2)
    print(schedule.get_student_schedule(student_1, university.teachers_lessons_list_per_week))
