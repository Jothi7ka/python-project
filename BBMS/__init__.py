#from BBMSP import  welcome,admin,patient,donor,hospital,logout
blood_bank = {
    'A+': 800,
    'A-': 670,
    'B+': 470,
    'B-': 0,
    'O+': 70,
    'O-': 60,
    'AB+': 0,
    'AB-': 90
}

while True:
    print("Blood Bank Management System")
    print("1. Register Donor")
    print("2. Display Blood Bank Status")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        print("Donor Registration:")

        print("Select Blood Group:")
        print("1. A+")
        print("2. A-")
        print("3. B+")
        print("4. B-")
        print("5. O+")
        print("6. O-")
        print("7. AB+")
        print("8. AB-")
        blood_group_select = input("Enter the number to select the Blood: ")
        if blood_group_select in ['1', '2', '3', '4', '5', '6', '7', '8']:
            blood_group = {
                '1': 'A+',
                '2': 'A-',
                '3': 'B+',
                '4': 'B-',
                '5': 'O+',
                '6': 'O-',
                '7': 'AB+',
                '8': 'AB-'
            }[blood_group_select]
        else:
            print("Invalid Blood Group selection.")
            continue

        unit_ml = int(input("Enter Unit (ml) to Donate: "))

        blood_bank[blood_group] += unit_ml
        print("Donation successful! Thank you For Donor.")

    elif choice == '2':
        print("Blood Bank Status:")
        for blood_type, units in blood_bank.items():
            print(blood_type + ':' + str(units) + ' units')

    elif choice == '3':
        print("Exiting the Blood Bank Management System. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a valid option.")
