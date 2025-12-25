# Find the type of user input (int, float, or string).
a = input("Enter a value: ")
print("The input is an", type(a), "type.")
b=float(input("Enter a number to convert to float: "))
print("Converted value:", b)
print("The converted value is of type", type(b))    
c=int(input("Enter a number to convert to int: "))
print("Converted value:", c)
print("The converted value is of type", type(c))
# This code takes user input and converts it to float and int, displaying the types.