class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):  # Overriding the parent class method
        print("Dog barks")

# Create objects
a = Animal()
d = Dog()

# Call speak() method
a.speak()  # Calls Animal's method
d.speak()  # Calls Dog's overridden method
