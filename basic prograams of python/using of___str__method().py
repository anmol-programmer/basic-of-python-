class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

# Creating object
p = Person("satyam", 22)

# Print object
print(p)  # Automatically calls p.__str__()
