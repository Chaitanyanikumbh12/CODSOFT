# Contact Book Application

contacts = []

# Add Contact
def add_contact():
    print("\n--- Add Contact ---")
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    birth_date = input("Enter Birth Date: ")

    contact = {
        "Name": name,
        "Phone": phone,
        "Email": email,
        "Address": address,
        "Birth Date": birth_date
    }

    contacts.append(contact)
    print("\nContact added successfully!")

# View Contacts
def view_contacts():
    if not contacts:
        print("\nNo contacts found!")
        return

    print("\n========== Contact List ==========")
    for i, contact in enumerate(contacts, start=1):
        print(f"\nContact {i}")
        print(f"Name    : {contact['Name']}")
        print(f"Phone   : {contact['Phone']}")
        print(f"Email   : {contact['Email']}")
        print(f"Address : {contact['Address']}")
        print(f"Birth Date : {contact['Birth Date']}")

# Search Contact
def search_contact():
    if not contacts:
        print("\nNo contacts available.")
        return

    search = input("\nEnter Name or Phone Number: ").lower()

    found = False

    for contact in contacts:
        if search == contact["Name"].lower() or search == contact["Phone"]:
            print("\nContact Found")
            print(f"Name    : {contact['Name']}")
            print(f"Phone   : {contact['Phone']}")
            print(f"Email   : {contact['Email']}")
            print(f"Address : {contact['Address']}")
            print(f"Birth Date : {contact['Birth Date']}")
            found = True

    if not found:
        print("Contact not found!")

# Update Contact
def update_contact():
    phone = input("\nEnter Phone Number of Contact to Update: ")

    for contact in contacts:
        if contact["Phone"] == phone:
            print("\nLeave blank to keep old value.")

            new_name = input("New Name: ")
            new_phone = input("New Phone: ")
            new_email = input("New Email: ")
            new_address = input("New Address: ")
            new_birth_date = input("New Birth Date: ")

            if new_name:
                contact["Name"] = new_name
            if new_phone:
                contact["Phone"] = new_phone
            if new_email:
                contact["Email"] = new_email
            if new_address:
                contact["Address"] = new_address
            if new_birth_date:
                contact["Birth Date"] = new_birth_date

            print("\nContact updated successfully!")
            return

    print("Contact not found!")

# Delete Contact
def delete_contact():
    phone = input("\nEnter Phone Number of Contact to Delete: ")

    for contact in contacts:
        if contact["Phone"] == phone:
            contacts.remove(contact)
            print("\nContact deleted successfully!")
            return

    print("Contact not found!")

# Main Menu
while True:
    print("\n==============================")
    print("      CONTACT BOOK")
    print("==============================")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ")

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
        
        print("\nThank you for using Contact Book!")
        break

    else:
        print("\nInvalid choice! Please try again.")