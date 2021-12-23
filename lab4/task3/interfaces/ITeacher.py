from abc import ABC, abstractmethod


class ITeacher(ABC):

    @property
    @abstractmethod
    def name(self):
        """teacher name getter"""
        ...

    @name.setter
    @abstractmethod
    def name(self, name):
        """teacher name setter"""
        ...

    @property
    @abstractmethod
    def courses(self):
        """getter of list of courses that teach this teacher"""
        ...

    def __str__(self):
        return f'Teacher: {self.name}\nCourses:{self.courses}'
