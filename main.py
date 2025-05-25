import tkinter as tk
from tkinter import ttk

def borrow_item():
    student_id = student_id_entry.get()
    item_name = item_combo.get()
    password = password_entry.get()

    if not student_id or item_name == "Select an item" or not password:
        result_label.config(text="Please fill all fields.", fg="#D71920")
    elif password == "admin123":
        result_label.config(text=f"{item_name} borrowed by {student_id}.", fg="#FFFFFF")
    else:
        result_label.config(text="Wrong admin password.", fg="#D71920")

root = tk.Tk()
root.title("Borrow Item - APC")
root.geometry("360x330")
root.configure(bg="#00205B")  # APC Navy Blue
frame = tk.Frame(root, bg="#FFFFFF", padx=20, pady=20)
frame.place(relx=0.5, rely=0.5, anchor="center")
tk.Label(frame, text="Student ID:", bg="#FFFFFF", fg="#00205B", font=("Arial", 10, "bold")).pack(anchor="w")
student_id_entry = tk.Entry(frame, bg="#F0F0F0", fg="#000000", width=30)
student_id_entry.pack(pady=5)
tk.Label(frame, text="Select Item:", bg="#FFFFFF", fg="#00205B", font=("Arial", 10, "bold")).pack(anchor="w")
item_combo = ttk.Combobox(frame, values=[
    "basketball",
    "ping pong",
    "ping pong balls",
    "tennis racket",
    "tennis balls",
    "shuttlecocks",
    "badminton net"
], state="readonly", width=28)
item_combo.set("Select an item")
item_combo.pack(pady=5)
tk.Label(frame, text="Admin Password:", bg="#FFFFFF", fg="#00205B", font=("Arial", 10, "bold")).pack(anchor="w")
password_entry = tk.Entry(frame, show="*", bg="#F0F0F0", fg="#000000", width=30)
password_entry.pack(pady=5)
tk.Button(frame, text="Borrow", command=borrow_item, bg="#D71920", fg="#FFFFFF", width=20).pack(pady=15)
result_label = tk.Label(frame, text="", bg="#FFFFFF", fg="#D71920", font=("Arial", 10, "bold"))
result_label.pack()

root.mainloop()
