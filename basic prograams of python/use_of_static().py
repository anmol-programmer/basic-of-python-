class Student:
    school_name = "Sunrise School"  # Class variable

    def __init__(self, name, grade):
        self.name = name            # Instance variable
        self.grade = grade

    # Instance Method
    def display_info(self):
        print(f"Student Name: {self.name}, Grade: {self.grade}")

    # Class Method
    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name
        print(f"School name changed to: {cls.school_name}")

    # Static Method
    @staticmethod
    def is_pass(mark):
        return mark >= 33

# Create object
s1 = Student("anmol", "10th")

# Call instance method
s1.display_info()  # Output: Student Name: Priya, Grade: 10th

# Call class method
Student.change_school("Green Valley School")  # Changes school_name for all students

# Call static method
print("Has passed?", Student.is_pass(45))  # Output: True
print("Has passed?", Student.is_pass(25))  # Output: False
