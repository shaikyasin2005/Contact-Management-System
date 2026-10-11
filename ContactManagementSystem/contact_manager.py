import json
import re
from pathlib import Path

FILE = Path("contacts.json")


def load_contacts():
    """Load contacts from the JSON file."""
    if not FILE.exists():
        return {}

    try:
        with FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, dict) else {}
    except (json.JSONDecodeError, OSError):
        print("Warning: Could not read contacts.json.")
        return {}


contacts = load_contacts()


def save_contacts():
    """Save all contacts to the JSON file."""
    try:
        with FILE.open("w", encoding="utf-8") as file:
            json.dump(contacts, file, indent=4)
        return True
    except OSError as error:
        print("Error saving contacts:", error)
        return False


def get_phone():
    while True:
        phone = input("Enter phone number: ").strip()

        # Allow an optional leading + and 7–15 digits.
        if re.fullmatch(r"\+?[0-9]{7,15}", phone):
            return phone

        print("Enter 7–15 digits, with an optional leading +.")


def get_email():
    while True:
        email = input("Enter email: ").strip()

        if re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
            return email

        print("Please enter a valid email address.")


def add_contact():
    name = input("Enter name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    phone = get_phone()

    if phone in contacts:
        print("A contact with this phone number already exists.")
        return

    email = get_email()
    address = input("Enter address: ").strip()

    contacts[phone] = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    if save_contacts():
        print("Contact added successfully.")
    else:
        contacts.pop(phone, None)
        print("Contact was not saved.")


def view_contacts():
    if not contacts:
        print("No contacts found.")
        return

    print("\n--- All Contacts ---")

    for phone, contact in sorted(
        contacts.items(),
        key=lambda item: item[1]["name"].casefold()
    ):
        print(f"\nName: {contact['name']}")
        print(f"Phone: {phone}")
        print(f"Email: {contact['email']}")
        print(f"Address: {contact['address']}")


def search_contact():
    query = input("Enter name or phone to search: ").strip().casefold()

    if not query:
        print("Search cannot be empty.")
        return

    results = [
        contact for contact in contacts.values()
        if query in contact["name"].casefold()
        or query in contact["phone"].casefold()
    ]

    if not results:
        print("No matching contacts found.")
        return

    for contact in results:
        print(
            f"\nName: {contact['name']}\n"
            f"Phone: {contact['phone']}\n"
            f"Email: {contact['email']}\n"
            f"Address: {contact['address']}"
        )


def update_contact():
    phone = input("Enter the phone number of the contact: ").strip()

    if phone not in contacts:
        print("Contact not found.")
        return

    contact = contacts[phone]

    print("Press Enter to keep the existing value.")

    name = input(f"Name [{contact['name']}]: ").strip()
    email = input(f"Email [{contact['email']}]: ").strip()
    address = input(f"Address [{contact['address']}]: ").strip()

    if email and not re.fullmatch(
        r"[^@\s]+@[^@\s]+\.[^@\s]+", email
    ):
        print("Invalid email address. Update cancelled.")
        return

    updated = contact.copy()

    if name:
        updated["name"] = name
    if email:
        updated["email"] = email
    if address:
        updated["address"] = address

    contacts[phone] = updated

    if save_contacts():
        print("Contact updated successfully.")
    else:
        contacts[phone] = contact
        print("Update was not saved.")


def delete_contact():
    phone = input("Enter the phone number to delete: ").strip()

    if phone not in contacts:
        print("Contact not found.")
        return

    contact = contacts[phone]
    confirm = input(
        f"Delete {contact['name']}? (yes/no): "
    ).strip().casefold()

    if confirm != "yes":
        print("Deletion cancelled.")
        return

    del contacts[phone]

    if save_contacts():
        print("Contact deleted successfully.")
    else:
        contacts[phone] = contact
        print("Deletion was not saved.")


def main():
    while True:
        print("\n===== CONTACT MANAGEMENT SYSTEM =====")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Thank you for using Contact Manager!")
            break
        else:
            print("Invalid choice. Please select 1–6.")


if __name__ == "__main__":
    main()