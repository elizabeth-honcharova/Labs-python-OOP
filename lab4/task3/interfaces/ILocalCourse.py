from abc import ABC

from lab4.task3.interfaces.ICourse import ICourse


class ILocalCourse(ICourse, ABC):
    """the interface for the local course class"""

    def __str__(self):
        return f'Local course: {self.name}\nProgram:{self.program}\nTeacher: {self.teacher.name}'
