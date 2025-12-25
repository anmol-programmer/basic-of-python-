# . Create a calculator using functions. 
# Function definitions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Taking inputs
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Select operation: +, -, *, /")
choice = input("Enter choice: ")

# Operation logic using if-elif-else
if choice == '+':
    print(f"{x} + {y} = {add(x, y)}")
elif choice == '-':
    print(f"{x} - {y} = {subtract(x, y)}")
elif choice == '*':
    print(f"{x} * {y} = {multiply(x, y)}")
elif choice == '/':
    print(f"{x} / {y} = {divide(x, y)}")
else:
    print("Invalid operation")
