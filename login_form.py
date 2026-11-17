import tkinter as tk
from tkinter import messagebox


# Part 7 - Login function
def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "12345":
        messagebox.showinfo(
            "LOGIN SUCCESSFULLY!",
            "Welcome Admin!"
        )
    else:
        messagebox.showerror(
            "LOGIN FAILED!",
            "Invalid Username and Password!"
        )


# Part 3 - Main window
root = tk.Tk()
root.title("Login Form")
root.geometry("400x350")
root.configure(bg="purple")

# Part 4 - Title
title_label = tk.Label(
    root,
    text="USER LOGIN",
    font=("Arial", 20, "bold"),
    bg="#f0f2f5",
    fg="black"
)
title_label.pack(pady=5)

# Part 5 - Username label and entry
username_label = tk.Label(
    root,
    text="Username",
    font=("Arial", 11),
    bg="#f0f2f5",
    fg="black"
)
username_label.pack(pady=5)

username_entry = tk.Entry(
    root,
    font=("Arial", 12),
    width=25
)
username_entry.pack(pady=5)

# Part 6 - Password label and entry
password_label = tk.Label(
    root,
    text="Password",
    font=("Arial", 12),
    bg="#f0f2f5",
    fg="black"
)
password_label.pack(pady=5)

password_entry = tk.Entry(
    root,
    font=("Arial", 12),
    width=25,
    show="*"
)
password_entry.pack(pady=5)

# Part 8 - Login button
login_button = tk.Button(
    root,
    text="LOG IN",
    font=("Arial", 12, "bold"),
    bg="blue",
    fg="white",
    width=20,
    command=login
)
login_button.pack(pady=20)

# Part 9 - Run the application
root.mainloop()