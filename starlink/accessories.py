
from tkinter import *
from PIL import Image, ImageTk
import webbrowser

f = Tk()

f.wm_state('zoomed')
f.title('STARLINK')
f.config(bg='black')


iconimg = Image.open('C:\\Users\\admin\\PycharmProjects\\mainProject1\\jo\\starlink logo (2).jpg')
tkicon = ImageTk.PhotoImage(iconimg)
f.iconphoto(False, tkicon)




imgpath_home = 'C:\\Users\\admin\\PycharmProjects\\mainProject1\\jo\\starlink logo (2).jpg'
img_home = Image.open(imgpath_home)
img_home = img_home.resize((120, 120))
tk_img_home = ImageTk.PhotoImage(img_home)
img_label_home = Label(f, image=tk_img_home, bg='black')
img_label_home.image = tk_img_home
img_label_home.place(x=0, y=0)



text2 = Label(f, text=" STARLINK  ACCESSORIES & MOUNTS", font=('Algerian', 30), fg='white', bg='black')
text2.place(x=300, y=10)

text4 = Label(f, text=" Available in the Starlink Shop after you purchase", font=('TimesNewRoman', 15), fg='white', bg='black')
text4.place(x=400, y=70)

def open_link3():
    webbrowser.open("https://www.ebay.com/sch/i.html?_nkw=star+link+travel+case&_sop=12")

imgpath_roam = 'C:\\Users\\admin\\PycharmProjects\\mainProject1\\jo\\accessories_actuated_travel_case.webp'
img_roam = Image.open(imgpath_roam)
img_roam = img_roam.resize((200, 200))
tk_img_roam = ImageTk.PhotoImage(img_roam)
img_label_roam = Label(f, image=tk_img_roam, bg='black')
img_label_roam.image = tk_img_roam
img_label_roam.place(x=0, y=150)
img_label_roam.bind("<Button-1>", lambda e: open_link3())



text2_home = Label(f, text="STARLINK TRAVEL CASE", font=('Calibri', 15), fg='white', bg='black')
text2_home.place(x=5,y=360)


def open_link4():
    webbrowser.open("https://www.ebay.com/sch/i.html?_nkw=ethernet+adapter+starlink&_sop=12")

imgpath_roam = 'C:\\Users\\admin\\PycharmProjects\\mainProject1\\jo\\accessories_ethernet_adapter.webp'
img_roam = Image.open(imgpath_roam)
img_roam = img_roam.resize((200, 200))
tk_img_roam = ImageTk.PhotoImage(img_roam)
img_label_roam = Label(f, image=tk_img_roam, bg='black')
img_label_roam.image = tk_img_roam
img_label_roam.place(x=240, y=150)
img_label_roam.bind("<Button-1>", lambda e: open_link4())


text2_home = Label(f, text="ETHERNET ADAPTER", font=('Calibri', 15), fg='white', bg='black')
text2_home.place(x=255,y=360)


def open_link5():
    webbrowser.open("https://www.ebay.com/sch/i.html?_nkw=starlink+mesh+wifi+router&_sop=12")

imgpath_roam = 'C:\\Users\\admin\\PycharmProjects\\mainProject1\\jo\\accessories_mesh_wifi_router.webp'
img_roam = Image.open(imgpath_roam)
img_roam = img_roam.resize((200, 200))
tk_img_roam = ImageTk.PhotoImage(img_roam)
img_label_roam = Label(f, image=tk_img_roam, bg='black')
img_label_roam.image = tk_img_roam
img_label_roam.place(x=478, y=150)
img_label_roam.bind("<Button-1>", lambda e: open_link5())


text7_home = Label(f, text="MESH WIFI ROUTER", font=('Calibri', 15), fg='white', bg='black')
text7_home.place(x=500,y=360)



