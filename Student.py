import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
def student_main_frame(root):
    def view_inventory():
        try:
            subprocess.run([sys.executable, "View_Inventory.py"])
        except FileNotFoundError:
            messagebox.showerror("Error", "View_Inventory.py file not found!")
        except Exception as e:
            messagebox.showerror("Error", f"Could not open inventory: {str(e)}")

    def book_appointment():
        messagebox.showinfo("Book Appointment", "Opening appointment booking...")
        # Add your appointment booking logic here

    def hide_everything():
        main_frame.pack_forget()
        header_frame.pack_forget()
        content_frame.pack_forget()
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
        text="What do you want to do?",
        font=("Arial", 24, "bold"),
        bg="#E6B84A",
        fg="white"
    )
    header_label.pack(expand=True)
    
    # Content frame with light gray background
    content_frame = tk.Frame(main_frame, bg="#D3D3D3")
    content_frame.pack(fill="both", expand=True)
    
    # Button container
    button_container = tk.Frame(content_frame, bg="#D3D3D3")
    button_container.pack(expand=True)
    
    # View Inventory Button
    inventory_btn = tk.Button(
        button_container,
        text="View Inventory",
        font=("Arial", 16, "bold"),
        bg="white",
        fg="black",
        width=20,
        height=2,
        relief="flat",
        command=view_inventory
    )
    inventory_btn.pack(pady=20)
    
    # Book Appointment Button
    appointment_btn = tk.Button(
        button_container,
        text="Book an Appointment",
        font=("Arial", 16, "bold"),
        bg="white",
        fg="black",
        width=20,
        height=2,
        relief="flat",
        command=book_appointment
    )
    appointment_btn.pack(pady=20)