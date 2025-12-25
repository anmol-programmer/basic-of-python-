n=int(input("enter the number of row in the pattern: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*",  end="")
    print()