def open_link5():
    webbrowser.open("https://www.ebay.com/itm/285262239662?itmmeta=01HQWDTVRKTCEKQCJBB44A9RNF&hash=item426af457ae:g:GJYAAOSwDUBj2YQm&itmprp=enc%3AAQAIAAAA0LiQklXh2WPsSax05SZcHbdT08xRnZTOVRvcijWyA7nF2%2Bx8jVQmdOGxQpUcIa0CXt0dduSMNwvIV8UU5hk24H4UXpCkWQjz4kCN%2BTZKFsPOdumQ66wiU%2Bdv7DdikGiQ1YwgiIPFSWgI%2FeRg%2F%2BrH%2F8gqyq%2FXpW0pg8L3d5B3G7wq5nKzVoPRYzIJMfiG3QX9nX82TyIHSZA%2B%2FmnH9N3FeJq2DVUTnII%2B6C3KELRVCh%2BOXKhhmHHuLiaxeMZPonTIAL25TKx66rDCZLeJTvApZrY%3D%7Ctkp%3ABk9SR7C8642_Yw")

imgpath_roam = 'C:\\Users\\admin\\PycharmProjects\\mainProject1\\jo\\accessories_actuated_pipe_adapter_mount.webp'
img_roam = Image.open(imgpath_roam)
img_roam = img_roam.resize((200, 200))
tk_img_roam = ImageTk.PhotoImage(img_roam)
img_label_roam = Label(f, image=tk_img_roam, bg='black')
img_label_roam.image = tk_img_roam
img_label_roam.place(x=720, y=150)
img_label_roam.bind("<Button-1>", lambda e: open_link5())



text8_home = Label(f, text="PIPE ADAPTER MOUNT", font=('Calibri', 15), fg='white', bg='black')
text8_home.place(x=725,y=360)

def open_link8():
    webbrowser.open("https://www.ebay.com/sch/i.html?_nkw=starlink+short+wall+mount&_sop=12")

imgpath_roam = 'C:\\Users\\admin\\PycharmProjects\\mainProject1\\jo\\accessories_actuated_short_wall_mount.webp'
img_roam = Image.open(imgpath_roam)
img_roam = img_roam.resize((200, 200))
tk_img_roam = ImageTk.PhotoImage(img_roam)
img_label_roam = Label(f, image=tk_img_roam, bg='black')
img_label_roam.image = tk_img_roam
img_label_roam.place(x=950, y=150)
img_label_roam.bind("<Button-1>", lambda e: open_link8())


text9_home = Label(f, text="SHORT WALL MOUNT", font=('Calibri', 15), fg='white', bg='black')
text9_home.place(x=960,y=360)


def open_link9():
    webbrowser.open("https://www.ebay.com/sch/i.html?_nkw=starlink+long+wall+mount&_sop=12")

imgpath_roam = 'C:\\Users\\admin\\PycharmProjects\\mainProject1\\jo\\accessories_actuated_long_wall_mount.webp'
img_roam = Image.open(imgpath_roam)
img_roam = img_roam.resize((200, 200))
tk_img_roam = ImageTk.PhotoImage(img_roam)
img_label_roam = Label(f, image=tk_img_roam, bg='black')
img_label_roam.image = tk_img_roam
img_label_roam.place(x=1180, y=150)
img_label_roam.bind("<Button-1>", lambda e: open_link9())


text10_home = Label(f, text="LONG WALL MOUNT", font=('Calibri', 15), fg='white', bg='black')
text10_home.place(x=1190,y=360)

def open_link10():
    webbrowser.open("https://www.ebay.com/sch/i.html?_from=R40&_nkw=starlink+pivot+mount&_sacat=0&_sop=12&_blrs=spell_auto_correct")

imgpath_roam = 'C:\\Users\\admin\\PycharmProjects\\mainProject1\\jo\\accessories_actuated_pivot_mount.webp'
img_roam = Image.open(imgpath_roam)
img_roam = img_roam.resize((200, 200))
tk_img_roam = ImageTk.PhotoImage(img_roam)
img_label_roam = Label(f, image=tk_img_roam, bg='black')
img_label_roam.image = tk_img_roam
img_label_roam.place(x=0, y=420)
img_label_roam.bind("<Button-1>", lambda e: open_link10())

text10_home = Label(f, text="PIVOT MOUNT", font=('Calibri', 15), fg='white', bg='black')
text10_home.place(x=20,y=630)

