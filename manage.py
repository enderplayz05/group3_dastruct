import tkinter as tk
from tkinter import ttk

def manage_frame(root):
    def hide_everything():
        header.pack_forget()
        frame.pack_forget()
        table_frame.pack_forget()
        tree.pack_forget()
        btn_frame.pack_forget()
        back_button.pack_forget()
        next_button.pack_forget()


    def go_back():
        hide_everything()
        from admin_menu import admin_menu_frame
        admin_menu_frame(root)
    # Header
    header = tk.Frame(root, bg="#2d2f38", height=40)
    header.pack(fill="x")
    tk.Label(
        header,
        text="MANAGE APPOINTMENTS",
        font=("Arial", 14, "bold"),
        fg="white",
        bg="#2d2f38"
    ).pack(pady=5)

    # Form Frame
    frame = tk.Frame(root, bg="#e0e0e0")
    frame.pack(pady=10)

    # Student ID
    tk.Label(frame, text="Student ID", font=("Arial", 10), bg="#e0e0e0").grid(row=0, column=0, padx=5, pady=5)
    ttk.Combobox(frame, values=[]).grid(row=0, column=1, padx=5)

    # Time
    tk.Label(frame, text="Time", font=("Arial", 10), bg="#e0e0e0").grid(row=1, column=0, padx=5, pady=5)
    ttk.Combobox(frame, values=[]).grid(row=1, column=1, padx=5)

    # Date
    tk.Label(frame, text="Date", font=("Arial", 10), bg="#e0e0e0").grid(row=2, column=0, padx=5, pady=5)
    ttk.Combobox(frame, values=[]).grid(row=2, column=1, padx=5)

    # Table
    table_frame = tk.Frame(root)
    table_frame.pack(pady=10)

    tree = ttk.Treeview(table_frame, columns=("Item", "QTY"), show="headings", height=8)
    tree.heading("Item", text="Item")
    tree.heading("QTY", text="QTY")
    tree.pack()

    for _ in range(8):
        tree.insert("", "end", values=("", ""))

    # Next Label
    next_button = tk.Label(root, text="Next", font=("Arial", 10, "underline"), fg="blue", bg="#e0e0e0", cursor="hand2")
    next_button.pack()

    btn_frame = tk.Frame(root, bg="#e0e0e0")
    btn_frame.pack(pady=15)

    tk.Button(btn_frame, text="Cancel appointment").grid(row=0, column=0, padx=10)
    tk.Button(btn_frame, text="Save Changes").grid(row=0, column=1, padx=10)
    back_button = tk.Button(header, text="← Back", command=go_back,
                            bg="#1b1f3b", fg="white", font=("Arial", 10, "bold"))
    back_button.pack(anchor="w", padx=10, pady=(10, 0))
