class Person:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def full_name(self):
        return f"{self.first} {self.last}"

    def __str__(self):
        return self.full_name()


per1 = Person("James", "White")
print(per1.last)
print(per1.full_name())
per1.last = "Green"
print(per1)
