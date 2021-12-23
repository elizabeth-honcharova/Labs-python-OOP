from lab4.task3.classes.Course import Course
from lab4.task3.interfaces.ILocalCourse import ILocalCourse


class LocalCourse(Course, ILocalCourse):
    """the class that represent local course"""

    def __init__(self, name, teacher, program):
        """initialize course instance

        Keyword arguments:
        name -- the title of course
        teacher -- the instance of Teacher class
        program -- list of course topics
        """
        super().__init__(name, teacher, program)
