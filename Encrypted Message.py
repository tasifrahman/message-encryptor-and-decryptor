from tkinter import *
from tkinter import messagebox
import binarycipher

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(encrypted_text)

def ciphertext(event=None):
    text = entry_text.get("1.0", END).strip()
    key = entry_key.get().strip()
    
    if len(key) < 8:
        encrypted_text_label.config(text="Key must be at least 8 characters long")
    else:
        global encrypted_text
        encrypted_text = binarycipher.encryption(text, key)
        encrypted_text_label.config(text=f"Encrypted Text: {encrypted_text}")
        copy_button.grid(row=4, column=1, pady=5)

def clear_fields():
    entry_text.delete("1.0", END)
    encrypted_text_label.config(text="",fg="#0c8f00")
    copy_button.grid_forget()

def key_entry_handler(event):
    if event.keysym == "Return":
        ciphertext()

root = Tk()
root.title("Encryption and Decryption")
root.geometry("500x350")  # Adjusted height for new button
root.configure(bg='#242424')

# Labels
label_text = Label(root, text="TEXT->", bg='#242424',fg="#ababab")
label_text.grid(row=0, column=0, padx=10, pady=10)

label_key = Label(root, text="KEY->", bg='#242424',fg="#ababab")
label_key.grid(row=1, column=0, padx=10, pady=10)

# Text and Entry Widgets
entry_text = Text(root, height=5, width=50,bg="#474747",fg="#dbdbdb")
entry_text.grid(row=0, column=1, padx=10, pady=10)

entry_key = Entry(root, width=50,bg="#474747",fg="#dbdbdb")
entry_key.grid(row=1, column=1, padx=10, pady=10)
entry_key.bind("<Return>", key_entry_handler)  # Bind Return key to key_entry_handler

# Buttons
submit_button = Button(root, text="Enter", command=ciphertext, bg='#474747',fg="#ababab")
submit_button.grid(row=2, column=1, pady=10)

copy_button = Button(root, text="Copy Text to Clipboard", command=copy_to_clipboard, bg='#474747',fg="#ababab")

clear_button = Button(root, text="Clear Text", command=clear_fields, bg='#474747',fg="#ababab")
clear_button.grid(row=5, column=1, pady=10)

# Encrypted Text Label
encrypted_text_label = Label(root, text="", wraplength=400, bg='#242424',fg="#0c8f00")
encrypted_text_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Bind Enter key in entry_text to move focus to entry_key
entry_text.bind("<Return>", lambda event: entry_key.focus_set())

root.mainloop()
