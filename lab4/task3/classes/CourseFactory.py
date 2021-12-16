import pymysql

from lab4.task3.classes.OffsiteCourse import OffsiteCourse
from lab4.task3.classes.Teacher import Teacher
from lab4.task3.interfaces.ICourseFactory import ICourseFactory
from lab4.task3.config import host, user, password, database
from lab4.task3.classes.LocalCourse import LocalCourse


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
        teacher = self.__is_in_database('teacher', teacher_name)
        teacher_id = teacher['id']

        is_course = self.__is_in_database('course', course_name)
        if not is_course:
            with self.connection.cursor() as cursor:
                command = "INSERT INTO course (name, teacher_id, program, type)" \
                              "VALUES (%s, %s, %s, %s)"
                values = [course_name, teacher_id, '. '.join(program_list), course_type]
                cursor.execute(command, values)
                self.connection.commit()

        return course

    def __is_in_database(self, db, name):
        if db == 'course':
            courses_list = self.__select_all_from_courses()
            result = next((item for item in courses_list if item["name"] == name), None)
        elif db == 'teacher':
            teachers_list = self.__select_all_from_teachers()
            result = next((item for item in teachers_list if item["name"] == name), None)
        else:
            raise ValueError
        return result

    def create_teacher(self, teacher_name: str):
        teacher = Teacher(teacher_name)
        is_teacher = teacher = self.__is_in_database('teacher', teacher_name)
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

