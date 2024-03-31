import sys as s
import pygame as p
import time as t

print('"*        BLOOD BANK AWARENESS !:        *"')
print("Donate blood, save lives! 💉❤️")
print("One blood donation can make a difference.")
print("Be a hero, donate blood today!")

t.sleep(5)
img=p.image.load('C:\\Users\\admin\\PycharmProjects\\Blood Bank Management\\BBMS\\tq2.webp')
p.display.set_caption(' BLOOD BANK MANAGEMENT SYSTEM')
size=img.get_rect().size
screen=p.display.set_mode(size)
screen.blit(img,(0,0))
p.init()
p.display.flip()
t.sleep(5)
p.quit()
print('ADMIN LOGOUT:')

admin_username='jothika'
admin_password='jothika15'
def admin_logout():
    username=str(input("Enter the username:"))
    password=str(input('Enter the password:'))
    if username==admin_username and password==admin_password:
       print('LOGOUT THE PAGE:')
       s.exit()
admin_logout()
