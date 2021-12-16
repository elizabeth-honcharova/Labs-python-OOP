from abc import ABC, abstractmethod


class ITeacher(ABC):

    @property
    @abstractmethod
    def name(self):
        """name getter"""
        ...

    @name.setter
    @abstractmethod
    def name(self, name):
        """name setter"""
        ...

    @property
    @abstractmethod
    def courses(self):
        """courses getter"""
        ...

    def __str__(self):
        return f'Teacher: {self.name}\nCourses:{self.courses}'
