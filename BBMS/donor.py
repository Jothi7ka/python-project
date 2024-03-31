print('DONOR LOGIN:')
def donor_login():
    username = str(input('Enter The Username:'))
    password = str(input('Enter The Password:'))
    if username and password:
        print('LOGIN SUCCESSFULLY:')
donor_login()
import pygame as p
import time as t
print('DONOR CHECK-UP:')
def is_hemoglobin_level_normal(hemoglobin_level):
    lower_range = 12
    upper_range = 18
    return lower_range <= hemoglobin_level <= upper_range
def donorcheck_up():
    while True:
        age = int(input("Enter Age:"))
        if 18 <= age <= 65:
            break
        else:
            print("Sorry, donors must be between 18 and 65 years old.")

    weight_kg = float(input("Enter Weight in kilograms: "))
    while weight_kg < 50:
        print("Sorry, donors must weigh at least 50 kilograms.")
        weight_kg = float(input("Enter Weight in kilograms: "))
        print("Hemoglobin Level Check:")
    hemoglobin_level = float(input("Enter Hemoglobin Level:"))

    if not is_hemoglobin_level_normal(hemoglobin_level):
        print("Hemoglobin level is outside the normal range.")
        return False

    print("Health Status Check:")

    general_health = input("Are you in good general health? (yes/no): ")
    if general_health!= 'yes':
        print("Sorry, donors should be in good general health.")
        return False

    infectious_diseases = input("Do you have any infectious diseases (HIV/AIDS, hepatitis, syphilis)? (yes/no): ")
    if infectious_diseases == 'yes':
        print("Sorry, donors should not have infectious diseases.")
        return False

    print("All checks passed. You are eligible to donate blood.")
    return True
donor_eligibility = donorcheck_up()
if donor_eligibility:
    t.sleep(2)
    img = p.image.load('C:\\Users\\admin\\PycharmProjects\\Blood Bank\\BBMSP\\donor register.png')
    size = img.get_rect().size
    screen = p.display.set_mode(size)
    screen.blit(img, (0, 0))
    p.init()
    p.display.flip()
    t.sleep(5)
    p.quit()

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
            first_name = input("Enter First Name: ")
            last_name = input("Enter Last Name: ")

            print("Select Blood Group:")
            print("1. A+")
            print("2. A-")
            print("3. B+")
            print("4. B-")
            print("5. O+")
            print("6. O-")
            print("7. AB+")
            print("8. AB-")

            blood_group_select = input("Enter the number to select the Blood Group: ")

            if blood_group_select == '1':
                blood_group = 'A+'
            elif blood_group_select == '2':
                blood_group = 'A-'
            elif blood_group_select == '3':
                blood_group = 'B+'
            elif blood_group_select == '4':
                blood_group = 'B-'
            elif blood_group_select == '5':
                blood_group = 'O+'
            elif blood_group_select == '6':
                blood_group = 'O-'
            elif blood_group_select == '7':
                blood_group = 'AB+'
            elif blood_group_select == '8':
                blood_group = 'AB-'
            else:
                print("Invalid Blood Group selection.")
                continue

            address = str(input("Enter Address: "))

            while True:
                contact_number = input("Enter Contact Number (10 digits): ")

                if len(contact_number) == 10:
                    break
                else:
                    print('Invalid contact number. Please enter a 10-digit number')

            unit_ml = int(input("Enter Unit (ml) to Donate: "))

            blood_bank[blood_group] += unit_ml
            print("Donation successful! Thank you For Donor:")

            t.sleep(2)

            img = p.image.load('C:\\Users\\admin\\PycharmProjects\\Blood Bank\\BBMSP\\blood donation.jpg')
            size = img.get_rect().size
            screen = p.display.set_mode(size)
            screen.blit(img, (0, 0))
            p.init()
            p.display.flip()
            t.sleep(10)
            p.quit()

            t.sleep(2)

            img = p.image.load('C:\\Users\\admin\\PycharmProjects\\Blood Bank\\BBMSP\\tq.png')
            size = img.get_rect().size
            screen = p.display.set_mode(size)
            screen.blit(img, (0, 0))
            p.init()
            p.display.flip()
            t.sleep(10)
            p.quit()

        elif choice == '2':
            print("Blood Bank Status:")
            for blood_type, units in blood_bank.items():
                print(blood_type + ':' + str(units) + ' units')

        elif choice == '3':
            print("Exiting the Blood Bank Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")
