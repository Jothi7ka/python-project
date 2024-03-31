
import pygame as p
import time as t
import sys as s

print('HOSPITAL ADMIN LOGIN:')
hospital_admin_username = 'admin'
hospital_admin_password = 'admin123'


def hospital_admin_login():
    username = str(input("Enter the hospital username: "))
    password = str(input('Enter the hospital password: '))
    if username == hospital_admin_username and password == hospital_admin_password:
        print('Login Successfully, Welcome to Hospital Admin:')
    else:
        print('Login failed')
        s.exit()


hospital_admin_login()

blood_bank = {
    'A+': 800,
    'A-': 670,
    'B+': 470,
    'B-': 0,
    'O+': 760,
    'O-': 460,
    'AB+': 0,
    'AB-': 390
}


def hospital_needs_blood():
    print('HOSPITAL EMERGENCY NEED BLOOD REGISTRATION:')
    hospital_name = str(input("Enter the hospital name: "))
    blood_type = input("Enter the required blood type (A+, A-, B+, B-, O+, O-, AB+, AB-): ")

    if blood_type not in blood_bank:
        print("Invalid blood type entered.")
        return

    required_units = int(input("Enter the required units: "))

    if blood_bank[blood_type] >= required_units:
        print('Blood is available in the inventory:')
        t.sleep(2)

        img = p.image.load('C:\\Users\\admin\\PycharmProjects\\Blood Bank\\BBMSP\\blood_available.jpg')
        size = img.get_rect().size
        screen = p.display.set_mode(size)
        screen.blit(img, (0, 0))
        p.init()
        p.display.flip()
        t.sleep(10)
        p.quit()


    else:
        print("Blood is not available in the inventory.")


hospital_needs_blood()
