import datetime

# Blood Bank System Data Storage
donors = []

# Add a new donor to the system
def add_donor():
    print("\n--- Add New Donor ---")
    name = input("Enter donor name: ")
    age = int(input("Enter donor age: "))
    blood_group = input("Enter donor blood group: ").upper()
    contact = input("Enter donor contact number: ")
    
    donor = {
        "name": name,
        "age": age,
        "blood_group": blood_group,
        "contact": contact,
        "donation_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    donors.append(donor)
    print(f"\nDonor {name} added successfully!\n")

# Search for donors by blood group
def search_donor():
    print("\n--- Search Donors ---")
    blood_group = input("Enter blood group to search for: ").upper()
    
    matches = [donor for donor in donors if donor["blood_group"] == blood_group]
    
    if matches:
        print(f"\nDonors with blood group {blood_group}:\n")
        for idx, donor in enumerate(matches, start=1):
            print(f"{idx}. Name: {donor['name']}, Age: {donor['age']}, Contact: {donor['contact']}, Donation Date: {donor['donation_date']}")
    else:
        print(f"\nNo donors found with blood group {blood_group}.\n")

# Display all donors
def display_donors():
    print("\n--- All Donors ---")
    if donors:
        for idx, donor in enumerate(donors, start=1):
            print(f"{idx}. Name: {donor['name']}, Age: {donor['age']}, Blood Group: {donor['blood_group']}, Contact: {donor['contact']}, Donation Date: {donor['donation_date']}")
    else:
        print("\nNo donors available in the system.\n")

# Main menu
def main():
    while True:
        print("\n--- Blood Bank Management System ---")
        print("1. Add Donor")
        print("2. Search Donor by Blood Group")
        print("3. Display All Donors")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_donor()
        elif choice == "2":
            search_donor()
        elif choice == "3":
            display_donors()
        elif choice == "4":
            print("\nThank you for using the Blood Bank Management System. Goodbye!\n")
            break
        else:
            print("\nInvalid choice! Please try again.\n")

# Run the Blood Bank Management System
if __name__ == "__main__":
    main()

