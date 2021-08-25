import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox as mb
from tkinter import PhotoImage
from mark_attendance import op

window = tk.Tk()
title_font = tkfont.Font(family='Helvetica', size=18, weight="bold")
window.title("Face_Recogniser")
window.resizable('false', 'false')
window.geometry("520x300")
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

def on_closing():
    mb.askokcancel("Quit", "Are you sure?")
    window.destroy()

def addu():
    import input_name
    window.destroy()
    input_name.adduser()

def matt():
    window.destroy()
    op()


window.protocol("WM_DELETE_WINDOW", on_closing)

l1 = tk.Label(window, text="        Home Page        ", fg="#263942", font=title_font)
l1.place(x=5, y=20)

render = PhotoImage(file='homepagepic.png')
img = tk.Label(window, image=render)
img.image = render
img.place(x=230, y=15)

b1 = tk.Button(window, text="     Add new user     ", padx=3, pady=7, fg="#ffffff", bg="#263942", command=addu)
b1.place(x=70, y=75)

b2 = tk.Button(window, text="   Mark Attendance  ", pady=7, fg="#ffffff", bg="#263942",command=matt)
b2.place(x=70, y=135)

b3 = tk.Button(window, text="   Quit   ", padx=34, pady=4, fg="#263942", bg="#ffffff", command=on_closing)
b3.place(x=70, y=195)

window.mainloop()

