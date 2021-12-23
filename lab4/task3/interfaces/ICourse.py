from abc import abstractmethod, ABCMeta


class ICourse(metaclass=ABCMeta):
    """the interface for course"""

    @property
    @abstractmethod
    def name(self):
        """the title of course getter"""
        ...

    @name.setter
    @abstractmethod
    def name(self, name):
        """the title of course setter"""
        ...

    @property
    @abstractmethod
    def program(self):
        """program of course getter"""
        ...

    @program.setter
    @abstractmethod
    def program(self, course_program):
        """program of course setter"""
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
