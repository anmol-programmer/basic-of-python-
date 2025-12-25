# . Create a class that keeps track of number of instances created.
class InstanceCounter:
    count = 0

    def __init__(self):
        InstanceCounter.count+= 1
i=InstanceCounter()
I2=InstanceCounter()
print(InstanceCounter.count)  # This will print the number of instances created, which is


   