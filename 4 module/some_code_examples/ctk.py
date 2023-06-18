#import tkinter as tk
import customtkinter as ctk

root = ctk.CTk()

ctk.set_appearance_mode("dark")


root.title("User-Login")
root.geometry("500x500")

def save_user_data():
    print(user_entry.get())
    print(pass_entry.get())

user_label = ctk.CTkLabel(root, text="Username")
user_label.pack(padx=10, pady=10)

user_entry = ctk.CTkEntry(root, width=130)
user_entry.pack(padx=10, pady=10)

pass_label = ctk.CTkLabel(root, text="Password")
pass_label.pack(padx=10, pady=10)

pass_entry = ctk.CTkEntry(root, width=130, show="*")
pass_entry.pack(padx=10, pady=10)

btn = ctk.CTkButton(root, text="Log In", command=save_user_data)
btn.pack(padx=10, pady=10)

root.mainloop()