def open_link11():
    webbrowser.open("https://www.ebay.com/itm/285040392524?itmmeta=01HQX0KJ4YC0K1SGEFJDP6BNQY&hash=item425dbb394c:g:fBUAAOSwsRxjdEb5&itmprp=enc%3AAQAIAAAA8OXQ%2BJJLYkVMcuL58gPnGViwiXMU6s2pYWk8OMNYr5G4qyo7NlUmEdg4ddxWPnmTMG41ly%2F1WZpCF1PdumAtzilx%2F2YPQ1Pd9soeVqACP8kBZ6C9QMlO7LZM9eciUOSw%2F33Abc8KTjBrJt3QKKW0JQs6FGD16lexXDUkII9%2BAw7gdsMDimcmWU4belDfQbHeGQMFVXUm8qo5orKjNBECt2x7FdP1b3We%2BHlYCfXQKmyCFsKB%2FlvQPCysDxvQ%2F4eDZv5h4NI1xqO76u1tfM9igSDOIrRfyd2J3z612413lRk%2FGzFkLEFOPaEZ7K2JIZ1igQ%3D%3D%7Ctkp%3ABFBMxKLOoL9j")

imgpath_roam = 'C:\\Users\\admin\\PycharmProjects\\mainProject1\\jo\\accessories_actuated_ground_pole_mount.webp'


img_roam = Image.open(imgpath_roam)
img_roam = img_roam.resize((200, 200))
tk_img_roam = ImageTk.PhotoImage(img_roam)
img_label_roam = Label(f, image=tk_img_roam, bg='black')
img_label_roam.image = tk_img_roam
img_label_roam.place(x=240, y=420)
img_label_roam.bind("<Button-1>", lambda e: open_link11())

text10_home = Label(f, text="GROUND POLE MOUNT", font=('Calibri', 15), fg='white', bg='black')
text10_home.place(x=240,y=630)

def open_link12():
    webbrowser.open("https://www.ebay.com/sch/i.html?_from=R40&_nkw=starlink+ridgeline+mount+kit&_sacat=0&_sop=12&_blrs=spell_auto_correct")
imgpath_roam = 'C:\\Users\\admin\\PycharmProjects\\mainProject1\\jo\\accessories_actuated_ridgeline_mount.webp'


img_roam = Image.open(imgpath_roam)
img_roam = img_roam.resize((200, 200))
tk_img_roam = ImageTk.PhotoImage(img_roam)
img_label_roam = Label(f, image=tk_img_roam, bg='black')
img_label_roam.image = tk_img_roam
img_label_roam.place(x=478, y=420)
img_label_roam.bind("<Button-1>", lambda e: open_link12())


text10_home = Label(f, text="RIDGELINE MOUNT KIT", font=('Calibri', 15), fg='white', bg='black')
text10_home.place(x=478,y=630)

def open_link12():
    webbrowser.open("https://www.ebay.com/itm/276327814427?itmmeta=01HQX1Y48PH8ZNFXNWEFH85ER6&hash=item40566bd51b:g:5tQAAOSwRsNlxtQw&itmprp=enc%3AAQAIAAABAL0H65AQuGGIhfs55pzQXlMvtQ6HBR7HhG5UtYo%2Bhng52nYB6ubNDHd2GQBwfDTUNkJD%2FA1sTv8Km7IulO2PhxFF8l1pTf%2FWWWCuUR8qhqe5wDdsUvog%2FrEWcvaF1fLvYtFOra%2BV608OlJTFd2sbtN%2BCicJVHJEPikLzxEjEvKGpbDMhIeh%2BUoVDlUcDav8pORmj4RsP4YB4JgRG%2BZfvowv5sZdI70G%2Bz9Bt3hzOr8qNWZ5kTzexcGpoIeU%2BeK3skkrTfmwEo%2B6DfYyusc%2FiKVU0qTrgyiSYkpL2XuZR2jO%2FndR%2BGXH3BnPqatYXsh9GETxLdMXMegsKk7lSOONnuAM%3D%7Ctkp%3ABFBMtMT4ob9j")
imgpath_roam = 'C:\\Users\\admin\\PycharmProjects\\mainProject1\\jo\\accessories_flathp_pipe_Adapter.webp'


