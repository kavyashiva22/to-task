class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}\nAddress: {self.address}\n"


class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        contact = Contact(name, phone, email, address)
        self.contacts.append(contact)
        print("Contact added successfully!\n")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return
        for index, contact in enumerate(self.contacts, start=1):
            print(f"{index}. {contact.name} - {contact.phone}")

    def search_contact(self, search_term):
        results = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]
        if not results:
            print("No contacts found.")
            return
        for contact in results:
            print(contact)
    
    def update_contact(self, search_term):
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                print("Contact found:")
                print(contact)
                contact.name = input("Enter new name (leave blank to keep current): ") or contact.name
                contact.phone = input("Enter new phone number (leave blank to keep current): ") or contact.phone
                contact.email = input("Enter new email (leave blank to keep current): ") or contact.email
                contact.address = input("Enter new address (leave blank to keep current): ") or contact.address
                print("Contact updated successfully!\n")
                return
        print("No contacts found.")

    def delete_contact(self, search_term):
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                self.contacts.remove(contact)
                print("Contact deleted successfully!\n")
                return
        print("No contacts found.")


def main():
    manager = ContactManager()
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            manager.add_contact(name, phone, email, address)
        elif choice == "2":
            manager.view_contacts()
        elif choice == "3":
            search_term = input("Enter name or phone number to search: ")
            manager.search_contact(search_term)
        elif choice == "4":
            search_term = input("Enter name or phone number of contact to update: ")
            manager.update_contact(search_term)
        elif choice == "5":
            search_term = input("Enter name or phone number of contact to delete: ")
            manager.delete_contact(search_term)
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
