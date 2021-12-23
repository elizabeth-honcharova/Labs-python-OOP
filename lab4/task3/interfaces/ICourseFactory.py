from abc import ABC, abstractmethod


class ICourseFactory(ABC):
    """the interface for the class that forms a course and adds it to tha database"""

    @abstractmethod
    def form_course(self, course_name: str, teacher_name: str, program_list: list, course_type: str):
        """method that forms course if it is not in the database"""
        ...

    @abstractmethod
    def create_teacher(self, teacher_name: str):
        """method that creates teacher in database if he is not in the database"""
        ...

    @abstractmethod
    def __iter__(self):
        ...
