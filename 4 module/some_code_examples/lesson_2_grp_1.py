import tkinter as tk
from tkinter import messagebox


class MyGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Class_GUI")
        self.root.geometry("500x500")
        self.label = tk.Label(self.root, text="Hello World!", font=("Arial", 20))
        self.label.pack(padx=20, pady=20)

        self.textbox = tk.Text(self.root, height=3, width=30, font=("Arial", 20))
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack(padx=10, pady=10)



        self.check_state = tk.IntVar()

        self.checkbtn = tk.Checkbutton(self.root, text="Done", font=("Arial", 20), variable=self.check_state)
        self.checkbtn.pack(pady=10)

        self.printbtn = tk.Button(self.root, text="Print", font=("Arial", 20), command=self.show_message)
        self.printbtn
        self.printbtn.pack(pady=10)

        self.menubar = tk.Menu(self.root)

        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Exit", command=self.on_closing)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit w/o question", command=self.root.destroy)
        
        self.actionmenu = tk.Menu(self.menubar, tearoff=0)
        self.actionmenu.add_command(label="Show message", command=self.show_message)

        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.menubar.add_cascade(label="Action", menu=self.actionmenu)

        self.root.config(menu=self.menubar)

        
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def print_check_state(self):
        print(self.check_state.get())

    def show_message(self):
        print("The button is clicked")
        print(self.check_state.get())
        if self.check_state.get() == 1:
            messagebox.showinfo(title="Message", message=self.textbox.get(1.0, tk.END))
        else:
            messagebox.showwarning(title="Message", message=self.textbox.get(1.0, tk.END))

    def on_closing(self):
        if messagebox.askyesno(title="Quit", message="Do you want to quit?"):
            self.root.destroy()

    def shortcut(self, event):
        print(f"Keysym: {event.keysym}")
        print(f"State: {event.state}")
        if event.state == 12 and event.keysym == "Return":
            self.show_message()
        if event.keysym == "Escape":
            self.root.destroy()

MyGUI()