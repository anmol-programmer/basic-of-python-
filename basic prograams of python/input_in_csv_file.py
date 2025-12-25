import csv
n = int(input("How many students? "))
with open('students.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Roll No', 'Name', 'Marks'])
    for i in range(n):
        roll = input("Enter roll number: ")
        name = input("Enter name: ")
        marks = input("Enter marks: ")
        writer.writerow([roll, name, marks])
with open('students.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(', '.join(row))