img_roam = Image.open(imgpath_roam)
img_roam = img_roam.resize((200, 200))
tk_img_roam = ImageTk.PhotoImage(img_roam)
img_label_roam = Label(f, image=tk_img_roam, bg='black')
img_label_roam.image = tk_img_roam
img_label_roam.place(x=720, y=420)
img_label_roam.bind("<Button-1>", lambda e: open_link12())



text11_home = Label(f, text="FLAT HIGH PERFORMANCE", font=('Calibri', 15), fg='white', bg='black')
text11_home.place(x=715,y=630)


text12_home = Label(f, text="PIPE ADAPTER", font=('Calibri', 15), fg='white', bg='black')
text12_home.place(x=760,y=660)

def open_link13():
    webbrowser.open("https://www.ebay.com/sch/i.html?_from=R40&_nkw=starlink+flat+high+performance+25m+starlink+cable&_sacat=0&_sop=12&_blrs=spell_auto_correct")
imgpath_roam = 'C:\\Users\\admin\\PycharmProjects\\mainProject1\\jo\\accessories_hp_25m_starlink_cable.webp'


img_roam = Image.open(imgpath_roam)
img_roam = img_roam.resize((200, 200))
tk_img_roam = ImageTk.PhotoImage(img_roam)
img_label_roam = Label(f, image=tk_img_roam, bg='black')
img_label_roam.image = tk_img_roam
img_label_roam.place(x=960, y=420)
img_label_roam.bind("<Button-1>", lambda e: open_link13())

text13_home = Label(f, text="FLAT HIGH PERFORMANCE", font=('Calibri', 15), fg='white', bg='black')
text13_home.place(x=955,y=630)



text13_home = Label(f, text="24M STARLINK CABLE", font=('Calibri', 15), fg='white', bg='black')
text13_home.place(x=970,y=660)


def open_link14():
    webbrowser.open("https://www.ebay.com/itm/296103405096?itmmeta=01HQX4A5WK3W5YQW6XXH2DBG43&hash=item44f1236628:g:LB8AAOSwPqVlPvYe&itmprp=enc%3AAQAIAAAA0CE%2BG%2FOdDVQe1lvHKpXJDpYaTj9k1%2BY3Tb3Vmpmue9LMazGJ0%2BgGlUKg10AovlcBgWITJ0t%2FOShV9XOlhTM%2Fxf%2BI2mcIRVQGHDlTTlC1CTshqlCTf9FgXkniMbJEjDgDxzghM1hjgcd69j1eAgfFEi%2BW3KiaF7gDBBEL68EvADPtb2z0XwusPnNiM8630f47DtVaqjMMP1tPXT%2B52FjGQxJxhwugLYWeMSCKtyOir1NxDeEpnY0h7hwi44tei8BU82bpSHW%2BTN1brRH1wwp2zTU%3D%7Ctkp%3ABk9SR7DeqKS_Yw")
imgpath_roam = 'C:\\Users\\admin\\PycharmProjects\\mainProject1\\jo\\s-l500.webp'


img_roam = Image.open(imgpath_roam)
img_roam = img_roam.resize((200, 200))
tk_img_roam = ImageTk.PhotoImage(img_roam)
img_label_roam = Label(f, image=tk_img_roam, bg='black')
img_label_roam.image = tk_img_roam
img_label_roam.place(x=1180, y=420)
img_label_roam.bind("<Button-1>", lambda e: open_link14())


text13_home = Label(f, text="CEILING MOUNT", font=('Calibri', 15), fg='white', bg='black')
text13_home.place(x=1205,y=630)

def open_link15():
    webbrowser.open("https://www.ebay.com/sch/i.html?_nkw=starlink+short+wall+mount&_sop=12")

b1 = Button(f, text="SHOP", font=('Elephant', 15), fg='black', bg='white', command=open_link15)
b1.place(x=1250, y=40)

def star15():
    f.destroy()
    import satellite
b = Button(f, text="Next",font=('Elephant', 8), fg='black', bg='black', command=star15)
b.place(x=1280, y=100)


f.mainloop()

