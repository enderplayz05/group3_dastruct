import tkinter as tk
from tkinter import messagebox
def inventory_frame(root):
    # Current page tracker
    current_page = 1

    def go_back():
        root.destroy()

    def next_page():
        global current_page
        if current_page == 1:
            show_page_2()
        else:
            messagebox.showinfo("Info", "This is the last page")

    def previous_page():
        global current_page
        if current_page == 2:
            show_page_1()
        else:
            go_back()

    def show_page_1():
        global current_page
        current_page = 1
        
        # Clear existing table
        for widget in table_frame.winfo_children():
            widget.destroy()
        
        # Table data for page 1
        inventory_data = [
            ("golf club", "4"),
            ("golf ball", "2"),
            ("Rugby", "4"),
            ("soccer", "4"),
            ("Volleyball", "4"),
            ("speaker", "4"),
            ("Bola ni guzman", "4")
        ]
        
        create_table(inventory_data)

    def show_page_2():
        global current_page
        current_page = 2
        
        # Clear existing table
        for widget in table_frame.winfo_children():
            widget.destroy()
        
        # Table data for page 2 (gymnasium equipment)
        inventory_data = [
            ("Badminton Racket", "12"),
            ("Basketball", "8"),
            ("Shuttlecock", "25"),
            ("Tennis Ball", "15"),
            ("Exercise Mat", "10"),
            ("Dumbbell", "20"),
            ("Jump Rope", "18")
        ]
        
        create_table(inventory_data)

    def create_table(data):
        # Header row
        header_frame = tk.Frame(table_frame, bg="#E6B84A", relief="solid", bd=2)
        header_frame.pack(fill="x")
        
        item_header = tk.Label(header_frame, text="Item", font=("Arial", 14, "bold"), 
                            bg="#E6B84A", fg="black", width=30, height=2, relief="solid", bd=1)
        item_header.pack(side="left", fill="both", expand=True)
        
        qty_header = tk.Label(header_frame, text="QTY", font=("Arial", 14, "bold"), 
                            bg="#E6B84A", fg="black", width=15, height=2, relief="solid", bd=1)
        qty_header.pack(side="right", fill="both", expand=True)
        
        # Data rows
        for item, qty in data:
            row_frame = tk.Frame(table_frame, bg="white", relief="solid", bd=1)
            row_frame.pack(fill="x")
            
            item_label = tk.Label(row_frame, text=item, font=("Arial", 12), 
                                bg="white", fg="black", width=30, height=2, relief="solid", bd=1)
            item_label.pack(side="left", fill="both", expand=True)
            
            qty_label = tk.Label(row_frame, text=qty, font=("Arial", 12), 
                            bg="white", fg="black", width=15, height=2, relief="solid", bd=1)
            qty_label.pack(side="right", fill="both", expand=True)

    def create_inventory_gui():
        global root, table_frame
        
        # Create main frame
        main_frame = tk.Frame(root, bg="#2E4BC6")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Header frame with yellow background
        header_frame = tk.Frame(main_frame, bg="#E6B84A", height=80)
        header_frame.pack(fill="x", pady=(0, 20))
        header_frame.pack_propagate(False)
        
        # Header text
        header_label = tk.Label(
            header_frame, 
            text="VIEW INVENTORY",
            font=("Arial", 24, "bold"),
            bg="#E6B84A",
            fg="white"
        )
        header_label.pack(expand=True)
        
        # Content frame with light gray background
        content_frame = tk.Frame(main_frame, bg="#D3D3D3")
        content_frame.pack(fill="both", expand=True)
        
        # Back button (circular with arrow) - top left
        back_btn = tk.Button(
            content_frame,
            text="←",
            font=("Arial", 16, "bold"),
            bg="black",
            fg="white",
            width=3,
            height=1,
            relief="flat",
            command=go_back
        )
        back_btn.place(x=20, y=20)
        
        # Create table frame
        table_frame = tk.Frame(content_frame, bg="#D3D3D3")
        table_frame.pack(expand=True, pady=80)
        
        # Initialize with page 1
        show_page_1()
        
        # Bottom buttons
        button_frame = tk.Frame(content_frame, bg="#D3D3D3")
        button_frame.pack(side="bottom", fill="x", pady=20)
        
        # Back button (bottom left)
        back_bottom_btn = tk.Button(
            button_frame,
            text="BACK",
            font=("Arial", 12, "bold"),
            bg="white",
            fg="black",
            width=10,
            height=2,
            relief="flat",
            command=previous_page
        )
        back_bottom_btn.pack(side="left", padx=20)
        
        # Next button (bottom right)
        next_btn = tk.Button(
            button_frame,
            text="NEXT",
            font=("Arial", 12, "bold"),
            bg="white",
            fg="black",
            width=10,
            height=2,
            relief="flat",
            command=next_page
        )
        next_btn.pack(side="right", padx=20)

    # Run the inventory GUI
    create_inventory_gui()