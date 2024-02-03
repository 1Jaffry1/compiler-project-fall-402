# import mysyn
import tkinter as tk
from tkinter import messagebox


class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("SQL Create Compiler")
        self.root.geometry("800x500")

        self.label = tk.Label(self.root, text="Group: Jafari, Faghih Mousavi, Arabzadeh", font=("Arial", 18))
        self.label.pack(pady=5)

        self.tb = tk.Text(self.root, height=12, font=("Courier New", 20))
        self.tb.pack(padx=10, pady=6)

        self.run = tk.Button(self.root, text="RUN", font=("Arial", 15), command=self.show_message)
        self.run.pack()

        self.root.mainloop()

    def show_message(self):
        print(self.tb.get('1.0', tk.END) is None)
        #     messagebox.showinfo("No input!")
        # else:
        #     messagebox.showinfo(message=self.tb.get('1.0', tk.END))
            # messagebox.showinfo(title="alert", message="No input provided")
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
