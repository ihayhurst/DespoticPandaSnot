#!/usr/bin/env python3
import tkinter as tk 

#Functions

class Application(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.myframe = tk.Frame(self.parent) 
        self.make_widgets()
        self.myframe.pack()

    def make_widgets(self):
        self.winfo_toplevel().title="Cardfight"
        self.label1 =  tk.Label(self.myframe, text="Hello World", fg="black").grid(row=0, column=0)
        self.button1 = tk.Button(self.myframe, text="wibble", fg="green") .grid(row=0, column=1)

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    app.pack(side="top", fill="both", expand=True)
    app.mainloop()
