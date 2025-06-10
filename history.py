import tkinter as tk
from tkinter import messagebox
history_data = []

def add_to_history(new_data):
        history_data.append(new_data)

def history_frame(root): 

    # Allow root to expand
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    frames = {}

    def show_frame(name):
        for f in frames.values():
            f.grid_forget()
        frames[name].grid(row=0, column=0, sticky="nsew")

    def hide_everything():
        for widget in root.winfo_children():
            widget.grid_forget()

    def go_back():
        hide_everything()
        from admin_menu import admin_menu_frame
        admin_menu_frame(root)

    # Main container frame
    frame = tk.Frame(root, bg="#d9d9d9")
    frames['main'] = frame
    frame.grid(row=0, column=0, sticky="nsew")
    frame.grid_rowconfigure(99, weight=1)
    for i in range(5):
        frame.grid_columnconfigure(i, weight=1)  # make columns expand

    # Back Button
    back_button = tk.Button(frame, text="← Back", command=go_back,
                            bg="#1b1f3b", fg="white", font=("Arial", 10, "bold"))
    back_button.grid(row=0, column=0, sticky="w", padx=10, pady=(10, 0), columnspan=5)

    # Title
    title = tk.Label(frame, text="History", font=("Arial", 20, "bold"),
                     bg="#1b1f3b", fg="white")
    title.grid(row=1, column=0, columnspan=5, sticky="ew", pady=5)

    # Search Bar
    search_frame = tk.Frame(frame, bg="#d9d9d9")
    search_frame.grid(row=2, column=0, columnspan=5, sticky="ew", pady=10)
    tk.Label(search_frame, text="Search:", bg="#d9d9d9", font=("Arial", 11)).pack(side="left")
    search_entry = tk.Entry(search_frame, font=("Arial", 11))
    search_entry.pack(side="left", padx=5)

    # Header Row
    headers = ["Student ID", "Name","Time", "borrowed","Date", "time Sent"]
    for col, text in enumerate(headers):
        tk.Label(frame, text=text, font=("Arial", 11, "bold"),
                 bg="#cccccc", width=15, anchor="w").grid(row=3, column=col, sticky="ew", padx=2, pady=2)

    # Data Rows
    for idx, record in enumerate(history_data):
        row = idx + 6  # Start after headers
        student_id = record.get("Student_ID", "")
        name = record.get("Name", "")
        time = record.get("Time","")
        borrowed_equipment = record.get("borrowed_data")
        date = f"{record.get('Month')}/{record.get('Day')}/{record.get('Year')}"
        time_sent = record.get("Date_sent", "")
        values = [student_id, name, time,borrowed_equipment,date, time_sent]
        for col, val in enumerate(values):
            tk.Label(frame, text=val, font=("Arial", 10), bg="white", anchor="w").grid(
                row=row, column=col, sticky="ew", padx=2, pady=2)

    show_frame('main')
