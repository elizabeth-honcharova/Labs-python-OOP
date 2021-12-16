from lab4.task3.classes.Teacher import Teacher
from lab4.task3.interfaces.ICourse import ICourse


def teacher_adder(setter):
    """decorator that added course to teacher`s list of courses"""
    def wrapper(self, teacher):
        setter(self, teacher)
        teacher.courses.append(self.name)
    return wrapper


class Course(ICourse):

    def __init__(self, name: str, teacher: Teacher, program: list):
        self.name = name
        self.teacher = teacher
        self.program = program

    @property
    def name(self):
        """name getter"""
        return self.__name

    @name.setter
    def name(self, name):
        """name setter"""
        if not isinstance(name, str):
            raise TypeError
        if not name:
            raise ValueError
        self.__name = name

    @property
    def teacher(self):
        """teacher getter"""
        return self.__teacher

    @teacher.setter
    @teacher_adder
    def teacher(self, teacher):
        """teacher setter"""
        if not isinstance(teacher, Teacher):
            raise TypeError
        self.__teacher = teacher

    @property
    def program(self):
        """program getter"""
        return self.__program

    @program.setter
    def program(self, program):
        """program setter"""
        if not all(isinstance(topic, str) for topic in program):
            raise TypeError
        if not program:
            raise ValueError
        self.__program = program


