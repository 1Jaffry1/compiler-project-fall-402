# import mysyn
import tkinter as tk
from tkinter import messagebox
import mysyn
import mylex


class GUI:
    def __init__(self):
        self.data = None
        self.root = tk.Tk()
        self.root.title("SQL Create Compiler")
        self.root.geometry("800x500")

        self.label = tk.Label(self.root, text="Group: Jafari, Faghih Mousavi, Arabzadeh", font=("Arial", 18))
        self.label.pack(pady=5)

        self.tb = tk.Text(self.root, height=12, font=("Courier New", 20))
        self.tb.pack(padx=10, pady=6)

        self.run = tk.Button(self.root, text="RUN", font=("Arial", 15), command=self.check_code)
        self.run.pack()

        self.root.mainloop()
        
    def run_code(self):
        mysyn.parser.parse(self.data)
        messagebox.showinfo(message=mylex.msg+'\n'+mysyn.msg)
        # print(mylex.msg+'\n'+mysyn.msg)

        

    def check_code(self):
        self.data = self.tb.get('1.0', tk.END)
        self.data = self.data.strip().upper()
        if self.data == "\n":
            messagebox.showinfo(message="No input! Please Enter SQL code")
        elif not self.data.__contains__(";"):
            messagebox.showinfo(message="FATAL: Missing ';' at end of code")
        else:
            self.run_code()


app = GUI()
# data = ""
# while True:
#     x = input()
#     if x.endswith(';'):
#         data += "\n"+x
#         break
#     else:
#         data += "\n"+x
# print(data)
# mysyn.parser.parse(data)
