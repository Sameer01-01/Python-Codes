contacts = {}

def display_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        for name, phone in contacts.items():
            print(f"Name: {name}, Phone: {phone}")

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    contacts[name] = phone
    print("Contact added successfully.")

def remove_contact():
    name = input("Enter name of the contact to remove: ")
    if name in contacts:
        del contacts[name]
        print("Contact removed successfully.")
    else:
        print("Contact not found.")

def main():
    while True:
        print("\n1. Add Contact")
        print("2. View Contacts")
        print("3. Remove Contact")
        print("4. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            display_contacts()
        elif choice == '3':
            remove_contact()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

main()
