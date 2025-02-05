from tkinter import *
from tkinter import messagebox

x = Tk()
x.title("ذکر روز های هفته")
x.geometry("460x210")
x.resizable(False, False)

frame1 = Frame(x)
frame1.grid()

def fb1():
    messagebox.showinfo("شنبه", ": ذکر روز شنبه (صد مرتبه)\nیا رب العالمین")

def fb2():
    messagebox.showinfo("یکشنبه", ": ذکر روز یکشنبه (صد مرتبه)\nیا ذالجلال والاکرام")

def fb3():
    messagebox.showinfo("دوشنبه", ": ذکر روز دوشنبه (صد مرتبه)\nیا قاضی الحاجات")

def fb4():
    messagebox.showinfo("سه شنبه", ": ذکر روز سه شنبه (صد مرتبه)\nیا ارحم الراحمین")

def fb5():
    messagebox.showinfo("چهارشنبه", ": ذکر روز چهارشنبه (صد مرتبه)\nیا حی یا قیوم")

def fb6():
    messagebox.showinfo("پنجشنبه", ": ذکر روز پنجشنبه (صد مرتبه)\nلا اله الا الله الملک الحق المبین")

def fb7():
    messagebox.showinfo("جمعه", ": ذکر روز جمعه (صد مرتبه)\nاللهم صل علی محمد و ال محمد")

b1 = Button(frame1, text = "شنبه", height = 5, width = 15, activebackground = "lightgreen", command = fb1)
b2 = Button(frame1, text = "یکشنبه", height = 5, width = 15, activebackground = "lightgreen", command = fb2)
b3 = Button(frame1, text = "دوشنبه", height = 5, width = 15, activebackground = "lightgreen", command = fb3)
b4 = Button(frame1, text = "سه شنبه", height = 5, width = 15, activebackground = "lightgreen", command = fb4)
b5 = Button(frame1, text = "چهارشنبه", height = 5, width = 15, activebackground = "lightgreen", command = fb5)
b6 = Button(frame1, text = "پنجشنبه", height = 5, width = 15, activebackground = "lightgreen", command = fb6)
b7 = Button(frame1, text = "جمعه", height = 5, width = 15, activebackground = "lightgreen", command = fb7)
b8 = Button(frame1, text = "خروج", height = 5, width = 15, activebackground = "red", command = x.destroy) 

lb = Label(x, text = "Programmed By MMD\nhttps://github.com/im-rmz-mmd", fg = "deepskyblue4", font = ("Fixedsys", 10))

b1.grid(row = 1, column = 3)
b2.grid(row = 1, column = 2)
b3.grid(row = 1, column = 1)
b4.grid(row = 1, column = 0)
b5.grid(row = 2, column = 3)
b6.grid(row = 2, column = 2)
b7.grid(row = 2, column = 1)
b8.grid(row = 2, column = 0)

lb.grid(row = 3, column = 0)

x.mainloop()