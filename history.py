import tkinter as tk
from tkinter import ttk

def history_frame(root):
    def hide_everything():
        search_entry.pack_forget()
        back_button.pack_forget()
        search_frame.pack_forget()
        title.pack_forget()
        tree.pack_forget()
    # Function to update the table (initially empty)
    def update_list():
        tree.delete(*tree.get_children())
        # Add real data here later if needed
        pass

    # Back button function
    def go_back():
        hide_everything()
        from admin_menu import admin_menu_frame
        admin_menu_frame(root)

    # Main window

    # Back button
    back_button = tk.Button(root, text="← Back", command=go_back,
                            bg="#1b1f3b", fg="white", font=("Arial", 10, "bold"))
    back_button.pack(anchor="w", padx=10, pady=(10, 0))

    # Title bar
    title = tk.Label(root, text="History", font=("Arial", 20, "bold"),
                    bg="#1b1f3b", fg="white")
    title.pack(fill="x", pady=(5, 0))

    # Search text only (no button)
    search_frame = tk.Frame(root, bg="#d9d9d9")
    search_frame.pack(pady=10)

    tk.Label(search_frame, text="Search:", bg="#d9d9d9", font=("Arial", 11)).pack(side="left")
    search_entry = tk.Entry(search_frame, font=("Arial", 11))
    search_entry.pack(side="left", padx=5)

    # Table setup with Student ID, Item, Date, and Quantity columns
    columns = ("Student ID", "Item", "Date", "Quantity")
    tree = ttk.Treeview(root, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col)
    tree.pack(fill="both", expand=True, padx=10, pady=10)

    # Treeview style
    style = ttk.Style()
    style.configure("Treeview.Heading", font=("Arial", 11, "bold"),
                    background="#d9d9d9", foreground="black")
    style.configure("Treeview", font=("Arial", 10), rowheight=25,
                    background="white", foreground="black")

    # Launch GUI
    update_list()

