n=int(input("enter a number to find the sum of digits:"))
number=0
digit=0
while n>0:
    digit = n % 10
    number=digit+number
    n = n // 10
# The line `print("The sum of digits is:", number)` is displaying the message "The sum of digits is:"
# followed by the value stored in the variable `number`. This line is outputting the sum of the digits
# of the number entered by the user.
print("The sum of digits is:", number)