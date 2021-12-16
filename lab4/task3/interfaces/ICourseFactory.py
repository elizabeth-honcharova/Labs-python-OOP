from abc import ABC, abstractmethod

from lab4.task3.classes.Teacher import Teacher


class ICourseFactory(ABC):

    @abstractmethod
    def form_course(self, course_name: str, teacher_name: str, program_list: list, course_type: str):
        ...

    @abstractmethod
    def create_teacher(self, teacher_name: str):
        ...

    @abstractmethod
    def __iter__(self):
        ...
