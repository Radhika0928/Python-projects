import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox as mb

def adduser():
    window = tk.Tk()
    title_font = tkfont.Font(family='Helvetica', size=18, weight="bold")
    entry_font = tkfont.Font(family='Helvetica', size=12)
    window.title("Face_Recogniser")
    window.resizable('false', 'false')
    window.geometry("520x300")
    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)

    def on_closing():
        mb.askokcancel("Quit", "Are you sure?")
        window.destroy()

    window.protocol("WM_DELETE_WINDOW", on_closing)

    l1 = tk.Label(window, text="Enter your name:", fg="#263942", font=title_font)
    l1.place(x=10, y=10)

    #name_var=tk.StringVar()
    e1 = tk.Entry(window, borderwidth=3, bg="lightgrey", font=entry_font)#,textvariable=name_var)
    e1.place(x=10, y=60)
    e1.focus()

    def start_training():
        import detect_face
        with open("namelist.txt","r") as f:
            global names
            names=[]
            names=f.read()
            if e1.get() == "" :
                mb.showerror("Error", "Name cannot be empty")
                return
            elif e1.get() in names.split():
                mb.showerror("Error", "Name already exists")
                return
            else:
                with open("namelist.txt","a") as f1:
                    f1.write(e1.get()+"\n")
                name=e1.get()
                window.destroy()
                detect_face.capture(name)

    b1 = tk.Button(window, text="  Next  ", fg="#ffffff", bg="#263942", padx=5, pady=5,command=start_training)
    b1.place(x=10, y=100)

    b2 = tk.Button(window, text=" Cancel ", fg="#ffffff", bg="#263942", padx=5, pady=5,command=on_closing)
    b2.place(x=100, y=100)

    window.mainloop()

# adduser()