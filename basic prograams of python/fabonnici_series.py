# print the fibonacci series   
num= int (input("Enter the number of terms in the Fibonacci series: "))
a=0
b=1
print("Fibonacci series:")
for i in range(num):
    print(a, end=' ')
    c = a + b
    a = b
    b = c
