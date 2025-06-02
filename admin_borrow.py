import tkinter as tk
def admin_borrow_frame(root):
    def unhide():
            result_label.pack()
            item_listbox.pack(pady=5, fill="x")
            frame.place(relx=0.5, rely=0.5, anchor="center")
            password_entry.pack(pady=5)

    def borrow_item():
        student_id = student_id_entry.get()
        selected = item_listbox.curselection()
        password = password_entry.get()

        if not student_id or not selected or not password:
            result_label.config(text="Please fill all fields.", fg="#D71920")
        elif password == "admin123":
            items = [item_listbox.get(i) for i in selected]
            result_label.config(text=f"{', '.join(items)} borrowed by {student_id}.", fg="#FFFFFF")
        else:
            result_label.config(text="Wrong admin password.", fg="#D71920")


    frame = tk.Frame(root, bg="#FFFFFF", padx=15, pady=15)
    

    tk.Label(frame, text="Student ID:", bg="#FFFFFF", fg="#00205B").pack(anchor="w")
    student_id_entry = tk.Entry(frame, width=30)
    student_id_entry.pack(pady=5)

    tk.Label(frame, text="Select Items to Borrow:", bg="#FFFFFF", fg="#00205B").pack(anchor="w")
    item_listbox = tk.Listbox(frame, selectmode="multiple", height=7)
    items = [
        "basketball",
        "ping pong",
        "ping pong balls",
        "tennis racket",
        "tennis balls",
        "shuttlecocks",
        "badminton net"
    ]
    for item in items:
        item_listbox.insert(tk.END, item)


    tk.Label(frame, text="Admin Password:", bg="#FFFFFF", fg="#00205B").pack(anchor="w")
    password_entry = tk.Entry(frame, show="*", width=30)
    

    tk.Button(frame, text="Borrow", command=borrow_item, bg="#D71920", fg="white", width=20).pack(pady=10)

    result_label = tk.Label(frame, text="", bg="#FFFFFF", fg="#D71920")


