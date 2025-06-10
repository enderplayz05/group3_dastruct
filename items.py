import tkinter as tk
from tkinter import ttk, messagebox

def item_GUI(root):

    def hide_everything():
        main_frame.pack_forget()
        header_frame.pack_forget()
        item_frame.pack_forget()
    def on_equipment_change(equipment):
        """Handle equipment selection change"""
        selected_equipment[equipment] = checkboxes[equipment].get()
        print(f"{equipment} {'selected' if selected_equipment[equipment] else 'deselected'}")
    def on_back_click():
        """Handle back button click"""
        from Student import student_main_frame
        hide_everything()
        student_main_frame(root)
        # Add your back navigation logic here
        
    def on_confirm_click():
        """Handle confirm button click"""
        selected_items = [eq for eq, selected in selected_equipment.items() if selected]
        if not selected_items:
            messagebox.showwarning("Selection Required", "Please select at least one equipment item.")
            return
        print("Selected equipment:", selected_items)
        # Show confirmation dialog
        message = "Selected Equipment:\n" + "\n".join(f"• {item}" for item in selected_items)
        messagebox.showinfo("Items Confirmated", message)
        hide_everything()
        from appointment_name_date import AppointmentBooking
        add_items = AppointmentBooking(root)
        add_items(selected_items)


    def get_selected_equipment():
        """Return list of selected equipment"""
        return [eq for eq, selected in selected_equipment.items() if selected]
    # Equipment options and their selection states
    equipment_options = [
        "Basketball", "Shuttle cock", "Tennis Racket", "Ping pong ball",
        "Tennis Ball", "Table tennis racket", "Badminton Racket", "Net"
    ]
    
    selected_equipment = {}
    # Initialize other equipment as not selected
    for equipment in equipment_options:
        if equipment not in selected_equipment:
            selected_equipment[equipment] = False

    # Header
    header_frame = tk.Frame(root, bg="#D4AC0D", height=80)  # Yellow header
    header_frame.pack(fill="x", padx=20, pady=(20, 0))
    header_frame.pack_propagate(False)
    header_label = tk.Label(
        header_frame, 
        text="BOOK AN APPOINTMENT",
        font=("Arial", 20, "bold"),
        bg="#D4AC0D",
        fg="white"
    )
    header_label.pack(expand=True)
    # Main content frame
    main_frame = tk.Frame(root, bg="#F5F5F5")  # Light gray background
    main_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))
    # Title
    title_label = tk.Label(
        main_frame,
        text="Choose your Equipment:",
        font=("Arial", 16, "bold"),
        bg="#F5F5F5",
        fg="#333333"
    )
    title_label.pack(pady=(30, 20))
    # Equipment selection frame
    equipment_frame = tk.Frame(main_frame, bg="#F5F5F5")
    equipment_frame.pack(pady=20)
    # Create equipment checkboxes in a 2x4 grid
    checkboxes = {}
    for i, equipment in enumerate(equipment_options):
        row = i // 2
        col = i % 2
        # Frame for each equipment item
        item_frame = tk.Frame(equipment_frame, bg="#F5F5F5")
        item_frame.grid(row=row, column=col, padx=15, pady=10, sticky="w")
        # Checkbox variable
        var = tk.BooleanVar(value=selected_equipment[equipment])
        checkboxes[equipment] = var
        # Checkbox
        checkbox = tk.Checkbutton(
            item_frame,
            variable=var,
            bg="#F5F5F5",
            activebackground="#F5F5F5",
            command=lambda eq=equipment: on_equipment_change(eq)
        )
        checkbox.pack(side="left", padx=(0, 10))
    # Equipment label (styled like a button)
        equipment_label = tk.Label(
            item_frame,
            text=equipment,
            font=("Arial", 11),
            bg="#CCCCCC",
            fg="#333333",
            relief="flat",
            padx=20,
            pady=8,
            width=15
        )
        equipment_label.pack(side="left")
    # Navigation buttons frame
    nav_frame = tk.Frame(main_frame, bg="#F5F5F5")
    nav_frame.pack(side="bottom", fill="x", pady=(40, 20))
    # Back button
    back_button = tk.Button(
        nav_frame,
        text="Back",
        font=("Arial", 12, "bold"),
        bg="#F5F5F5",
        fg="#333333",
        relief="flat",
        cursor="hand2",
        command=on_back_click
    )
    back_button.pack(side="left", padx=20)
    # Confirm button
    confirm_button = tk.Button(
        nav_frame,
        text="Confirm",
        font=("Arial", 12, "bold"),
        bg="#F5F5F5",
        fg="#333333",
        relief="flat",
        cursor="hand2",
        command=on_confirm_click
    )
    confirm_button.pack(side="right", padx=20)
    
 
