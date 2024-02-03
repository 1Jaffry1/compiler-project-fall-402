import os
import tkinter as tk
from tkinter import messagebox

import tkmacosx

import mysyn
import mylex
from tkmacosx import Button


class GUI:
    def __init__(self):
        self.data = None
        self.root = tk.Tk()
        self.root.title("SQL Create Compiler")
        self.root.geometry("800x500")
        self.root.resizable(width=False, height=False)
        bg = tk.PhotoImage(file="bg_image.png")
        photo = tk.Label(self.root, image=bg)
        photo.place(x=0, y=0)

        self.label = tk.Label(self.root,bg="#0A193E", fg="white" ,text="Group: Jafari, Faghih Mousavi, Arabzadeh", font=("Arial", 18))
        self.label.pack(pady=5)

        self.textbox = tk.Text(self.root, height=12,bg="#283747", fg="#FFFDD0" ,font=("Courier New", 20))
        self.textbox.pack(padx=10, pady=6)

        if os.name == "nt":
            self.run_button = tk.Button(self.root, text="▶︎ RUN", bg="black", fg="light green" ,font=("helvetica", 15),
                                    command=self.check_code)
        else:
            self.run_button = tkmacosx.Button(self.root, text="▶︎ RUN", bg="black", fg="light green" ,font=("helvetica", 15),
                                    command=self.check_code)
        self.run_button.pack()

        self.root.mainloop()
        
    def run_code(self):
        mylex.line_number = 0
        mylex.index = 0
        mylex.msg = ''
        mysyn.msg = ''
        mysyn.parser.parse(self.data)
        messagebox.showinfo(message=mylex.msg+'\n'+mysyn.msg)

        

    def check_code(self):
        self.data = self.textbox.get('1.0', tk.END)
        self.data = self.data.strip().upper()
        if self.data == "":
            messagebox.showinfo(message="No input! Please Enter SQL code")
        elif not self.data.__contains__(";"):
            messagebox.showinfo(message="FATAL: Missing ';' at end of code")
        else:
            self.run_code()


app = GUI()
