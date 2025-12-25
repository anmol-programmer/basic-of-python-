# Save a note to the file
def save_note():
    note = input("Enter your note: ")                  # Take user input for the note
    with open("notes.txt", "a") as file:               # Open (or create) notes.txt in append mode
        file.write(note + "\n")                         # Write the note followed by a newline
    print("Note saved successfully!")                   # Confirmation message

# Read all notes from the file
def read_notes():
    print("\nYour Notes:")
    
    with open("notes.txt", "r") as file:            # Try to open the file in read mode
            for line in file:                           # Loop through each line (note) in the file
                print("-", line)                # Print the note with a bullet, strip removes \n
                        

# Main menu
print("1. Save Note")                                   # Show menu option 1
print("2. Read Notes")
print("3. exit")                                  # Show menu option 2

while True:           # Take input from user for choice
    choice = input("Enter your choice (1/2/3): ")  
    if choice == "1":
        save_note()                                         # Call save_note function
    elif choice == "2":
        read_notes()                                      # Call read_notes function
    elif choice == "3":
        print("Exiting the program...")  
        break                 # Show exit message
    else:
        print("Invalid choice")                            # Show message for invalid input

                                    