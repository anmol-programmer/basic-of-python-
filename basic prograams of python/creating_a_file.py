with open('example.txt', 'w') as file:
    file.write(input("Enter some text to write to the file: ") + "\n")
    file.write("It contains some text for demonstration purposes.\n")