import tkinter as tk
from tkinter import ttk
import hashlib

root = tk.Tk()
root.title('Password Hashing Encrypter')
root.geometry('400x150')

## -------- GUI ----------
pass_label = ttk.Label(root, text='Enter Password : ')
pass_label.grid(row=0, column=0, pady = 10)

pass_var = tk.StringVar()
pass_entry = ttk.Entry(root, width=30, textvariable=pass_var)
pass_entry.grid(row=0, column=1)
pass_entry.focus()


## -------- Hashing --------

def hashProcess():
    pwd = pass_var.get()

    passUtf8 = pwd.encode('utf-8')

    hash = hashlib.md5(passUtf8)
    hexa = hash.hexdigest()

    en_pwd = ttk.Label(root, text=f'Your encrypted password is {hexa}')
    en_pwd.grid(row=2, column=0, columnspan=5, pady=10, padx=10)

hash_btn = ttk.Button(root, text='Encrypt Password', command=hashProcess)
hash_btn.grid(row=1, column=0, pady=10, padx=10)


root.mainloop()