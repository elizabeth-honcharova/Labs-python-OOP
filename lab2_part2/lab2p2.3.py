class Student:

    all_record_books = list()
    all_names = list()

    def __new__(cls, full_name, n_record_book, **grades):
        if n_record_book in cls.all_record_books:
            raise Exception("Instance wasn`t created. Student with the same record book already exist.")
        if full_name in cls.all_names:
            raise Exception("Instance wasn`t created. Student with the same name already exist.")
        return super(Student, cls).__new__(cls)

    def __init__(self, full_name, n_record_book, **grades):
        self.full_name = full_name
        self.n_record_book = n_record_book
        self.grades = grades

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, full_name):
        if not isinstance(full_name, str):
            raise TypeError("Invalid name")
        if not full_name:
            raise ValueError("Invalid name")
        if full_name in self.all_names:
            raise ValueError("Invalid name")
        self.__full_name = full_name
        self.all_names.append(full_name)

    @property
    def n_record_book(self):
        return self.__n_record_book

    @n_record_book.setter
    def n_record_book(self, n_record_book):
        if not isinstance(n_record_book, str):
            raise TypeError("Invalid number of record_book")
        if n_record_book in self.all_record_books:
            raise ValueError("Invalid number of record_book")
        self.__n_record_book = n_record_book
        self.all_record_books.append(n_record_book)

    @property
    def grades(self):
        return self.__grades

    @grades.setter
    def grades(self, grades):
        if not all(isinstance(key, str) for key in grades):
            raise TypeError("Invalid key")
        if not all(isinstance(value, (int,float)) for value in grades.values()):
            raise TypeError("Invalid value")
        if not all(value > 0 for value in grades.values()):
            raise ValueError("Invalid value")
        self.__grades = grades

    def average_score(self):
        av_score = 0.0
        for mark in self.grades.values():
            av_score += mark
        return av_score / len(self.grades)


class Group:

    __students_num = 0

    def __new__(cls, *students):
        if len(students) > 20:
            raise Exception("Instance wasn`t created. Max size of group is 20.")
        return super(Group, cls).__new__(cls)

    def __init__(self, *students):
        for student in students:
            if not isinstance(student, Student):
                raise TypeError("Invalid students")
        self.students = students
        Group.__students_num += len(students)

    @property
    def students(self):
        return self.__students

    @students.setter
    def students(self, students):
        if not all(isinstance(student, Student) for student in students):
            raise TypeError("Invalid students")
        if len(students) > 20:
            raise ValueError("Invalid number of students")
        self.__students = list(students)
        Group.__students_num += len(students)

    def add_student(self, student):
        if Group.__students_num > 20:
            raise Exception("Too many students")
        if not isinstance(student, Student):
            raise TypeError("Invalid student")
        if student in self.__students:
            raise ValueError("Invalid student")
        self.__students.append(student)
        Group.__students_num += 1

    def del_student(self, n_record_book):
        if not isinstance(n_record_book, str):
            raise TypeError("Invalid number of record_book")
        for student in self.students:
            if student.n_record_book == n_record_book:
                self.__students.remove(student)
                Group.__students_num -= 1
                break

    def success_list(self):
        suc_dict = dict()
        for i in self.students:
            suc_dict[i.full_name] = i.average_score()
        suc_list = list(suc_dict.items())
        suc_list.sort(key=lambda i: i[1], reverse=True)
        return suc_list

    def top_five(self):
        print(self.success_list()[:5])


if __name__ == "__main__":

    Olya = Student("Olya Grishki", "34T4353636", math=5, PE=3.4)
    Dasha = Student("Dasha Bibko", "464g435", math=2, PE=5)
    Sasha = Student("Sasha Gog", "45GG435", math=4.8, PE=4.9)

    ti_02 = Group(Olya, Dasha, Sasha)
    ti_02.top_five()

    Olya2 = Student("Olyaa Grishki", "34T4356", math=5, PE=3.4)
    Bib = Student("Zuchka", "4", b=2, PE=6, bab=1)
    ti_01 = Group(Bib)
    ti_01.add_student(Sasha)
    ti_01.top_five()
    ti_01.del_student("45GG435")
    ti_01.top_five()
