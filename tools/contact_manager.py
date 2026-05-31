#!/usr/bin/env python3
import json
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w', encoding='utf-8') as f:
        json.dump(contacts, f, indent=2)

def add_contact(contacts):
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    return contacts

def list_contacts(contacts):
    print("\nContacts:")
    for i, c in enumerate(contacts, 1):
        print(f"{i}. {c['name']} - {c.get('phone', 'N/A')} - {c.get('email', 'N/A')}")

def main():
    print("=" * 50)
    print("    CONTACT MANAGER")
    print("=" * 50)
    
    contacts = load_contacts()
    
    while True:
        print("\n1. Add contact")
        print("2. List contacts")
        print("3. Delete contact")
        print("0. Exit")
        
        choice = input("\nSelect: ")
        
        if choice == "1":
            contacts = add_contact(contacts)
            save_contacts(contacts)
            print("Added!")
        elif choice == "2":
            list_contacts(contacts)
        elif choice == "3":
            try:
                idx = int(input("Contact number: ")) - 1
                if 0 <= idx < len(contacts):
                    contacts.pop(idx)
                    save_contacts(contacts)
                    print("Deleted!")
            except ValueError:
                print("Invalid number!")
        elif choice == "0":
            break
    
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()