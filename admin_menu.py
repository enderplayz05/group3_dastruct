import tkinter as tk

def admin_menu_frame(root):
    # === Header Frame ===
    header_frame = tk.Frame(root, bg="#2e2f34", width=960, height=50)
    header_frame.place(relx=0.5,rely=0.12, anchor='center')

    header_label = tk.Label(header_frame, text="WELCOME BACK ADMIN", fg="white", bg="#2e2f34",font=("Arial", 20, "bold"))
    header_label.place(relx=0.5,rely=0.5, anchor='center')

    # === Content Frame (light gray background) ===
    content_frame = tk.Frame(root, bg="#dbdbdb", width=960, height=540)
    content_frame.place(relx=0.5,rely=0.5, anchor='center')

    # === Button Style ===
    def hide_everything():
        content_frame.place_forget()
        header_frame.place_forget()
    def create_button(text, command):
        return tk.Button(content_frame, text=text, font=("Arial", 14, "bold"),
                        bg="white", fg="black", relief="flat",
                        activebackground="#bbbbbb", command=command,width=20,height=2)

    # === Button Functions ===
    def manage_appointments():
        print("Manage Appointments Clicked")

    def authorize_appointments():
        print("Authorize Appointments Clicked")

    def view_history():
        print("History Clicked")

    def arrow_button_on_enter(event):
        back_arrow_button.config(
            bg='#bbbbbb'
            )
    def arrow_button_on_leave(event):
        back_arrow_button.config(
            bg='#2F2F32'
            )
        
    def back_action():
        from main_menu import main_menu_frame
        hide_everything()
        main_menu_frame(root)
    # === Create Buttons ===
    btn1 = create_button("Manage Appointments", manage_appointments)
    btn2 = create_button("Authorize Appointments", authorize_appointments)
    btn3 = create_button("History", view_history)

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

    
    # === Layout ===
    btn1.place(relx=0.5, y=100, anchor='center')
    btn2.place(relx=0.5, y=200, anchor='center')
    btn3.place(relx=0.5, y=300, anchor='center')
