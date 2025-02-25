import tkinter as tk
from tkinter import messagebox

def on_click(button_text):
    current = entry_var.get()
    if button_text == "=":
        try:
            result = eval(current)
            entry_var.set(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression")
            entry_var.set("")
    elif button_text == "C":
        entry_var.set("")
    else:
        entry_var.set(current + button_text)

# Create main window
root = tk.Tk()
root.title("Basic Calculator")
root.geometry("300x400")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), justify='right', bd=10, relief=tk.GROOVE)
entry.pack(fill=tk.BOTH, ipadx=8, ipady=8, padx=10, pady=10)

# Button layout
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+')
]

frame = tk.Frame(root)
frame.pack()

for row in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
    for btn_text in row:
        btn = tk.Button(row_frame, text=btn_text, font=("Arial", 22), command=lambda b=btn_text: on_click(b))
        btn.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=5, pady=5)

root.mainloop()
