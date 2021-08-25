import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox as mb
from Attendance_window import detect


def op():
    window = tk.Tk()
    #title_font = tkfont.Font(family='Helvetica', size=18, weight="bold")
    title_font = tkfont.Font(family='Helvetica', size=18,slant="italic")
    button_font=tkfont.Font(size=13)
    window.title("Face_Recogniser")
    window.resizable('false', 'false')
    window.geometry("550x300")
    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)

    def det():
        detect()
        mb.showinfo("Success","Attendance Marked successfully")
        mb.showinfo("Message","To mark another attendance click 'Next' or click 'Exit' to leave")
    def leave():
        mb.askokcancel("Quit", "Are you sure you want to quit?")
        window.destroy()

    l1=tk.Label(window,text=" Click Next button to Mark your attendance ",font=title_font,fg="#263942")
    l1.place(x=20,y=20)

    b1=tk.Button(window, text=" Next ", padx=15, pady=5, fg="#ffffff", bg="#263942",font=button_font,command=det)
    b1.place(x=50,y=80)

    b2=tk.Button(window, text=" Exit ", padx=18, pady=5, fg="#ffffff", bg="#263942",font=button_font,command=leave)
    b2.place(x=50,y=150)


    window.mainloop()


# op()
