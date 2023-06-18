import tkinter as tk

root = tk.Tk()

root.title("APpPpP")
root.geometry("500x500")


label = tk.Label(root, text="Hello World", font=("Arial", 20))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=3, width=30, font=("Arial", 20))
textbox.pack(padx=100, pady=10)

myentry = tk.Entry(root, font=("Arial", 20))
myentry.pack(pady=10)

def click_big_button():
    lbl = tk.Label(root, text=myentry.get())
    lbl.pack()


button = tk.Button(
    root,
    text="Click Me",
    font=("Arial", 20),
    fg="red",
    bg="blue",
    activebackground="pink",
    activeforeground="yellow",
    command=click_big_button
)
button.pack(pady=10)


buttonframe = tk.Frame(root, background="grey")
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=2)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text="Button 1")
btn1.grid(row=0, column=0, sticky=tk.W + tk.E)
btn2 = tk.Button(buttonframe, text="Button 2")
btn2.grid(row=0, column=1, sticky=tk.W + tk.E)
btn3 = tk.Button(buttonframe, text="Button 3")
btn3.grid(row=0, column=2, sticky=tk.W + tk.E)
btn4 = tk.Button(buttonframe, text="Button 4")
btn4.grid(row=1, column=0, sticky=tk.W + tk.E)
btn5 = tk.Button(buttonframe, text="Button 5")
btn5.grid(row=1, column=1, sticky=tk.W + tk.E)
btn6 = tk.Button(buttonframe, text="Button 6")
btn6.grid(row=1, column=2, sticky=tk.W + tk.E)

buttonframe.pack(fill="both")
root.mainloop()
