"""
Практическое задание «ООП: наследование, инкапсуляция и полиморфизм»

Классы:
- Mentor: базовый класс для лекторов и проверяющих.
- Lecturer: класс для лекторов, наследуется от Mentor
- Student: класс для студентов
- Reviewer: класс для проверяющих, наследуется от Mentor

Содержит функции для расчета средних оценок по курсу.
"""


class Mentor:
    """
        Базовый класс для лекторов и проверяющих.

        Атрибуты:
            name (str): Имя наставника
            surname (str): Фамилия наставника
            courses_attached (list): Список прикрепленных курсов
    """
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    """
        Класс для представления лектора.

        Наследуется от класса Mentor

        Атрибуты:
            name (str): Имя
            surname (str): Фамилия
            courses_attached (list): Список курсов
            grades (dict): Оценки по курсам
        """
    def __init__(self, name: str, surname: str):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.average_grade()}\n')

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() < other.average_grade()
        else:
            return NotImplemented

    def __le__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() <= other.average_grade()
        else:
            return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() == other.average_grade()
        else:
            return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() != other.average_grade()
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() > other.average_grade()
        else:
            return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() >= other.average_grade()
        else:
            return NotImplemented

    def average_grade(self) -> float:
        """
               Вычисляет среднюю оценку лектора по всем курсам.

               Returns:
                   float: Средняя оценка, округленная до 2 знаков
        """
        all_grades = []
        for course_grades in self.grades.values():
            all_grades.extend(course_grades)
        if len(all_grades):
            return round(sum(all_grades) / len(all_grades), 2)
        else:
            return 0.0


class Student:
    """
        Класс для представления студента.

        Позволяет оценивать лекторов

        Атрибуты:
            name (str): Имя студента
            surname (str): Фамилия студента
            gender (str): Пол студента
            finished_courses (list): Список завершенных курсов
            courses_in_progress (list): Список текущих курсов
            grades (dict): Оценки по курсам
        """
    def __init__(self, name: str, surname: str, gender: str):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.average_grade()}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}\n')

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() < other.average_grade()
        else:
            return NotImplemented

    def __le__(self, other):
        if isinstance(other, Student):
            return self.average_grade() <= other.average_grade()
        else:
            return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.average_grade() == other.average_grade()
        else:
            return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Student):
            return self.average_grade() != other.average_grade()
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() > other.average_grade()
        else:
            return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Student):
            return self.average_grade() >= other.average_grade()
        else:
            return NotImplemented

    def rate_lecturer(self, lecturer: Lecturer, course: str, grade: int) -> str | None:
        """
               Позволяет студенту оценить лектора.

               Args:
                   lecturer (Lecturer): Лектор, которого нужно оценить
                   course (str): Курс, по которому выставляется оценка
                   grade (int): Оценка

               Returns:
                   str | None: 'Ошибка' если оценка не может быть выставлена, иначе None
        """
        if (isinstance(lecturer, Lecturer) and course in self.courses_in_progress
                and course in lecturer.courses_attached) and isinstance(grade, int):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self) -> float:
        """
               Вычисляет среднюю оценку студента по всем курсам.

               Returns:
                   float: Средняя оценка, округленная до 2 знаков
        """
        all_grades = []
        for course_grades in self.grades.values():
            all_grades.extend(course_grades)
        if len(all_grades):
            return round(sum(all_grades) / len(all_grades), 2)
        else:
            return 0.0


class Reviewer(Mentor):
    """
       Класс для представления проверяющего.

       Наследуется от класса Mentor.

       Позволяет оценивать студентов.

       Атрибуты:
           name (str): Имя проверяющего
           surname (str): Фамилия проверяющего
           courses_attached (list): Список прикрепленных курсов
    """
    def __init__(self, name: str, surname: str):
        super().__init__(name, surname)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

    def rate_student(self, student: Student, course: str, grade: int) -> str | None:
        """
               Позволяет  оценить студента.

               Args:
                   student (Student): Студент, которого нужно оценить
                   course (str): Курс, по которому выставляется оценка
                   grade (int): Оценка (целое число)

               Returns:
                   str | None: 'Ошибка' если оценка не может быть выставлена, иначе None
        """
        if (isinstance(student, Student) and course in student.courses_in_progress
                and course in self.courses_attached and isinstance(grade, int)):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


