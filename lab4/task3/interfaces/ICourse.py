from abc import abstractmethod, ABCMeta


class ICourse(metaclass=ABCMeta):

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
    def program(self):
        ...

    @program.setter
    @abstractmethod
    def program(self, course_program):
        ...

    @property
    @abstractmethod
    def teacher(self):
        ...

    @teacher.setter
    @abstractmethod
    def teacher(self, teacher):
        ...

    def __str__(self):
        return f'Course: {self.name}\nProgram:{self.program}\nTeacher: {self.teacher.name}'
