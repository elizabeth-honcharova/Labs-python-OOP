from abc import ABC

from lab4.task3.interfaces.ICourse import ICourse


class IOffsiteCourse(ICourse, ABC):

    def __str__(self):
        return f'Offsite course: {self.name}\nProgram:{self.program}\nTeacher: {self.teacher.name}'
