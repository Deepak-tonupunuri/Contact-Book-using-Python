#Contact Book
class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email):
        if name in self.contacts:
            print(f"Contact with name {name} already exists.")
        else:
            self.contacts[name] = {"phone": phone, "email": email}
            print(f"Contact {name} added successfully.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} deleted successfully.")
        else:
            print(f"Contact with name {name} does not exist.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for name, details in self.contacts.items():
                print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")

    def search_contact(self, name):
        if name in self.contacts:
            details = self.contacts[name]
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")
        else:
            print(f"Contact with name {name} not found.")

    def update_contact(self, name, phone=None, email=None):
        if name in self.contacts:
            if phone:
                self.contacts[name]['phone'] = phone
            if email:
                self.contacts[name]['email'] = email
            print(f"Contact {name} updated successfully.")
        else:
            print(f"Contact with name {name} does not exist.")

def main():
    book = ContactBook()
    
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. View Contacts")
        print("4. Search Contact")
        print("5. Update Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            book.add_contact(name, phone, email)
        elif choice == '2':
            name = input("Enter name to delete: ")
            book.delete_contact(name)
        elif choice == '3':
            book.view_contacts()
        elif choice == '4':
            name = input("Enter name to search: ")
            book.search_contact(name)
        elif choice == '5':
            name = input("Enter name to update: ")
            phone = input("Enter new phone number (leave blank if no change): ")
            email = input("Enter new email (leave blank if no change): ")
            book.update_contact(name, phone if phone else None, email if email else None)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
