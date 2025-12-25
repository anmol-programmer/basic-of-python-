# Write a program to check if a list is palindrome. 
n=int(input("Enter the number of elements in the list: "))
list=[]
list2=[]
for i in range(n):
    list.append(int(input("Enter element")))
print("The list is:", list)
# Check if the list is a palindrome
for item in list:
    list2.append(item)
list2.reverse()
if list == list2:
    print("The list is a palindrome.")
else:
    # The line `print("The list is not a palindrome.")` is printing a message to the console
    # indicating that the input list is not a palindrome. This message is displayed when the condition
    # `if list == list2` evaluates to `False`, meaning that the original list and the reversed list
    # are not the same, indicating that the input list is not a palindrome.
    print("The list is not a palindrome.")

