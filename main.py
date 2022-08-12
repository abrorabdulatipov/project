# from tkinter import *
# root = Tk()
# root.title('window')
# root.geometry('250x280')
# root.config(bg = 'grey')
# count = 0
# # color = ('grey', 'yellow')
# def d():
#     global count
#     count += 1
#     if count==34:
#         count = 0
#     # print(count)
#     bt.config(bg='green')
#
# bt = Button(root, text='🟪', width=7, height=3, bg='blue', command=d)
# bt.pack()
#
#
# root.mainloop()
#
#
#
#
#
#
# from tkinter import Label, Tk
# root = Tk()
# label1 = Label(root, text='Option1', width=15, height=7, bg='green')
# label2 = Label(root, text='Option2', width=15, height=7, bg = 'grey')
# label1.pack()
# label2.pack()
#
# root.mainloop()
#
#
# from tkinter import *
# root = Tk()
# root.geometry('200x150')
# count = 0
# def f():
#     global count
#     count += 1
#
#     label.config(text=count)
# label = Label(root, text='0', width=10, height=3)
# label.pack()
#
# btn = Button(root, text='Add', bg='grey', width=10, height=3, command=f)
# btn.pack()
# btn1 = Button(root, text='remove', bg='red', width=10, height=3, command=f)
# btn1.pack()
#
# root.mainloop()
#
#
# from tkinter import *
# root = Tk()
# label1 = Label(root, text='option1', bg = 'teal', fg = 'black')
# label2 = Label(root, text='option2', bg = 'red', fg = 'black')
# label3 = Label(root, text='option3', bg = 'green', fg = 'black')
# label4 = Label(root, text='option4', bg = 'yellow', fg = 'black')
# label5 = Label(root, text='option5', bg = 'orange', fg = 'black', width=13)
#
# label1.grid(row=0, column=0)
# label2.grid(row=0, column=1)
# label3.grid(row=0, column=2)
# label4.grid(row=1, column=0)
# label5.grid(row=1, column=1, columnspan=2)
#
# root.mainloop()
#
#
# from tkinter import *
# root = Tk()
# root.geometry('400x500')
# def f():
#     gt = entry.get()
#     if len(gt)!=0:
#          print(gt)
#          entry.delete(0, END)
#     entry.delete(0, END)
# entry = Entry(root, width=20, font=('ALGERIAN', 20))
# btn = Button(root, text='Get', font=('ALGERIAN', 20), command=f)
# entry.pack()
# btn.pack()
#
# root.mainloop()