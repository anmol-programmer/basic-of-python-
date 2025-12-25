#. Create a class Car and subclass ElectricCar; demonstrate polymorphism. 
class Car:
    def start_engine(self):
        return "The car's engine starts."

    def stop_engine(self):
        return "The car's engine stops."
class ElectricCar(Car):
    def start_engine(self):
        return "The electric car's engine starts silently."

    def stop_engine(self):
        return "The electric car's engine stops silently."

car = Car()
electric_car = ElectricCar()
print(car.start_engine())          # Output: The car's engine starts.
print(car.stop_engine())           # Output: The car's engine stops.
print(electric_car.start_engine())  # Output: The electric car's engine starts silently.
print(electric_car.stop_engine())   # Output: The electric car's engine stops silently.

