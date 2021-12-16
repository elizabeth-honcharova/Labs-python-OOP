from lab4.task3.interfaces.ITeacher import ITeacher


class Teacher(ITeacher):

    def __init__(self, name: str):
        self.name = name
        self.__courses = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError
        if not name:
            raise ValueError
        self.__name = name

    @property
    def courses(self):
        return self.__courses

