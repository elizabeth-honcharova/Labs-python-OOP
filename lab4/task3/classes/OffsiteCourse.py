from lab4.task3.classes.Course import Course
from lab4.task3.interfaces.IOffsiteCourse import IOffsiteCourse


class OffsiteCourse(Course, IOffsiteCourse):
    """the class that represent offsite course"""

    def __init__(self, name, teacher, program):
        """initialize course instance

        Keyword arguments:
        name -- the title of course
        teacher -- the instance of Teacher class
        program -- list of course topics
        """
        super().__init__(name, teacher, program)
