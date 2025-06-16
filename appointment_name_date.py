import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

#main func
def AppointmentBooking(root):
    student_items_data = []
#add borrowed data to list
    def add_items(new_data):
        for item in new_data:
            student_items_data.append(item)

    # Variables to store user input (id, email, date/time)
    name = tk.StringVar()
    student_id = tk.StringVar()
    selected_month = tk.StringVar()
    selected_day = tk.StringVar()
    selected_year = tk.StringVar()
    selected_time = tk.StringVar()
    student_email = tk.StringVar()
    
    # Create the main container
    main_frame = tk.Frame(root, bg='#2e4399')
    main_frame.pack(expand=True, fill='both', padx=50, pady=50)
    
    # Show the first screen initially, clear before moving 
    
    def clear_screen():
        main_frame.pack_forget()
        header.pack_forget()
    
    
    # Header
    header = tk.Label(main_frame, text="BOOK AN APPOINTMENT", 
                        font=('Arial', 16, 'bold'), bg='#d4a843', fg='white',
                        pady=15)
    header.pack(fill='x', pady=(0, 30))
    
    # Content frame
    content_frame = tk.Frame(main_frame, bg='#e8e8e8', padx=40, pady=40)
    content_frame.pack(fill='both', expand=True)
    
    # Name section
    name_label = tk.Label(content_frame, text="Name", font=('Arial', 12, 'bold'),
                            bg='#e8e8e8', fg='black')
    name_label.pack(anchor='w', pady=(0, 10))
    
    name_entry = tk.Entry(content_frame, textvariable=name, font=('Arial', 11),
                            bg='#c8c8c8', fg='gray', width=40, relief='flat', bd=10)
    name_entry.pack(fill='x', pady=(0, 30))
    name_entry.insert(0, "Enter your name")
    
    # Student ID section
    id_label = tk.Label(content_frame, text="Student ID Number", 
                        font=('Arial', 12, 'bold'), bg='#e8e8e8', fg='black')
    id_label.pack(anchor='w', pady=(0, 10))
    
    id_entry = tk.Entry(content_frame, textvariable=student_id, font=('Arial', 11),
                        bg='#c8c8c8', fg='gray', width=40, relief='flat', bd=10)
    id_entry.pack(fill='x', pady=(0, 50))
    id_entry.insert(0, "Enter your Student ID Number")
    
    student_email_label = tk.Label(content_frame, text="Student Email", font=('Arial', 12, 'bold'),
                            bg='#e8e8e8', fg='black')
    student_email_label.pack(anchor='w', pady=(0, 10))

    student_email_entry = tk.Entry(content_frame, textvariable=student_email, font=('Arial', 11),
                        bg='#c8c8c8', fg='gray', width=40, relief='flat', bd=10)
    student_email_entry.pack(fill='x', pady=(0, 70))
    student_email_entry.insert(0, "Enter your APC email")

    # Handle placeholder text, detect when u click outside
    def on_name_focus_in(event): 
        if name_entry.get() == "Enter your name":
            name_entry.delete(0, tk.END)
            name_entry.config(fg='black')
    
    def on_name_focus_out(event):
        if name_entry.get() == "":
            name_entry.insert(0, "Enter your name")
            name_entry.config(fg='gray')
    
    def on_id_focus_in(event):
        if id_entry.get() == "Enter your Student ID Number":
            id_entry.delete(0, tk.END)
            id_entry.config(fg='black')
    
    def on_id_focus_out(event):
        if id_entry.get() == "":
            id_entry.insert(0, "Enter your Student ID Number")
            id_entry.config(fg='gray')

    def on_student_email_focus_in(event):
        if student_email_entry.get() == "Enter your APC email":
            student_email_entry.delete(0, tk.END)
            student_email_entry.config(fg='black')
    
    def on_student_email_focus_out(event):
        if student_email_entry.get() == "":
            student_email_entry.insert(0, "Enter your APC email")
            student_email_entry.config(fg='gray')
    
    name_entry.bind('<FocusIn>', on_name_focus_in)
    name_entry.bind('<FocusOut>', on_name_focus_out)
    id_entry.bind('<FocusIn>', on_id_focus_in)
    id_entry.bind('<FocusOut>', on_id_focus_out)
    student_email_entry.bind('<FocusIn>', on_student_email_focus_in)
    student_email_entry.bind('<FocusOut>', on_student_email_focus_out)
    
    def go_back_from_first(): #goes back item borrowing screen
        from items import item_GUI
        clear_screen()
        item_GUI(root)

    def go_to_date_screen(): #checks if filled in
        """Navigate to date selection screen"""
        # Validate input first
        name = name_entry.get()
        student_id = id_entry.get()
        
        if name == "Enter your name" or name.strip() == "":
            messagebox.showerror("Error", "Please enter your name")
            return
        
        if student_id == "Enter your Student ID Number" or student_id.strip() == "":
            messagebox.showerror("Error", "Please enter your Student ID Number")
            return
        
        content_frame.pack_forget()
        header.pack_forget()
        back_button.pack_forget()
        next_button.pack_forget()
        show_date_screen()
    # Back button
    back_button = tk.Button(main_frame, text="Back", font=('Arial', 10),
                            bg='white', fg='black', padx=20, pady=5,
                            command=go_back_from_first)
    back_button.pack(side='left', padx=10, pady=10)
    
    # Next button
    next_button = tk.Button(main_frame, text="Next", font=('Arial', 10),
                            bg='white', fg='black', padx=20, pady=5,
                            command=go_to_date_screen)
    next_button.pack(side='right', padx=10, pady=10)
    
    def show_date_screen():
        """Display the date and time selection screen"""
        
        # Header
        header = tk.Label(main_frame, text="BOOK AN APPOINTMENT", 
                         font=('Arial', 16, 'bold'), bg='#d4a843', fg='white',
                         pady=15)
        header.pack(fill='x', pady=(0, 30))
        
        # Content frame
        content_frame = tk.Frame(main_frame, bg='#e8e8e8', padx=40, pady=40)
        content_frame.pack(fill='both', expand=True)
        
        # Create left and right sections
        left_frame = tk.Frame(content_frame, bg='#e8e8e8')
        left_frame.pack(side='left', fill='both', expand=True, padx=(0, 20))
        
        right_frame = tk.Frame(content_frame, bg='#e8e8e8')
        right_frame.pack(side='right', fill='both', expand=True, padx=(20, 0))
        
        # Left side - Date selection
        # Month
        month_label = tk.Label(left_frame, text="Month", font=('Arial', 12, 'bold'),
                              bg='#e8e8e8', fg='black')
        month_label.pack(anchor='w', pady=(0, 10))
        
        month_combo = ttk.Combobox(left_frame, textvariable=selected_month,
                                  values=["January", "February", "March", "April", "May", "June",
                                         "July", "August", "September", "October", "November", "December"],
                                  state="readonly", font=('Arial', 11))
        month_combo.pack(fill='x', pady=(0, 20))
        
        # Day
        day_label = tk.Label(left_frame, text="Day", font=('Arial', 12, 'bold'),
                            bg='#e8e8e8', fg='black')
        day_label.pack(anchor='w', pady=(0, 10))
        
        day_combo = ttk.Combobox(left_frame, textvariable=selected_day,
                                values=[str(i) for i in range(1, 32)],
                                state="readonly", font=('Arial', 11))
        day_combo.pack(fill='x', pady=(0, 20))
        
        # Year
        year_label = tk.Label(left_frame, text="Year", font=('Arial', 12, 'bold'),
                             bg='#e8e8e8', fg='black')
        year_label.pack(anchor='w', pady=(0, 10))
        
        year_combo = ttk.Combobox(left_frame, textvariable=selected_year,
                                 values=["2024", "2025", "2026"],
                                 state="readonly", font=('Arial', 11))
        year_combo.pack(fill='x', pady=(0, 20))
        
        # Right side - Time selection
        time_label = tk.Label(right_frame, text="Time", font=('Arial', 12, 'bold'),
                             bg='#e8e8e8', fg='black')
        time_label.pack(anchor='w', pady=(0, 10))
        
        # Time options with radio buttons
        time_options = [
            "7:30 AM - 9:30 AM",
            "9:30 AM - 11:30 AM", 
            "1:30 PM - 3:30 PM",
            "3:30 PM - 5:30 PM"
        ]
        
        for i, time_option in enumerate(time_options):
            rb = tk.Radiobutton(right_frame, text=time_option, variable=selected_time,
                               value=time_option, font=('Arial', 11), bg='#e8e8e8',
                               fg='black', selectcolor='white')
            rb.pack(anchor='w', pady=5)
            
            # Select the first option by default
            if i == 0:
                selected_time.set(time_option)
        
        # Back button
        back_button = tk.Button(main_frame, text="Back", font=('Arial', 10),
                               bg='white', fg='black', padx=20, pady=5,
                               command=go_to_name_screen)
        back_button.pack(side='left', padx=10, pady=10)
        
        # Next button
        next_button = tk.Button(main_frame, text="submit", font=('Arial', 10),
                               bg='white', fg='black', padx=20, pady=5,
                               command=submit)
        next_button.pack(side='right', padx=10, pady=10)
    
    def submit(): #final confirmation and data handling logic
        go_to_next_screen(student_items_data)
        
    def go_to_date_screen():
        """Navigate to date selection screen"""
        # Validate input first
        name = name.get()
        student_id = student_id.get()
        
        if name == "Enter your name" or name.strip() == "":
            messagebox.showerror("Error", "Please enter your name")
            return
        
        if student_id == "Enter your Student ID Number" or student_id.strip() == "":
            messagebox.showerror("Error", "Please enter your Student ID Number")
            return
        
        show_date_screen()
    #reload screen
    def go_to_name_screen():
        clear_screen()
        AppointmentBooking(root)
        
    #pop up summary
    def go_to_next_screen(student_items_data):
        """Navigate to the next screen (placeholder for future functionality)"""
        # For now, show a confirmation message with the selected details
        message = f"Appointment Details:\n\n"
        message += f"Name: {name.get()}\n"
        message += f"Student ID: {student_id.get()}\n"
        message += f"Date: {selected_month.get()} {selected_day.get()}, {selected_year.get()}\n"
        message += f"Time: {selected_time.get()}\n\n"
        message += f"Borrowed: {student_items_data}\n\n"
    # add items here, save and send to authorize.py
        date_sent_data = datetime.time(datetime.now()) 
        messagebox.showinfo("Appointment Booked", message)
        from authorize import add_appointments
        new_data = {
            'Name':name.get(),
            'Student_ID':student_id.get(),
            'Month':selected_month.get(),
            'Day':selected_day.get(),
            'Year':selected_year.get(),
            'Time':selected_time.get(),
            'Date_sent':date_sent_data.strftime("%H:%M:%S"),
            'borrowed_data':student_items_data,
            'student_email':student_email_entry.get(),
            }
        #clears and load main menu
        add_appointments(new_data)
        from main_menu import main_menu_frame
        clear_screen()
        main_menu_frame(root)
    return add_items


