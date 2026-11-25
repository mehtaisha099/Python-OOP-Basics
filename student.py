class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_average(self):
        return sum(self.marks) / len(self.marks)


student = Student("Isha", [80, 75, 90, 85, 70])

print("Student Name:", student.name)
print("Average Marks:", student.calculate_average())