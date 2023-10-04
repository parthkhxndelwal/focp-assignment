import json

# Function to load contacts from a JSON file
def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = []
    return contacts

# Function to save contacts to a JSON file
def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)

# Function to add a new contact
def add_contact(contacts):
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added successfully.")

# Function to view all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        print("Contacts:")
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

# Function to update a contact
def update_contact(contacts):
    view_contacts(contacts)
    try:
        idx = int(input("Enter the number of the contact to update: ")) - 1
        if 0 <= idx < len(contacts):
            contact = contacts[idx]
            name = input(f"Enter the new name for {contact['name']}: ")
            phone = input(f"Enter the new phone number for {contact['name']}: ")
            email = input(f"Enter the new email address for {contact['name']}: ")

            contact["name"] = name
            contact["phone"] = phone
            contact["email"] = email

            save_contacts(contacts)
            print("Contact updated successfully.")
        else:
            print("Invalid contact number. Please enter a valid number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Function to delete a contact
def delete_contact(contacts):
    view_contacts(contacts)
    try:
        idx = int(input("Enter the number of the contact to delete: ")) - 1
        if 0 <= idx < len(contacts):
            deleted_contact = contacts.pop(idx)
            save_contacts(contacts)
            print(f"Contact '{deleted_contact['name']}' deleted successfully.")
        else:
            print("Invalid contact number. Please enter a valid number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Main function to interact with the user
def main():
    contacts = load_contacts()

    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Quit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            update_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Exiting the Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option (1/2/3/4/5).")

if __name__ == "__main__":
    main()