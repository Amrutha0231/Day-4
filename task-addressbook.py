import os

def add_contact(contacts):
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    contacts.append({"Name": name, "Phone": phone, "Email": email})
    print(f"Contact '{name}' added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        print("Contacts:")
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. Name: {contact['Name']}, Phone: {contact['Phone']}, Email: {contact['Email']}")

def search_contact(contacts, name):
    found_contacts = [contact for contact in contacts if name.lower() in contact['Name'].lower()]
    if not found_contacts:
        print(f"No contacts found with the name '{name}'.")
    else:
        print(f"Contacts with the name '{name}':")
        for index, contact in enumerate(found_contacts, start=1):
            print(f"{index}. Name: {contact['Name']}, Phone: {contact['Phone']}, Email: {contact['Email']}")

def save_contacts(contacts, filename):
    with open(filename, 'w') as file:
        for contact in contacts:
            file.write(f"{contact['Name']},{contact['Phone']},{contact['Email']}\n")
    print("Contacts saved successfully!")

def load_contacts(filename):
    contacts = []
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            for line in file:
                name, phone, email = line.strip().split(',')
                contacts.append({"Name": name, "Phone": phone, "Email": email})
    return contacts

def main():
    contacts = []
    filename = "contacts.txt"

    while True:
        print("\nChoose an action:")
        print("1 - Add contact")
        print("2 - View contacts")
        print("3 - Search contacts")
        print("4 - Save contacts")
        print("5 - Load contacts")
        print("6 - Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            name = input("Enter the name to search: ")
            search_contact(contacts, name)
        elif choice == '4':
            save_contacts(contacts, filename)
        elif choice == '5':
            contacts = load_contacts(filename)
            print("Contacts loaded successfully!")
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
