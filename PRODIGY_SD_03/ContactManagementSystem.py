import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "contacts.json"


def load_contacts():
    if DATA_FILE.exists():
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError):
            return []
    return []


def save_contacts(contacts):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(contacts, file, indent=2)


def display_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. {contact['name']} | {contact['phone']} | {contact['email']}")


def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty. Please enter a value.")


def add_contact(contacts):
    print("\nAdd New Contact")
    name = get_non_empty_input("Name: ")
    phone = get_non_empty_input("Phone: ")
    email = get_non_empty_input("Email: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully.")


def edit_contact(contacts):
    if not contacts:
        print("No contacts available to edit.")
        return

    print("\nEdit Contact")
    display_contacts(contacts)

    try:
        selected = int(input("Enter the contact number to edit: ").strip())
        if selected < 1 or selected > len(contacts):
            raise ValueError
    except ValueError:
        print("Invalid selection. Please enter a valid contact number.")
        return

    contact = contacts[selected - 1]
    print("Press Enter to keep the current value.")
    name = input(f"Name [{contact['name']}]: ").strip() or contact['name']
    phone = input(f"Phone [{contact['phone']}]: ").strip() or contact['phone']
    email = input(f"Email [{contact['email']}]: ").strip() or contact['email']

    contact.update({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print(f"Contact '{name}' updated successfully.")


def delete_contact(contacts):
    if not contacts:
        print("No contacts available to delete.")
        return

    print("\nDelete Contact")
    display_contacts(contacts)

    try:
        selected = int(input("Enter the contact number to delete: ").strip())
        if selected < 1 or selected > len(contacts):
            raise ValueError
    except ValueError:
        print("Invalid selection. Please enter a valid contact number.")
        return

    removed = contacts.pop(selected - 1)
    save_contacts(contacts)
    print(f"Contact '{removed['name']}' deleted successfully.")


def main():
    contacts = load_contacts()

    while True:
        print("\nContact Management System")
        print("1. Add contact")
        print("2. View contacts")
        print("3. Edit contact")
        print("4. Delete contact")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            print("\nContact List")
            display_contacts(contacts)
        elif choice == "3":
            edit_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Please choose a valid option from 1 to 5.")


if __name__ == "__main__":
    main()
