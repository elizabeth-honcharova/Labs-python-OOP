import pymysql

from lab4.task3.classes.Course import Course
from lab4.task3.classes.OffsiteCourse import OffsiteCourse
from lab4.task3.classes.Teacher import Teacher
from lab4.task3.interfaces.ICourseFactory import ICourseFactory
from lab4.task3.config import host, user, password, database
from lab4.task3.interfaces.LocalCourse import LocalCourse


class CourseFactory(ICourseFactory):

    def __init__(self):
        self.connection = CourseFactory.__connect()

    @staticmethod
    def __connect():
        connector = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=database,
            cursorclass=pymysql.cursors.DictCursor
        )
        return connector

    def form_course(self, course_name: str, teacher_name: str, program_list: list, course_type: str):

        teacher = Teacher(teacher_name)

        if course_type.lower() == "local":
            course = LocalCourse(course_name, teacher, program_list)
        elif course_type == "offsite":
            course = OffsiteCourse(course_name, teacher, program_list)
        else:
            raise ValueError

        self.create_teacher(teacher_name)

        teachers_list = self.__select_all_from_teachers()
        teacher = next((item for item in teachers_list if item["name"] == teacher_name), None)

        teacher_id = teacher['id']

        with self.connection.cursor() as cursor:

            command = "INSERT INTO course (name, teacher_id, program, type)" \
                          "VALUES (%s, %s, %s, %s)"
            values = [course_name, teacher_id, '. '.join(program_list), course_type]
            cursor.execute(command, values)
            self.connection.commit()

        return course

    def create_teacher(self, teacher_name: str):
        teacher = Teacher(teacher_name)

        teachers_list = self.__select_all_from_teachers()
        is_teacher = next((item for item in teachers_list if item["name"] == teacher_name), None)

        if not is_teacher:
            with self.connection.cursor() as cursor:
                command = 'INSERT INTO teacher (name) VALUE (%s)'
                cursor.execute(command, teacher_name)
                self.connection.commit()

        return teacher

    def __select_all_from_courses(self):
        with self.connection.cursor() as cursor:
            command = 'SELECT course.name, teacher.name, program, type ' \
                              'FROM course ' \
                              'JOIN teacher ON course.teacher_id = teacher.id'
            cursor.execute(command)
            fetchall = cursor.fetchall()
        return fetchall

    def __select_all_from_teachers(self):
        with self.connection.cursor() as cursor:
            cursor.execute('SELECT * FROM teacher')
            fetchall = cursor.fetchall()
        return fetchall

    def __iter__(self):
        return CoursesIterator(self.__select_all_from_courses())


class CoursesIterator:
    def __iter__(self):
        return self

    def __init__(self, courses):
        self.courses = courses
        self.index = 0

    def __next__(self):
        if self.index >= len(self.courses):
            raise StopIteration()
        self.index += 1
        return self.courses[self.index-1]

