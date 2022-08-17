from tkinter import *
root = Tk()

ishora = ''
firstNum = ''
def cal(number):
    getNum = str(entry.get())
    entry.delete(0, END)
    entry.insert(0, getNum+str(number))

def dev():
    global ishora, firstNum
    ishora='bolish'
    firstNum = entry.get()
    entry.delete(0, END)

def result():
    newNum = entry.get()
    entry.delete(0, END)
    if ishora=='bolish':
        entry.insert(0, f"{int(firstNum)/int(newNum)}")

entry = Entry(root, width=25, font=('consolas', 24))
backSpace = Button(root, text='C', font=('consolas', 24),
                   command=lambda : entry.delete(len(entry.get())-1, END))
point = Button(root, text='P', font=('consolas', 24), command=lambda : entry.delete(0, END))
devide = Button(root, text='/', font=('consolas', 24), command=dev)
multiply = Button(root, text='*', font=('consolas', 24))
subtract = Button(root, text='-', font=('consolas', 24))
equel = Button(root, text='=', font=('consolas', 24), command=result)


btn1 = Button(root, text=1, font=('consolas', 24), command=lambda : cal(1))
btn2 = Button(root, text=2, font=('consolas', 24), command=lambda : cal(2))
btn3 = Button(root, text=3, font=('consolas', 24), command=lambda : cal(3))

entry.grid(row=0, column=0, columnspan=4, pady=15, padx=15)
backSpace.grid(row=1, column=0)
point.grid(row=1, column=1)
devide.grid(row=1, column=2)
multiply.grid(row=1, column=3)
btn1.grid(row=2, column=0)
btn2.grid(row=2, column=1)
btn3.grid(row=2, column=2)
subtract.grid(row=2, column=3)
equel.grid(row=3, column=0, columnspan=4)

root.mainloop()