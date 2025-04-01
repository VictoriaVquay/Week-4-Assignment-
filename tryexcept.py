#try:
    # Attempt to open a file that doesn't exist
   # with open('example.txt', 'r') as file:
       # data = file.read()   
       # print(data)
#except FileNotFoundError:   
    # Handle the error if the file is not found
    #print("File not found. Please check the filename.") 

import os

# File name where contacts are stored
CONTACTS_FILE = "contacts.txt"

def add_contact():
    """Add a new contact to the file."""
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone Number: ").strip()

    # Validate phone number
    if not phone.isdigit():
        print("❌ Invalid phone number! Please enter digits only.")
        return

    with open(CONTACTS_FILE, "a") as file:
        file.write(f"{name}, {phone}\n")
    
    print("✅ Contact added successfully!")

def view_contacts():
    """Display all contacts."""
    try:
        with open(CONTACTS_FILE, "r") as file:
            contacts = file.readlines()
            if not contacts:
                print("📭 No contacts found.")
                return
            print("\n📞 Contact List:")
            for contact in contacts:
                print(contact.strip())
    except FileNotFoundError:
        print("❌ No contacts found. Add some first!")

def search_contact():
    """Search for a contact by name."""
    name = input("Enter Name to Search: ").strip().lower()
    try:
        with open(CONTACTS_FILE, "r") as file:
            contacts = file.readlines()
            found = False
            for contact in contacts:
                if name in contact.lower():
                    print("🔍 Found:", contact.strip())
                    found = True
            if not found:
                print("❌ Contact not found!")
    except FileNotFoundError:
        print("❌ No contacts found. Add some first!")

def main():
    """Main menu for the contact manager."""
    while True:
        print("\n📇 Contact Manager")
        print("1️⃣ Add Contact")
        print("2️⃣ View Contacts")
        print("3️⃣ Search Contact")
        print("4️⃣ Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again!")

if __name__ == "__main__":
    main()