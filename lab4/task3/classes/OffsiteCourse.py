from lab4.task3.classes.Course import Course
from lab4.task3.interfaces.IOffsiteCourse import IOffsiteCourse


class OffsiteCourse(Course, IOffsiteCourse):

    def __init__(self, name, teacher, program):
        super().__init__(name, teacher, program)
