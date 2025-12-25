class parent:
    """A simple parent class."""

    def display(self):
        print("This is the parent class.")
class child(parent):
    """A child class that inherits from parent."""

    def output(self):
        print("This is the child class.")
c=child()
c.display()  # This will call the display method from the child class.  
c.output()   # This will call the output method from the child class.