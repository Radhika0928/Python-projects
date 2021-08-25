import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox as mb
from mark_attendance import op

def capture(name_var):
    window = tk.Tk()
    name=name_var
    title_font = tkfont.Font(family='Helvetica', size=18, weight="bold")
    #entry_font = tkfont.Font(family='Helvetica', size=12)
    window.title("Face_Recogniser")
    window.resizable('false', 'false')
    window.geometry("520x300")
    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)

    def on_closing():
        mb.askokcancel("Quit", "Are you sure?")
        window.destroy()

    def cface():
        import add_user
        l1.config(text=str("Captured Images = 0 "))
        mb.showinfo("INSTRUCTIONS", "We will Capture some picture of your Face.")
        x=add_user.datset(name)
        l1.config(text=str("Number of images captured = " + str(x)))
        mb.showinfo("MESSAGE", "Data has been successfully saved")

    def homepage():
        window.destroy()
        op()

    window.protocol("WM_DELETE_WINDOW", on_closing)

    l1=tk.Label(window,text="Number of images captured = 0",font=title_font,fg="#263942")
    l1.place(x=20,y=20)

    b1=tk.Button(window,text="Capture Data Set",padx=5,pady=5,fg="#ffffff", bg="#263942",command=cface)
    b1.place(x=40,y=80)

    b1 = tk.Button(window, text=" Mark Attendance ", padx=7, pady=5, fg="#ffffff", bg="#263942",command=homepage)
    b1.place(x=210, y=80)

    window.mainloop()
# capture("radhika")