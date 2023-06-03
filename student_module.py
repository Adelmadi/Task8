class Student:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
        self.marks = []

    def add_mark(self, mark):
        self.marks.append(mark)

    def get_all_marks(self):
        return self.marks

    def calc_average(self):
        if len(self.marks) == 0:
            return 0
        return sum(self.marks) / len(self.marks)


student1 = Student("Adel", 22, "Rafah")
student1.add_mark(80)
student1.add_mark(85)
student1.add_mark(90)

print( f"Student Name: {student1.name}" )
print(f"Student Age: {student1.age}" )
print(f"Student City: {student1.city}")
print(f"Student Marks: {student1.get_all_marks()}")
print(f"Student Average Mark: {student1.calc_average()}")
