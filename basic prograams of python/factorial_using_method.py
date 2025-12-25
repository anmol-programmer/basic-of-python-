# find the factiorial of a number using a method
def factorial(n):
    count = 1
    for i in range(1, n + 1):
        count *= i
    return count

# Take user input
n = int(input("Enter a number: "))
print("The factorial of", n, "is", factorial(n))
