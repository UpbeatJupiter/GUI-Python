class Person:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def full_name(self):
        return f"{self.first} {self.last}"

    @full_name.setter
    def full_name(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    def __str__(self):
        return self.full_name


class Student(Person):

    def __init__(self, first, last, gpa):
        super().__init__(first, last)
        self.gpa = gpa

    def __str__(self):
        return f"Student is {super().__str__()}.\n -- GPA: {self.gpa}"


stu1 = Student("Julia", "Smith", 3.6)
stu1.full_name = "New Person"

print(stu1)
