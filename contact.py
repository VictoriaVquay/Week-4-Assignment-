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