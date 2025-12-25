#  Create a class Student with attributes like name and marks. 
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")
student1 = Student("satyam", 85)
student2 = Student("Anmol", 90)
student1.display()