import tkinter as tk
import tkinter.font
from tkinter import messagebox

root = tk.Tk()
root.title("First GUI")
root.geometry("500x700+900+150")

some_font = tk.font.Font(
    family="Arial",
    size=20,
    weight="bold",
    slant="italic",
    underline=False,
    overstrike=False,
)
font_for_textbox = tk.font.Font(
    family="Arial",
    size=20,
    weight="bold",
    slant="roman",
    underline=False,
    overstrike=False,
)


counter = 0


def click_button():
    global counter
    counter += 1
    # print("Кнопка нажата {} раз".format(counter))
    print(state_of_checkbox.get())


def click_button2():
    global counter
    counter += 1
    lbl = tk.Label(root, text=f"Кнопка нажата {counter} раз")
    lbl.pack()


def log_click():
    auth = dict()
    auth["admin123"] = "1"
    auth["user1"] = "2"
    auth["guestgg"] = "3"

    login_from_entry = login_entry.get()
    psw_from_entry = psw_entry.get()

    try:
        if auth[login_from_entry] == psw_from_entry:
            print("Добро пожаловать")
        else:
            print("Неверный пароль")
    except KeyError:
        print("Неверный логин")


def on_closing():
    if messagebox.askyesno("Выход", "Хотите выйти?"):
        root.destroy()


label1 = tk.Label(
    root, text="Hello, World!", font=some_font, background="grey", foreground="black"
)
label1.pack(padx=20, pady=20)
# label1.place(x=100, y=100)
# label1.grid(row=0, column=0)

textbox = tk.Text(
    root,
    height=2,
    width=20,
    font=font_for_textbox,
    fg="blue",
    bg="red",
    selectbackground="blue",
    selectforeground="red",
)
textbox.pack(padx=20, pady=10)
# textbox.focus()

login_label = tk.Label(root, text="Login:", font=font_for_textbox)
login_label.pack(padx=20, pady=10)

login_entry = tk.Entry(
    root, font=font_for_textbox, selectbackground="red", selectforeground="green"
)
login_entry.pack(padx=20, pady=10)


psw_label = tk.Label(root, text="Password:", font=font_for_textbox)
psw_label.pack(padx=20, pady=10)

psw_entry = tk.Entry(
    root,
    font=font_for_textbox,
    show="*",
)
psw_entry.pack(padx=20, pady=10)


my_button = tk.Button(
    root,
    text="PRESS",
    font=some_font,
    bg="pink",
    fg="grey",
    activebackground="blue",
    activeforeground="red",
    command=click_button,
)
my_button.pack(padx=100, pady=10, fill="x")


log_button = tk.Button(
    root,
    text="LOGIN",
    font=some_font,
    command=log_click,
)
log_button.pack(padx=20, pady=10)


state_of_checkbox = tk.BooleanVar()

checkbox = tk.Checkbutton(root, text="Запомнить меня", variable=state_of_checkbox)
checkbox.pack()


def print_radio():
    print(var_for_radio.get())


var_for_radio = tk.IntVar()
radio1 = tk.Radiobutton(
    root,
    text="Male",
    variable=var_for_radio,
    value=1,
    command=print_radio,
)
radio1.pack()
radio2 = tk.Radiobutton(
    root,
    text="Female",
    variable=var_for_radio,
    value=0,
    command=print_radio,
)
radio2.pack()


root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
