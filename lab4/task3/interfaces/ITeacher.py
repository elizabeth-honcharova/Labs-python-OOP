from abc import ABC, abstractmethod


class ITeacher(ABC):

    @property
    @abstractmethod
    def name(self):
        ...

    @name.setter
    @abstractmethod
    def name(self, name):
        ...

    @property
    @abstractmethod
    def courses(self):
        ...

    def __str__(self):
        return f'Teacher: {self.name}\nCourses:{self.courses}'
