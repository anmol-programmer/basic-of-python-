# Append to the file
with open('example.txt', 'a') as file:
    file.write(input("Enter some text to append to the file: ") + "\n")
    file.write("Additional text for demonstration purposes.\n")

# Read from the file to confirm appending
with open('example.txt', 'r') as file:
    content = file.read()
    print("Current content of the file:\n")
    print(content)
