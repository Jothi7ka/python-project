import pygame as p
import time as t
import sys
p.init()
width = 1000
height = 700
a = p.display.set_mode((width, height))
p.display.set_caption(' BLOOD BANK MANAGEMENT SYSTEM')
font = p.font.SysFont('Algerian', 30)
text1 = 'WELCOME TO BLOOD BANK MANAGEMENT SYSTEM!'
text2 = 'AVAILABLE FEATURES: ADMIN LOGIN, PATIENT LOGIN, DONOR LOGIN'
textsurface1 = font.render(text1, True, (255,0,0))
textsurface2 = font.render(text2, True, (255,0,0))
start_time = t.time()
while True:
    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit()
            sys.exit()
    elapsed_time = t.time() - start_time
    if elapsed_time < 5:
        a.fill((255, 255, 255))
        a.blit(textsurface1, (width//2 - textsurface1.get_width()//2, height//2 - textsurface1.get_height()//2))
        a.blit(textsurface2, (width//1.8 - textsurface2.get_width()//1.8, height//1.8 - textsurface2.get_height()//1.8))
        p.display.flip()
    else:
        break
t.sleep(5)
# image display in pygame  window
import pygame as p
import time as t

img=p.image.load('C:\\Users\\admin\\PycharmProjects\\Blood Bank\\BBMSP\\Blood.png')
p.display.set_caption(' BLOOD BANK MANAGEMENT SYSTEM')
size=img.get_rect().size
screen=p.display.set_mode(size)
screen.blit(img,(0,0))
p.init()
p.display.flip()
t.sleep(5)
p.quit()

'''def M  ain_menu():
    print('1.admin'
          '\n2.patient'
          '\n3.hospital'
          '\n4.donor'
          '\n5.logout')

    ch = int(input('Enter your choice:'))
    i = 1
    while (i <= 3):
        if ch == 1:
            import admin
        elif ch == 2:
            import patient
        elif ch == 3:
            import hospital
        elif ch == 4:
            import donor
        elif ch == 5:
            import logout

            break
        else:
            print('Please enter the correct choice')
        i += 1


Main_menu()'''