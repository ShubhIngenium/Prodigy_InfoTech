# Contact Management System

A simple Python program to store, view, edit, and delete contact information.

## Features

- Add a new contact with name, phone number, and email
- View all saved contacts
- Edit an existing contact
- Delete a contact
- Stores contacts in `contacts.json` for persistence

## Usage

Run the program with:

```bash
python ContactManagementSystem.py
```

Then choose one of the menu options:

1. Add contact
2. View contacts
3. Edit contact
4. Delete contact
5. Exit

## Notes

- Contacts are saved to `contacts.json` in the same folder.
- If `contacts.json` does not exist, it is created automatically.
- Fields cannot be left empty when adding a contact.

## Example

```text
Contact Management System
1. Add contact
2. View contacts
3. Edit contact
4. Delete contact
5. Exit
Choose an option: 1

Add New Contact
Name: Jay
Phone: 112233445566
Email: jay@example.com
Contact 'Jay' added successfully.
```
