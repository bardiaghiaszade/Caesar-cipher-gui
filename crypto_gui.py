"""
Tkinter GUI with two windows and optional encryption.
"""

import tkinter as tk
from crypto import caesar_encrypt


def transfer_text(*args):
    """Transfer text from window 1 to window 2."""
    text = input_text.get("1.0", tk.END)

    if encrypt_var.get():
        try:
            shift = int(shift_entry.get())
        except ValueError:
            shift = 3  # fallback if input is invalid

        text = caesar_encrypt(text, shift)

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, text)


root = tk.Tk()
root["bg"] = "black" 
root.title("Input Window")


encrypt_var = tk.BooleanVar()

input_text = tk.Text(root, height=10, width=40)
input_text.pack()

# Verschiebung input
shift_frame = tk.Frame(root)
shift_frame.pack(pady=5)

tk.Label(shift_frame, text="Verschiebung:").pack(side=tk.LEFT)

shift_entry = tk.Entry(shift_frame, width=5)
shift_entry.insert(0, "3")  # default shift
shift_entry.pack(side=tk.LEFT)

tk.Checkbutton(
    root,
    text="Encrypt text",
    variable=encrypt_var,
    command=transfer_text
).pack()

input_text.bind("<KeyRelease>", transfer_text)
shift_entry.bind("<KeyRelease>", transfer_text)

second_window = tk.Toplevel(root)
second_window.title("Output Window")

output_text = tk.Text(second_window, height=10, width=40)
output_text.pack()

root.mainloop()
