import tkinter as tk

def borrow_item():
    student_id = student_id_entry.get()
    item_name = item_entry.get()
    password = password_entry.get()

    if not student_id or not item_name or not password:
        result_label.config(text="Please fill all fields.", fg="#D71920")  # APC Red for warnings
    elif password == "admin123":
        result_label.config(text=f"{item_name} borrowed by {student_id}.", fg="#000000")  # Black for success
    else:
        result_label.config(text="Wrong admin password.", fg="#D71920")  # APC Red for errors

# Main window
root = tk.Tk()
root.title("Admin Borrow Authentication")
root.geometry("400x300")
root.configure(bg="#D71920")  # APC Red background

# UI frame in white
frame = tk.Frame(root, bg="#FFFFFF", padx=15, pady=15)
frame.place(relx=0.5, rely=0.5, anchor="center")

# Labels and entries styled with black text
tk.Label(frame, text="Student ID:", bg="#FFFFFF", fg="#000000", font=("Arial", 10, "bold")).pack(anchor="w")
student_id_entry = tk.Entry(frame, bg="#f0f0f0", fg="#000000", relief="solid")
student_id_entry.pack(fill="x", pady=5)

tk.Label(frame, text="Item Name:", bg="#FFFFFF", fg="#000000", font=("Arial", 10, "bold")).pack(anchor="w")
item_entry = tk.Entry(frame, bg="#f0f0f0", fg="#000000", relief="solid")
item_entry.pack(fill="x", pady=5)

tk.Label(frame, text="Admin Password:", bg="#FFFFFF", fg="#000000", font=("Arial", 10, "bold")).pack(anchor="w")
password_entry = tk.Entry(frame, show="*", bg="#f0f0f0", fg="#000000", relief="solid")
password_entry.pack(fill="x", pady=5)

tk.Button(frame, text="Authenticate & Borrow", bg="#000000", fg="#FFFFFF", font=("Arial", 10, "bold"), command=borrow_item).pack(pady=15)

result_label = tk.Label(frame, text="", bg="#FFFFFF", fg="#D71920", font=("Arial", 10, "bold"))
result_label.pack()

root.mainloop()
