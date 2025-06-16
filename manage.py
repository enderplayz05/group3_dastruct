import tkinter as tk
from tkinter import ttk
from history import history_data
manage_data = dict()

def manage_import_data(unique_key,new_data):
    manage_data[unique_key] = new_data

def manage_frame(root):

    def hide_everything():
        header.pack_forget()
        frame.pack_forget()
        table_frame.pack_forget()
        tree.pack_forget()
        btn_frame.pack_forget()
        back_button.pack_forget()
        next_button.pack_forget()
        add_item_btn.pack_forget()
        try:
            save_button.pack_forget()
            item_combo.pack_forget()
        except:
            print("already deleted")
    

        

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

    local_keys = list(manage_data.keys())

    # Unique ID
    tk.Label(frame, text="Unique ID", font=("Arial", 10), bg="#e0e0e0").grid(row=0, column=0, padx=5, pady=5)
    unique_ID_combo = ttk.Combobox(frame, values=[local_keys])
    unique_ID_combo.grid(row=0, column=1, padx=5)

    def on_id_selected(event):
        get_unique_ID = unique_ID_combo.get()
        if get_unique_ID in history_data:
            global get_student_ID
            global get_time
            global date
            global get_borrowed_data
            global get_month
            global get_year
            global get_day

            get_student_ID = history_data[get_unique_ID].get("Student_ID")
            get_time = history_data[get_unique_ID].get("Time")
            get_day = history_data[get_unique_ID].get("Day")
            get_month = history_data[get_unique_ID].get("Month")
            get_year = history_data[get_unique_ID].get("Year")
            date = f"{get_month}/{get_day}/{get_year}"
            get_borrowed_data = history_data[get_unique_ID].get("borrowed_data")
            show_infos()
            

    unique_ID_combo.bind("<<ComboboxSelected>>", on_id_selected)
    def show_infos():
        for var in history_data:
            get_unique_ID = unique_ID_combo.get()
            if get_unique_ID == var:
                global day_combo
                global month_combo
                global year_combo
                global time_combo
                global unsaved_items
                unsaved_items = []

                # Time
                tk.Label(frame, text="Time", font=("Arial", 10), bg="#e0e0e0").grid(row=2, column=0, padx=5, pady=5)
                time_options = ["7:30 AM - 9:30 AM","9:30 AM - 11:30 AM", "1:30 PM - 3:30 PM","3:30 PM - 5:30 PM"]
                time_combo = ttk.Combobox(frame, values=time_options)
                time_combo.set(get_time)
                time_combo.grid(row=2, column=1, padx=5)

                # Date
                tk.Label(frame, text="Date", font=("Arial", 10), bg="#e0e0e0").grid(row=3, column=0, padx=5, pady=5)
                # Month
                month_options = [f"{i:02}" for i in range(1, 13)]
                month_combo = ttk.Combobox(frame, values=month_options, width=5)
                month_combo.set(get_month)
                month_combo.grid(row=3, column=1, padx=(5, 0), sticky="w")

                # Day
                day_options = [f"{i:02}" for i in range(1, 32)]
                day_combo = ttk.Combobox(frame, values=day_options, width=5)
                day_combo.set(get_day)
                day_combo.grid(row=3, column=1, padx=(50, 0))

                # Year
                year_options = ["2024", "2025", "2026"]
                year_combo = ttk.Combobox(frame, values=year_options, width=7)
                year_combo.set(get_year)
                year_combo.grid(row=3, column=1, padx=(100, 0), sticky="e")

                tk.Label(frame, text="Student ID", font=("Arial", 10), bg="#e0e0e0").grid(row=1, column=0, padx=5, pady=5)
                tk.Label(frame, text=get_student_ID).grid(row=1, column=1, padx=5)

                # Table
                global table_frame
                table_frame = tk.Frame(root)
                table_frame.pack(pady=10)

                global tree
                tree = ttk.Treeview(table_frame, columns=("Item", "QTY"), show="headings", height=8)
                tree.heading("Item", text="Item",anchor="center")
                tree.column("# 1", anchor="center")
                tree.heading("QTY", text="QTY",anchor="center")
                tree.column("# 2", anchor="center")
                for item in get_borrowed_data:
                    tree.insert('','end',text=item,values=(item,'1'))
                    tree.pack()
                    def on_item_selected(event):
                        selected_item = tree.focus()
                        if not selected_item:
                            return

                        item_data = tree.item(selected_item)['values']
                        item_name = item_data[0] if item_data else ""

                        # Create Combobox below the tree
                        if hasattr(on_item_selected, "combo"):
                            on_item_selected.combo.destroy()

                        combo_values = ["Basketball", "Shuttle cock", "Tennis Racket", "Ping pong ball",
                        "Tennis Ball", "Table tennis racket", "Badminton Racket", "Net"]
                        on_item_selected.combo = ttk.Combobox(table_frame, values=combo_values)
                        on_item_selected.combo.set(item_name)
                        on_item_selected.combo.pack()

                        def update_item(event):
                            new_value = on_item_selected.combo.get()
                            tree.item(selected_item, values=(new_value, 1))  # assumes qty is always 1
                            on_item_selected.combo.destroy()

                        on_item_selected.combo.bind("<<ComboboxSelected>>", update_item)
                    global add_item_btn
                    add_item_btn = tk.Button(root, text="Add Item", command=show_add_item_combobox)
                    add_item_btn.pack(pady=5)

                    tree.bind("<<TreeviewSelect>>", on_item_selected)
    
    # Next Label
    next_button = tk.Label(root, text="Next", font=("Arial", 10, "underline"), fg="blue", bg="#e0e0e0", cursor="hand2")
    next_button.pack()

    def cancel_appointment():
        selected_id = unique_ID_combo.get()
        if selected_id in history_data:
            del history_data[selected_id]
            del manage_data[selected_id]
            go_back()

    def save_changes():
        selected_id = unique_ID_combo.get()
        if selected_id in history_data:
            updated_items = []
            for row in tree.get_children():
                item_name, qty = tree.item(row)["values"]
                updated_items.append(item_name)

            updated_time = time_combo.get()
            updated_day = day_combo.get()
            updated_month = month_combo.get()
            updated_year = year_combo.get()

            history_data[selected_id]["borrowed_data"] = updated_items
            history_data[selected_id]["Time"] = updated_time
            history_data[selected_id]["Day"] = updated_day
            history_data[selected_id]["Month"] = updated_month
            history_data[selected_id]["Year"] = updated_year

            unsaved_items.clear()  # clear temporary items after saving
            go_back()

    def go_back():
        from admin_menu import admin_menu_frame
        hide_everything()
        admin_menu_frame(root)
    
    def show_add_item_combobox():
        # Frame to hold combobox and confirm button
        global add_frame
        add_frame = tk.Frame(root, bg="#e0e0e0")
        add_frame.pack(pady=5)

        tk.Label(add_frame, text="Select item to add:", font=("Arial", 10), bg="#e0e0e0").pack(side="left")
        global item_combo
        item_choices = ["Basketball", "Shuttle cock", "Tennis Racket", "Ping pong ball",
                        "Tennis Ball", "Table tennis racket", "Badminton Racket", "Net"]
        item_combo = ttk.Combobox(add_frame, values=item_choices)
        item_combo.pack(side="left", padx=5)

        def confirm_add_item():
            selected_item = item_combo.get()
            if selected_item:
                unsaved_items.append(selected_item)
                tree.insert('', 'end', values=(selected_item, '1'))
                add_frame.destroy()  # Remove add combobox after adding
            else:
                tk.messagebox.showwarning("No Item", "Please select an item.")

        tk.Button(add_frame, text="Confirm", command=confirm_add_item).pack(side="left")


    btn_frame = tk.Frame(root, bg="#e0e0e0")
    btn_frame.pack(pady=15)

    cancel_button = tk.Button(btn_frame, text="Cancel appointment", command=cancel_appointment)
    cancel_button.grid(row=0, column=0, padx=10)
    save_button = tk.Button(btn_frame, text="Save Changes", command=save_changes)
    save_button.grid(row=0, column=1, padx=10)
    back_button = tk.Button(header, text="← Back", command=go_back,
                            bg="#1b1f3b", fg="white", font=("Arial", 10, "bold"))
    back_button.pack(anchor="w", padx=10, pady=(10, 0))
