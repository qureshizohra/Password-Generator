import tkinter as tk
from tkinter import messagebox
import secrets
import string

def generate_password_gui():
    length = int(length_entry.get())
    use_upper = upper_var.get()
    use_digits = digits_var.get()
    use_special = special_var.get()

    characters = string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    password = ''.join(secrets.choice(characters) for _ in range(length))
    result_label.config(text=f"Generated Password: {password}")


root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text="Password Length").pack()
length_entry = tk.Entry(root)
length_entry.pack()

upper_var = tk.BooleanVar()
tk.Checkbutton(root, text="Include Uppercase", variable=upper_var).pack()

digits_var = tk.BooleanVar()
tk.Checkbutton(root, text="Include Digits", variable=digits_var).pack()

special_var = tk.BooleanVar()
tk.Checkbutton(root, text="Include Special Characters", variable=special_var).pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password_gui)
generate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()