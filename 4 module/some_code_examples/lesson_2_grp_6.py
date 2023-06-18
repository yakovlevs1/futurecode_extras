import tkinter as tk
import tkinter.font



class MyGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("First GUI")
        self.root.geometry("500x700+900+150")

        self.default_font = tk.font.Font(
            family="Arial",
            size=20,
        )

        self.frame_for_buttons = tk.Frame(self.root, background="red")

        for i in range(1, 4):
            for j in range(3):
                self.btn = tk.Button(
                    self.frame_for_buttons, text=str(i + 3 * j), font=self.default_font
                )
                self.btn.grid(row=j, column=i, sticky="ew")

        self.frame_for_buttons.pack(fill="both")

        self.login_label = tk.Label(self.root, text="Login:", font=self.default_font)
        self.login_label.pack(padx=20, pady=10)

        self.login_entry = tk.Entry(
            self.root,
            font=self.default_font,
            selectbackground="red",
            selectforeground="green",
        )
        self.login_entry.pack(padx=20, pady=10)
        self.login_entry.bind("<KeyPress>", self.focus_psw)

        self.psw_label = tk.Label(self.root, text="Password:", font=self.default_font)
        self.psw_label.pack(padx=20, pady=10)

        self.psw_entry = tk.Entry(self.root, font=self.default_font, show="*")
        self.psw_entry.pack(padx=20, pady=10)
        self.psw_entry.bind("<KeyPress>", self.shortcut)

        self.menubar = tk.Menu(self.root)

        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Close", command=self.root.destroy)
        self.filemenu.add_command(label="Open")
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Save")

        self.additional_menu = tk.Menu(self.filemenu, tearoff=0)
        self.additional_menu.add_command(label="Exit", command=self.root.destroy)

        self.filemenu.add_cascade(label="Edit", menu=self.additional_menu)

        self.menubar.add_cascade(label="File", menu=self.filemenu)

        self.root.config(menu=self.filemenu)

        self.root.mainloop()

    def try_to_login(self):
        auth = dict()
        auth["admin123"] = "1"
        auth["user1"] = "2"
        auth["guestgg"] = "3"

        login_from_entry = self.login_entry.get()
        psw_from_entry = self.psw_entry.get()

        try:
            if auth[login_from_entry] == psw_from_entry:
                print("Добро пожаловать")
            else:
                print("Неверный пароль")
        except KeyError:
            print("Неверный логин")

    def shortcut(self, event):
        print(event.keysym, end=" ")
        print(event.state)
        if event.keysym == "Escape":
            self.root.destroy()
        elif event.keysym == "Return" and (event.state == 8 or event.state == 262152):
            self.try_to_login()

    def focus_psw(self, event):
        print(event.keysym, end=" ")
        print(event.state)
        if event.keysym == "Return" and event.state == 8:
            self.psw_entry.focus()


MyGUI()
