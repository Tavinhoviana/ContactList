def add_new_contact(contacts, contact_name, new_phone, new_email):
    contact = {
        "contact": contact_name,
        "phone": new_phone,
        "email": new_email,
        "added": False
    }
    contacts.append(contact)
    print(f"Contact {contact_name} was successfully added!")

def view_contacts(contacts):
    if not contacts:
        print("\nThe contact list is empty.")
        return
    
    print("\nContact list:")
    for index, contact in enumerate(contacts, start=1):
        status = "✓" if contact["added"] else " "
        name = contact["contact"]
        phone = contact["phone"]
        email = contact["email"]
        print(f"{index}. [{status}] {name}, {phone}, {email}")
        
def update_contact(contacts, contact_index, new_name, new_phone, new_email):
    adjusted_contact_index = int(contact_index) - 1
    if 0 <= adjusted_contact_index < len(contacts):
        contacts[adjusted_contact_index]["contact"] = new_name
        contacts[adjusted_contact_index]["phone"] = new_phone
        contacts[adjusted_contact_index]["email"] = new_email
        print(f"Contact {contact_index} updated to {new_name}.")
    else:
        print("Invalid contact index.")

def favorite_contact(contacts, contact_index):
    adjusted_contact_index = int(contact_index) - 1
    if 0 <= adjusted_contact_index < len(contacts):
        contacts[adjusted_contact_index]["added"] = True
        print(f"Contact {contact_index} marked as favorite.")
    else:
        print("Invalid index.")

def unfavorite_contact(contacts, contact_index):
    for contact in contacts:
        if contact.get("contact") == contact_index and contact["added"]:
            contact["added"] = False
            print(f"The contact '{contact_index}' was unfavorited.")   
    print(f"Contact '{contact_index}' not found or was already not favorited.")
    return

def view_favorites(contacts):
    favorites = [c for c in contacts if c["added"]]
    if not favorites:
        print("\nNo favorite contacts.")
        return
    
    print("\nFavorite contacts list:")
    for index, contact in enumerate(favorites, start=1):
        name = contact["contact"]
        phone = contact["phone"]
        email = contact["email"]
        print(f"{index}. {name}, {phone}, {email}")

def delete_contact(contacts, contact_index):
    adjusted_contact_index = int(contact_index) - 1
    if 0 <= adjusted_contact_index < len(contacts):
        removed_contact = contacts.pop(adjusted_contact_index)
        print(f"Contact {removed_contact['contact']} was removed.")
    else:
        print("Invalid contact index.")

# List of contacts
contacts = []

while True:
    print("\nContact list:")
    print("1. Add new contact")
    print("2. View contacts")
    print("3. Edit contact")
    print("4. Mark contact as favorite")
    print("5. Unmark as favorite")
    print("6. View only favorite contacts")
    print("7. Delete contact")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        contact_name = input("Enter the name: ")
        new_phone = input("Enter the phone number: ")
        new_email = input("Enter the email: ")
        add_new_contact(contacts, contact_name, new_phone, new_email)

    elif choice == "2":
        view_contacts(contacts)

    elif choice == "3":
        view_contacts(contacts)
        contact_index = input("Enter the number of the contact you want to update: ")
        new_name = input("Enter the new name of the contact: ")
        new_phone = input("Enter the new phone number of the contact: ")
        new_email = input("Enter the new email of the contact: ")
        update_contact(contacts, contact_index, new_name, new_phone, new_email)

    elif choice == "4":
        view_contacts(contacts)
        contact_index = input("Enter the number of the contact you want to favorite: ")
        favorite_contact(contacts, contact_index)

    elif choice == "5":
        contact_index = input("Enter the name of the contact you want to unfavorite: ")
        unfavorite_contact(contacts, contact_index)

    elif choice == "6":
        view_favorites(contacts)

    elif choice == "7":
        view_contacts(contacts)
        contact_index = input("Enter the number of the contact you want to delete: ")
        delete_contact(contacts, contact_index)

    elif choice == "8":
        print("Program ended.")
        break

    else:
        print("Invalid option. Please try again.")
