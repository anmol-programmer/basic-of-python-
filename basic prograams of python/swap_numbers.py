# Write a program that swaps two numbers without using a third variable.
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
a = a + b
b = a - b
a = a - b
print("After swapping:")
print("First number:", a)
print("Second number:", b)
# This code snippet is intended to swap two numbers entered by the user.            `