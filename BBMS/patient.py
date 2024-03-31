import pygame as p
import time as t

print('PATIENT LOGIN:')

def patient_login():
    username = str(input('Enter The Username: '))
    password = str(input('Enter The Password: '))
    if username and password:
        print('LOGIN SUCCESSFULLY:')

patient_login()

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

patients = []  # Initialize an empty list for patients

def register_patient():
    print("Patient Registration:")
    patient_name = input("Enter Patient Name: ")
    patient_age = int(input("Enter Patient Age: "))
    while True:
        contact_number = input("Enter Contact Number (10 digits): ")

        if len(contact_number) != 10:
            print("Invalid contact number. Please enter a 10-digit number.")
        else:
            contact_number = int(contact_number)
            break

    print("Select Blood Group:")
    print("1. A+")
    print("2. A-")
    print("3. B+")
    print("4. B-")
    print("5. O+")
    print("6. O-")
    print("7. AB+")
    print("8. AB-")
    blood_group = input("Enter Blood Group: ")

    if blood_group == '1':
        blood_group = 'A+'
    elif blood_group == '2':
        blood_group = 'A-'
    elif blood_group == '3':
        blood_group = 'B+'
    elif blood_group == '4':
        blood_group = 'B-'
    elif blood_group == '5':
        blood_group = 'O+'
    elif blood_group == '6':
        blood_group = 'O-'
    elif blood_group == '7':
        blood_group = 'AB+'
    elif blood_group == '8':
        blood_group = 'AB-'
    else:
        print("Invalid Blood Group selection.")

    unit_ml = int(input("Enter Unit (ml) to Request: "))

    patient = {
        'Patient Name': patient_name,
        'Patient Age': patient_age,
        'Contact no': contact_number,
        'Blood Group': blood_group,
        'Unit (ml) Requested': unit_ml
    }

    patients.append(patient)
    print("Patient registered successfully!  ")

def make_blood_request():
    print("\nMake Blood Request:")

    blood_group = input("Enter Blood Group: ")
    unit_ml = int(input("Enter Unit (ml) to Request: "))
    disease = str(input("Enter Disease (if any):"))

    if blood_group in blood_bank and blood_bank[blood_group] >= unit_ml:
        print("Blood request successful! Your blood is available in the blood bank.")
        t.sleep(2)
        img = p.image.load('C:\\Users\\admin\\PycharmProjects\\Blood Bank\\BBMSP\\r2 blood.jpg')
        size = img.get_rect().size
        screen = p.display.set_mode(size)
        screen.blit(img, (0, 0))
        p.init()
        p.display.flip()
        t.sleep(5)
        p.quit()
    else:
        print("Blood request failed!  Your blood is not available in sufficient quantity.")


register_patient()
make_blood_request()
