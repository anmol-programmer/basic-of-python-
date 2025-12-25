class Person:
    def __init__(self, name, age, salary):
        self.name = name           # Public
        self._age = age            # Protected
        self.__salary = salary     # Private

    def show_info(self):
        print("Name (Public):", self.name)
        print("Age (Protected):", self._age)
        print("Salary (Private):", self.__salary)

class Employee(Person):
    def access_protected_and_private(self):
        print("Accessing Public name:", self.name)        
        print("Accessing Protected age:", self._age)      
        try:
            print("Accessing Private salary:", self.__salary) 
        except AttributeError:
            print("Cannot access __salary directly (Private)")
        # Accessing Private using name mangling (Not recommended)
        print("Accessing Private salary via name mangling:", self._Person__salary)

# Main Program
p = Person("satyam", 25, 50000)
print("[Accessing from Outside the Class]")
print("Public Name:", p.name)         
print("Protected Age:", p._age)      
try:
    print("Private Salary:", p.__salary)  
except AttributeError:
    print("Cannot access __salary directly (Private)")

# Access via name mangling
print("Private Salary via name mangling:", p._Person__salary)

# Show info using method
p.show_info()

# Access from subclass
e = Employee("anmol", 22, 60000)
e.access_protected_and_private()
