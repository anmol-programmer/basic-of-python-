import csv  # Import the CSV module

# ---------- Step 1: Create and Write Data to CSV ----------
with open('students.csv', 'w', newline='') as file:  # Open file in write mode
    write = csv.writer(file)  # Create a CSV writer object

    # Writing the header row (column titles)
    write.writerow(['Roll No', 'Name', 'Marks'])

    # Writing some student records
    write.writerow([1 , 'Alice', 85])
    write.writerow([2 , 'Bob' , 78])
    write.writerow([3 , 'Charlie ', 92])

print("✅ Student records have been saved to 'students.csv'\n")

# ---------- Step 2: Read and Display the CSV ----------
print("📖 Reading student records from file:\n")

with open('students.csv', 'r') as file:  # Open file in read mode
    reader = csv.reader(file)  # Create a CSV reader object

    for row in reader:  # Loop through each row in the file
        print(', '.join(row))  # Print each row nicely
