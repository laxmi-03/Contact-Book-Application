def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")

    contact = {"name": name, "phone": phone, "email": email}

    contacts.append(contact)
    print("Contact added successfully!")


def edit_contact(contacts):
    name = input("Enter name of the contact to edit: ")
    found = False

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print("Select the field to edit:")
            print("1. Name")
            print("2. Phone number")
            print("3. Email")
            choice = input("Enter your choice (1-3):")

            if choice == "1":
                new_name = input("Enter new name: ")
                contact["name"] = new_name
            elif choice == "2":
                new_phone = input("Enter new phone number: ")
                contact["phone"] = new_phone
            elif choice == "3":
                new_email = input("Enter new email address: ")
                contact["email"] = new_email
            else:
                print("Invalid choice.")
                return

            print("Contact edited sucessfully!")
            found = True
            break

        if not found:
            print("Contact not found.")


def search_contacts(contacts):
    query = input("Enter search query: ")
    found_contacts = []

    for contact in contacts:
        if (
            query.lower() in contact["name"].lower()
            or query.lower() in contact["phone"].lower()
            or query.lower() in contact["email"].lower()
        ):
            found_contacts.append(contact)

    if found_contacts:
        print("Search results:")
        display_contacts(found_contacts)
    else:
        print("No contact found.")


def remove_contacts(contacts):
    name = input("Enter name of the contact to remove: ")
    found = False

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            print("Contact removed sussesfully!")
            found = True
            break

    if not found:
        print("Contact not found.")


def display_contacts(contacts):
    for contact in contacts:
        print("Name:", contact["name"])
        print("Phone:", contact["phone"])
        print("Email:", contact["email"])
        print()


def list_all_contacts(contacts):
    if contacts:
        print("All contacts:")
        display_contacts(contacts)
    else:
        print("No contact found.")


def manage_contacts():
    contacts = [
        {"name": "laxmi", "phone": "9355472350", "email": "laxmi@gmail.com"},
        {"name": "Anuj", "phone": "9818781308", "email": "anuj02@gmail.com"},
    ]

    while True:
        print("1. Add contact")
        print("2. Edit contact")
        print("3. Search contact")
        print("4. Remove contact")
        print("5. List all contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            edit_contact(contacts)
        elif choice == "3":
            search_contacts(contacts)
        elif choice == "4":
            remove_contacts(contacts)
        elif choice == "5":
            list_all_contacts(contacts)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid chouce. Try again.")


# Start the contact management system
manage_contacts()


