class Student:

    all_names = list()

    def __new__(cls, full_name, n_record_book, **grades):
        if full_name in cls.all_names:
            print("Instance wasn`t created. Student with the same name already exist.")
            return None
        return super(Student, cls).__new__(cls)

    def __init__(self, full_name, n_record_book, **grades):
        Student.all_names.append(full_name)
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
        self.__full_name = full_name

    @property
    def grades(self):
        return self.__grades

    @grades.setter
    def grades(self, grades):
        for value in grades.values():
            if not isinstance(value, (float, int)) or value <= 0:
                raise TypeError("Invalid value")
        self.__grades = grades

    def average_score(self):
        av_score = 0.0
        for mark in self.grades.values():
            av_score += mark
        av_score /= len(self.grades)
        return av_score


class Group:

    def __new__(cls, *students):
        if len(students) > 20:
            print("Instance wasn`t created. Max size of group is 20.")
            return None
        return super(Group, cls).__new__(cls)

    def __init__(self, *students):
        for student in students:
            if not isinstance(student, Student):
                raise TypeError("Invalid product")
        self.students = students

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

    Olya = Student("Olya Grishki", "34T435", math=5, PE=3.4)
    Dasha = Student("Dasha Bibko", "464g435", math=2, PE=5)
    Sasha = Student("Sasha Gog", "45GG435", math=4.8, PE=4.9)

    ti_02 = Group(Olya, Dasha, Sasha)
    ti_02.top_five()

    Olya2 = Student("Olya Grishki", "34T435", math=5, PE=3.4)
    Bib = Student("Zuchka", 4, b=2, PE=6, bab=1)
    ti_01 = Group(Bib)
    ti_01.top_five()
