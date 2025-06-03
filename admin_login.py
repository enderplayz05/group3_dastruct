import tkinter as tk
from tkinter import messagebox
from admin_menu import admin_menu_frame

def  admin_login_frame(root):
    frame_index = 0
    loading_frames = [
    "Authenticating",
    "Authenticating.",
    "Authenticating..",
    "Authenticating...",
    "Access Verified.",
    "Welcome, Administrator"
    ]

    def arrow_button_on_enter(event):
        back_arrow_button.config(
            bg='#bbbbbb'
            )
    def arrow_button_on_leave(event):
        back_arrow_button.config(
            bg='#2F2F32'
            )

    def login_button_on_enter(event):
        login_button.config(
            bg='#bbbbbb'
            )

    def login_button_on_leave(event):
        login_button.config(
            bg='white'
            )

    def back_action():
        print("This will be when press, goes to main menu")

    def hide_everything():
        content_frame.place_forget()
        header_frame.place_forget()

    def check_password():
        correct_password = "admin123"
        entered_password = password_entry.get()

        if entered_password == correct_password:
            message_label.config(
                text="Login Succesful!", 
                fg='green'
                )
            start_text_animation()
            password_entry.delete(0, 'end')

        else:
            message_label.config(text="Incorrect password. Try again.", fg='red')
            password_entry.delete(0, 'end')

    content_frame = tk.Frame(root, bg='#dcdcdc')
    content_frame.place(
        relx=0.5, 
        rely=0.4, 
        anchor='center', 
        width=650, 
        height=300)

    header_frame = tk.Frame(root, 
        bg='#2F2F32', 
        width=650, 
        height=50
        )
    header_frame.place(relx=0.5, 
        y=145,
        anchor="center"
        )

    password_label = tk.Label(content_frame, 
        text="Password", 
        bg='#dcdcdc', 
        fg='black', 
        font=('Arial', 14, 'bold'))
    password_label.place(
        relx=0.5, 
        y=90, 
        anchor='center'
        )

    password_entry = tk.Entry(
        content_frame, 
        show='*', 
        font=('Arial', 14), 
        width=30
        )
    password_entry.place(
        relx=0.5, 
        y= 120, 
        anchor='center'
        )

    message_label = tk.Label(content_frame, 
        text="", 
        bg='#dcdcdc', 
        fg='red', 
        font=('Arial', 12, 'italic'))
    message_label.place(relx=0.5, 
        y=165, 
        anchor='center')

    back_arrow_button = tk.Button(
        header_frame, 
        text='⬅', 
        bg='#2F2F32', 
        font=('Arial', 20), 
        borderwidth=0,
        command=back_action
        )
    
    back_arrow_button.place(
        relx=0.08,
        anchor='ne'
        )

    back_arrow_button.bind(
        "<Enter>",
        arrow_button_on_enter
        )
    
    back_arrow_button.bind(
        "<Leave>",
        arrow_button_on_leave 
        )

    title = tk.Label(header_frame, 
        text="Admin Login", 
        bg='#2F2F32', 
        fg='white', 
        font=('Arial', 20, 'bold'))
    title.place(relx=0.5,
        rely=0.5,
        anchor='center'
        )

    login_button = tk.Button(content_frame, 
        text="Login", 
        font=('Arial', 12), 
        bg='white', 
        fg='black', 
        width=10, 
        command=check_password
        )
    
    login_button.place(
        relx=0.5, 
        y=240, 
        anchor='center'
        )

    login_button.bind(
        "<Enter>", 
        login_button_on_enter
        )
    
    login_button.bind(
        "<Leave>", 
        login_button_on_leave
        )

    def start_text_animation():
        global frame_index
        frame_index = 0
        animate_text()

    def animate_text():
        global frame_index
        message_label.config(text=loading_frames[frame_index])
        frame_index += 1
        if frame_index < len(loading_frames):
            root.after(500, animate_text)  # ~1.2 sec total
        else:
            root.after(750,go_to_admin_admin_menu)

    def go_to_admin_admin_menu():
        hide_everything()
        admin_menu_frame(root)



