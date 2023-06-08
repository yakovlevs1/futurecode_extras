import tkinter as tk
import time, random


# from tkinter import *
def get_text():
    string_from_entry = my_entry.get()
    label.config(text=string_from_entry)
    print(string_from_entry)


def move_button():
    i = random.randint(0, 400)
    j = random.randint(0, 400)
    my_button.place(x=i, y=j)

def click_big_button():
    lbl = tk.Label(root, text=my_entry.get())
    lbl.pack()


root = tk.Tk()
root.title("First example")
root.geometry("600x600+800+300")
label = tk.Label(root, text="ПРИВЕТ", font=("Arial", 20), fg="red", bg="gray", underline=1)
label.pack(padx=10, pady=10)


textbox = tk.Text(
    root, height=3, width=30, font=("Arial", 20), border=5, selectbackground="red"
)
# textbox.pack(padx=10, pady=10)

my_button = tk.Button(
    root,
    text="НЕ НАЖИМАЙ",
    font=("Arial", 20, "bold"),
    fg="red",
    bg="blue",
    activebackground="pink",
    activeforeground="yellow",
    command=click_big_button,
)
my_button.pack(padx=10, pady=10)

my_entry = tk.Entry(root, font=("Arial", 20), width=30)
my_entry.insert(0, "Введите текст")
my_entry.focus()
my_entry.pack(padx=10, pady=10)


buttonframe = tk.Frame(root, bg="gray")
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text="Button 1")
btn1.grid(row=0, column=0, sticky=tk.N)
btn2 = tk.Button(buttonframe, text="Button 2")
btn2.grid(row=0, column=1, sticky=tk.W)
btn3 = tk.Button(buttonframe, text="Button 3")
btn3.grid(row=0, column=2, sticky=tk.E)
btn4 = tk.Button(buttonframe, text="Button 4")
btn4.grid(row=1, column=0, sticky=tk.W)
btn5 = tk.Button(buttonframe, text="Button 5")
btn5.grid(row=1, column=1, sticky=tk.W)
btn6 = tk.Button(buttonframe, text="Button 6")
btn6.grid(row=1, column=2, sticky=tk.W + tk.E)
buttonframe.pack(fill="x")

root.mainloop()
