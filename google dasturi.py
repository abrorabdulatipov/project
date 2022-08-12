from tkinter import *
import webbrowser

root = Tk()
root.title('Qidruv tizmi')
root.geometry('500x300')
root.config(bg='#00001a')


def qidir():
    webbrowser.open_new_tab(f'http://www.google.com/search?btnG=1&q=%{sech.get()}')


def donoting():
    l = LabelFrame(root, text='Muolif haqida', bg='#709900')
    l.pack(fill=BOTH, expand=True)
    donoting = Label(l, text="bu dastur egasi *******\n"
                             "rahmat dasturimizni kuzatganiglar uchun").pack()


def dhaqida():
    global lframe
    lframe = LabelFrame(root, text='Dastur haqida', bg='#709900')
    lframe.pack(fill=BOTH, expand=True)
    dhaqida = Label(lframe, text="Haqida\n"
                                 "Biz bu dasturni Python"
                                 " kursda yozdim ", bg="#709900").pack()


def asosiy():
    a = LabelFrame(root, text='Mualif haqida', bg='#709900')
    a.pack(fill=BOTH, expand=True)
    asosiy = Label(a, text="BU DASTURNI WEB PYTHONDA ISHLAB CHIQARILGAN\n"
                           "DASTURNI EGASI *******\n"
                           "MUROJAT UCHUN +998 91 *** 20 28\n"
                           "TELEGRAM Arslon7F_7A_ARSLON\n"
                           "DASTURIMZDA KAMCHLIK BO`LSA UZUR").pack()


menubar = Menu(root, bg='black', fg='white')
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='Asosiy', command=asosiy)
menubar.add_cascade(label='Asosiy', menu=filemenu)

abautmenu = Menu(menubar, tearoff=0)
abautmenu.add_command(label='Dastur haqida', command=dhaqida)

abautmenu.add_command(label='Muaolif haqida', command=donoting)
menubar.add_cascade(label='Haqida', menu=abautmenu)

chiqish = Menu(menubar, tearoff=0)
chiqish.add_command(label='chiqish', command=quit)
menubar.add_cascade(label='Chqish', menu=chiqish)
root.config(menu=menubar)

lb = Label(root, text='Google ', font=('Arial', 15),
           bg='#00001a', fg='white').pack()

soz = Label(root, text='qidradigan so\'zni kiriting:',
            font=('Arial', 15), bg='black', fg='white').place(x=125, y=75)

sech = Entry(root, fg='#00001a', font=('Arail 15'),
             relief=SOLID, width=25, cursor='spider')
sech.place(x=125, y=100)

qidr = Button(root, text='Qidirish', bg='blue',
              fg='white', font=('Arial 15'),
              relief=SOLID, cursor='hand2',
              width=25, command=qidir).place(x=120, y=125)

root.mainloop()
