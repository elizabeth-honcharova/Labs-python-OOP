from abc import abstractmethod, ABCMeta


class ICourse(metaclass=ABCMeta):

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
    def program(self):
        """program getter"""
        ...

    @program.setter
    @abstractmethod
    def program(self, course_program):
        """program setter"""
        ...

    @property
    @abstractmethod
    def teacher(self):
        """teacher getter"""
        ...

    @teacher.setter
    @abstractmethod
    def teacher(self, teacher):
        """teacher setter"""
        ...

    def __str__(self):
        return f'Course: {self.name}\nProgram:{self.program}\nTeacher: {self.teacher.name}'
