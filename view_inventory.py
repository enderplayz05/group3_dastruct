import tkinter as tk
from tkinter import ttk

current_category = 0
categories = [
    {
        "name": "General Sports",
        "items": [
            {"name": "Volleyball", "qty": 4},
            {"name": "Tennis Racket", "qty": 2},
            {"name": "Tennis ball", "qty": 4},
            {"name": "Badminton Racket", "qty": 4},
            {"name": "Shuttle cock", "qty": 4},
            {"name": "Ping pong ball", "qty": 4},
            {"name": "Table tennis racket", "qty": 4}
        ]
    },
    {
        "name": "Basketball Equipment",
        "items": [
            {"name": "Basketball", "qty": 8},
            {"name": "Basketball Hoop", "qty": 2},
            {"name": "Basketball Shoes", "qty": 6},
            {"name": "Basketball Jersey", "qty": 12},
            {"name": "Basketball Shorts", "qty": 12},
            {"name": "Water Bottle", "qty": 15},
            {"name": "Towel", "qty": 10}
        ]
    },
    {
        "name": "Badminton Equipment",
        "items": [
            {"name": "Badminton Racket", "qty": 8},
            {"name": "Shuttle cock", "qty": 20},
            {"name": "Badminton Net", "qty": 2},
            {"name": "Badminton Shoes", "qty": 6},
            {"name": "Grip Tape", "qty": 15},
            {"name": "String", "qty": 5},
            {"name": "Badminton Bag", "qty": 4}
        ]
    }
]

def inventory_GUI(root):
# Global variables to track current category

    def create_inventory_table(parent_frame, items):
        # Clear existing widgets
        for widget in parent_frame.winfo_children():
            if widget != back_button and widget != next_button:
                widget.destroy()
        
        # Create main table container
        table_container = tk.Frame(parent_frame, bg='black')
        table_container.place(relx=0.5, rely=0.45, anchor='center', width=602, height=402)
        
        # Create table frame (inner frame with padding for border effect)
        table_frame = tk.Frame(table_container, bg='#e1b757')
        table_frame.place(x=1, y=1, width=600, height=400)
        
        # Header with borders
        header_frame = tk.Frame(table_frame, bg='#e1b757', highlightbackground='black', highlightthickness=1)
        header_frame.place(x=0, y=0, width=600, height=50)
        
        # Vertical line in header
        header_vline = tk.Frame(header_frame, bg='black', width=1)
        header_vline.place(x=299, y=0, width=1, height=50)
        
        item_header = tk.Label(header_frame, text="Item", font=('Arial', 14, 'bold'), 
                            bg='#e1b757', fg='black')
        item_header.place(x=150, y=25, anchor='center')
        
        qty_header = tk.Label(header_frame, text="QTY", font=('Arial', 14, 'bold'), 
                            bg='#e1b757', fg='black')
        qty_header.place(x=450, y=25, anchor='center')
        
        # Items with borders
        item_height = 44
        for i, item in enumerate(items):
            y_pos = 50 + (i * item_height)
            
            # Item row frame with border
            row_frame = tk.Frame(table_frame, bg='white', highlightbackground='black', highlightthickness=1)
            row_frame.place(x=0, y=y_pos, width=600, height=item_height)
            
            # Vertical line in row
            row_vline = tk.Frame(row_frame, bg='black', width=1)
            row_vline.place(x=299, y=0, width=1, height=item_height)
            
            # Item name (left side)
            item_label = tk.Label(row_frame, text=item["name"], font=('Arial', 12), 
                                bg='white', fg='black')
            item_label.place(x=150, y=22, anchor='center')
            
            # Quantity (right side)
            qty_label = tk.Label(row_frame, text=str(item["qty"]), font=('Arial', 12), 
                                bg='white', fg='black')
            qty_label.place(x=450, y=22, anchor='center')

    def hide_everything():
        main_frame.pack_forget()
        title_frame.pack_forget()
        bottom_frame.pack_forget()

    def go_back():
        from Student import student_main_frame
        hide_everything()
        student_main_frame(root)

    def next_category():
        global current_category
        current_category = (current_category + 1) % len(categories)
        update_display()

    def prev_category():
        global current_category
        current_category = (current_category - 1) % len(categories)
        update_display()

    def update_display():
        category = categories[current_category]
        title_label.config(text=f"VIEW INVENTORY - {category['name']}")
        create_inventory_table(main_frame, category["items"])

    # Title frame
    title_frame = tk.Frame(root, bg='#e1b757', height=80)
    title_frame.pack(fill='x', padx=20, pady=(20, 10))
    title_frame.pack_propagate(False)

    title_label = tk.Label(title_frame, text="VIEW INVENTORY - General Sports", 
                        font=('Arial', 20, 'bold'), bg='#e1b757', fg='white')
    title_label.place(relx=0.5, rely=0.5, anchor='center')

    # Main content frame
    main_frame = tk.Frame(root, bg='#4169E1')
    main_frame.pack(fill='both', expand=True, padx=20, pady=10)

    # Back button (circular)
    back_button = tk.Button(main_frame, text="←", font=('Arial', 18, 'bold'), 
                        bg='black', fg='white', width=4, height=2,
                        command=go_back, relief='flat')
    back_button.place(x=30, y=30)

    # Bottom buttons frame
    bottom_frame = tk.Frame(root, bg='#4169E1', height=80)
    bottom_frame.pack(fill='x', padx=20, pady=20)
    bottom_frame.pack_propagate(False)

    # Back button (bottom)
    bottom_back_button = tk.Button(bottom_frame, text="BACK", font=('Arial', 12, 'bold'), 
                                bg='white', fg='black', width=12, height=2,
                                command=prev_category)
    bottom_back_button.place(x=50, rely=0.5, anchor='w')

    # Next button (bottom)
    next_button = tk.Button(bottom_frame, text="NEXT", font=('Arial', 12, 'bold'), 
                        bg='white', fg='black', width=12, height=2,
                        command=next_category)
    next_button.place(x=750, rely=0.5, anchor='e')

    # Initialize display
    update_display()
