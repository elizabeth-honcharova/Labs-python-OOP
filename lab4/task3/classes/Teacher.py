from lab4.task3.interfaces.ITeacher import ITeacher


class Teacher(ITeacher):
    """the class that store data about the teacher"""

    def __init__(self, name: str):
        """initialize course instance
        Keyword arguments:
        name -- the name of the teacher
        """
        self.name = name
        self.__courses = []

    @property
    def name(self):
        """teacher name getter"""
        return self.__name

    @name.setter
    def name(self, name):
        """teacher name setter"""
        if not isinstance(name, str):
            raise TypeError
        if not name:
            raise ValueError
        self.__name = name

    @property
    def courses(self):
        """getter of list of courses that teach this teacher"""
        return self.__courses

