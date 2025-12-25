#Create a calculator that can add, subtract, multiply, and divide two numbers. 
a=float(input("Enter first number: "))
b=float(input("Enter second number: "))

def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    if b == 0:
        return "Error! Division by zero."
    return a / b
operator = input("Enter operator (+, -, *, /): ")
if operator == '+':
    print("Result:", add(a, b))
elif operator == '-':
    print("Result:", subtract(a, b))
elif operator == '*':
    print("Result:", multiply(a, b))
elif operator == '/':   
    print("Result:", divide(a, b))
else:
    print("Invalid operator! Please use +, -, *, or /.")    
# This code snippet is a simple calculator that performs basic arithmetic operations
# such as addition, subtraction, multiplication, and division on two user-provided numbers.