import tkinter as tk

root = tk.Tk()
root.title("Simple Calculator")


e = tk.Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(number):
    # current = e.get()
    # e.delete(0, tk.END)
    # e.insert(0, str(current) + str(number))
    e.insert(tk.END, number)


def click_button_clear():
    e.delete(0, tk.END)


def click_button_evaluate():
    result = eval(e.get())
    e.delete(0, tk.END)
    e.insert(0, result)


button_1 = tk.Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = tk.Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = tk.Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = tk.Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = tk.Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = tk.Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = tk.Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = tk.Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = tk.Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = tk.Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_addition = tk.Button(
    root, text="+", padx=40, pady=20, command=lambda: button_click("+")
)
button_equal = tk.Button(
    root, text="=", padx=90, pady=20, command=click_button_evaluate
)
button_clear = tk.Button(
    root, text="Clear", bg="red", padx=80, pady=20, command=click_button_clear
)


button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)

button_addition.grid(row=5, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_equal.grid(row=5, column=1, columnspan=2)


root.mainloop()
