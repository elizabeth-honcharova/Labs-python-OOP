from lab4.task3.classes.Teacher import Teacher
from lab4.task3.interfaces.ICourse import ICourse


def teacher_adder(setter):
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
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError
        if not name:
            raise ValueError
        self.__name = name

    @property
    def teacher(self):
        return self.__teacher

    @teacher.setter
    @teacher_adder
    def teacher(self, teacher):
        if not isinstance(teacher, Teacher):
            raise TypeError
        self.__teacher = teacher

    @property
    def program(self):
        return self.__program

    @program.setter
    def program(self, program):
        if not all(isinstance(topic, str) for topic in program):
            raise TypeError
        if not program:
            raise ValueError
        self.__program = program


