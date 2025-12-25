#. Create a contact book using a dictionary. 
# Contact Book using Dictionary
contact_book = {}

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    contact_book[name] = phone
    print("Contact added successfully!")

def search_contact():
    name = input("Enter name to search: ")
    if name in contact_book:
        print(f"Name: {name}, Phone: {contact_book[name]}")
    else:
        print("Contact not found.")

def display_contacts():
    if not contact_book:
        print("Contact book is empty.")
    else:
        print("\nAll Contacts:")
        for name, phone in contact_book.items():
            print(f"Name: {name}, Phone: {phone}")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contact_book:
        del contact_book[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

# Main menu
while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Display All Contacts")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        search_contact()
    elif choice == '3':
        display_contacts()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
