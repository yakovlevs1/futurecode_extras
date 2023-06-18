import tkinter as tk
from tkinter import messagebox


class MyGUI:

    def __init__(self):

        self.root = tk.Tk()

        self.root.title("My GUI")
        self.root.geometry("500x500")
        self.label = tk.Label(self.root, text="Hello World", font=("Arial", 20))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=3, width=30, font=("Arial", 20))
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack(padx=10, pady=10)

        self.check_state = tk.IntVar()

        self.check = tk.Checkbutton(self.root, text="Show Messagebox", font=("Arial", 20), variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="Click Me", font=("Arial", 20), command=self.show_message)
        self.button.pack(padx=10, pady=10)

        self.menubar = tk.Menu(self.root)

        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Close", command=self.on_closing)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Close w/o question", command=self.root.destroy)

        self.actionmenu = tk.Menu(self.menubar, tearoff=0)
        self.actionmenu.add_command(label="Show Message", command=self.show_message)

        
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.menubar.add_cascade(label="Action", menu=self.actionmenu)
        self.root.config(menu=self.menubar)

        self.clearbtn = tk.Button(self.root, text="Clear", font=("Arial", 20), command=self.clear)
        self.clearbtn.pack(padx=10, pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()
    
    def show_message(self):
        print("The button is clicked!")
        print(self.check_state.get())
        if self.check_state.get() == 1:
            print(self.textbox.get("1.0", tk.END))
            messagebox.showinfo(title="Messagebox", message=self.textbox.get("1.0", tk.END))
        else:
            messagebox.showwarning(title="Messagebox", message="Checkbox is unchecked")

    def shortcut(self, event):
        #print(event.keysym)
        #print(event.state)
        if event.state == 12 and event.keysym == "Return":
            print("ctrl+enter pressed")
            self.show_message()
        if event.state == 13 and event.keysym == "Return":
            print("shift+enter pressed")
        if event.keysym == "Escape":
            self.root.destroy()

    def on_closing(self):
        if messagebox.askyesno("Quit", "Do you want to quit?"):
            self.root.destroy()

    def clear(self):
        self.textbox.delete("1.0", tk.END)

MyGUI()