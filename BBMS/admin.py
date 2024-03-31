import sys as s
print('ADMIN LOGIN:')
admin_username='jothika'
admin_password='jothika15'
def admin_login():
    username=str(input("Enter the username:"))
    password=str(input('Enter the password:'))
    if username==admin_username and password==admin_password:
       print('Login Successfully,Welcome to Admin:')
    else:
        print('Login failed')
        s.exit()
admin_login()

blood = {
    'A+': 800,
    'A-': 670,
    'B+': 470,
    'B-': 0,
    'O+': 70,
    'O-': 60,
    'AB+': 0,
    'AB-': 90
}

print('Available Blood In The Blood Bank:')
for blood_type, units in blood.items():
    print(blood_type + ':' + str(units) + ' units')

blood_donors_details = [
    {'Name': 'Yasmin', 'Blood Group': 'A+', 'Contact No': '8935406248', 'Address': 'Salem', 'Email': 'yasmin@gmail.com'},
    {'Name': 'Nandhu', 'Blood Group': 'B+', 'Contact No': '9360646454', 'Address': 'Bangalore', 'Email': 'nandhini@gmail.com'},
    {'Name': 'Mohana', 'Blood Group': 'O+', 'Contact No': '6748293058', 'Address': 'Coimbatore', 'Email': 'mohana@gmail.com'},
    {'Name': 'paviii', 'Blood Group': 'AB+', 'Contact No': '6748293058', 'Address': 'Chennai', 'Email': 'pavithra@gmail.com'},
    {'Name': 'priyaa', 'Blood Group': 'A-', 'Contact No': '6748293058', 'Address': 'Erode', 'Email': 'priya@gmail.com'},
]

print('Available Blood Donors:')
for donor in blood_donors_details:
    print('Name: ' + donor['Name'] + ', Blood Group: ' + donor['Blood Group'] + ', Contact No: ' + donor['Contact No'] + ', Address: ' + donor['Address'] + ', Email: ' + donor['Email'])


patient_details = [
    {'Name': 'Indhu', 'Blood Group': 'AB+', 'Contact No': '8472390395', 'Address': 'Salem', 'Blood_unit':'400'},
    {'Name': 'Senika', 'Blood Group': 'B-', 'Contact No': '8940837283', 'Address': 'Bangalore', 'Blood_unit':'350'},
    {'Name': 'Mouni', 'Blood Group': 'O-', 'Contact No': '6748293058', 'Address': 'Coimbatore', 'Blood_unit':'450'},
    {'Name': 'Nooru', 'Blood Group': 'AB-', 'Contact No': '8593029292', 'Address': 'Chennai', 'Blood_unit':'350'},
    {'Name': 'Durga', 'Blood Group': 'A+', 'Contact No': '8795038273', 'Address': 'Erode', 'Blood_unit': '500'},
]

print('Patient Details:')

for patient in  patient_details:
    print('Name: ' + patient['Name'] + ', Blood Group: ' + patient['Blood Group'] + ', Contact No: ' + patient['Contact No'] + ', Address: ' + patient['Address'] + ', Blood_unit: ' + patient['Blood_unit'])



















