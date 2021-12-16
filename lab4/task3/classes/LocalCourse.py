from lab4.task3.classes.Course import Course
from lab4.task3.interfaces.ILocalCourse import ILocalCourse


class LocalCourse(Course, ILocalCourse):

    def __init__(self, name, teacher, program):
        super().__init__(name, teacher, program)
