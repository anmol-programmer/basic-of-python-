# Write to the file
with open('example.txt', 'w') as file:
    file.write(input("Enter some text to write to the file: ") + "\n")
    file.write("It contains some text for demonstration purposes.\n")

# Read from the file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