def average_students_grade(students: list[Student], course: str) -> float:
    """
        Возвращает среднюю оценку всех студентов по определенному курсу.

        Args:
            students (list[Student]): Список объектов Student
            course (str): Название курса

        Returns:
            float: Средняя оценка по курсу, округленная до 2
    """
    grades_list = []
    for student in students:
        student_grades = student.grades.get(course)
        if student_grades:
            grades_list.extend(student_grades)
    if len(grades_list):
        return round(sum(grades_list) / len(grades_list), 2)
    else:
        return 0.0


def average_lecturers_grade(lecturers: list[Lecturer], course: str) -> float:
    """
       Вычисляет среднюю оценку всех лекторов по определенному курсу.

       Args:
           lecturers (list[Lecturer]): Список объектов Lecturer
           course (str): Название курса

       Returns:
           float: Средняя оценка по курсу, округленная до 2 знаков после запятой
    """
    grades_list = []
    for lecturer in lecturers:
        lecturer_grades = lecturer.grades.get(course)
        if lecturer_grades:
            grades_list.extend(lecturer_grades)
    if len(grades_list):
        return round(sum(grades_list) / len(grades_list), 2)
    else:
        return 0.0


student1 = Student('Иван', 'Иванов', 'М')
student1.courses_in_progress += ['Python', 'Java']
student1.finished_courses += ['C++', 'SQL']
student2 = Student('Екатерина', 'Сидорова', 'Ж')
student2.courses_in_progress += ['Python', 'SQL']
student2.finished_courses += ['C++', 'Java']
lecturer1 = Lecturer('Петр', 'Петров')
lecturer1.courses_attached += ['Python', 'SQL']
lecturer2 = Lecturer('Сергей', 'Сергеев')
lecturer2.courses_attached += ['Python', 'Java']
reviewer1 = Reviewer('Антон', 'Антонов')
reviewer1.courses_attached += ['Python', 'Java']
reviewer2 = Reviewer('Александр', 'Александров')
reviewer2.courses_attached += ['SQL']

reviewer1.rate_student(student1, 'Python', 5)
reviewer1.rate_student(student1, 'Python', 4)
reviewer1.rate_student(student1, 'Java', 5)
reviewer1.rate_student(student2, 'Python', 4)
reviewer1.rate_student(student2, 'Python', 3)
reviewer2.rate_student(student2, 'SQL', 5)
reviewer2.rate_student(student2, 'SQL', 4)
student1.rate_lecturer(lecturer1, 'Python', 5)
student1.rate_lecturer(lecturer2, 'Python', 3)
student1.rate_lecturer(lecturer2, 'Java', 5)
student2.rate_lecturer(lecturer1, 'SQL', 5)
student2.rate_lecturer(lecturer1, 'Python', 4)
student2.rate_lecturer(lecturer2, 'Python', 4)

print(student1)
print(student2)
print(lecturer1)
print(lecturer2)
print(reviewer1)
print(reviewer2)

print(student1 < student2)
print(student1 <= student2)
print(student1 == student2)
print(student1 != student2)
print(student1 > student2)
print(student1 >= student2)

print(lecturer1 < lecturer2)
print(lecturer1 <= lecturer2)
print(lecturer1 == lecturer2)
print(lecturer1 != lecturer2)
print(lecturer1 > lecturer2)
print(lecturer1 >= lecturer2)

students_list = [student1, student2]
lecturers_list = [lecturer1, lecturer2]
print(average_students_grade(students_list, 'Python'))
print(average_lecturers_grade(lecturers_list, 'Python'))

