import tkinter as tk
def main_menu_frame(window):

    main_frame = tk.Frame(window, bg="lightgray")
    main_frame.place(relx=0.5, rely=0.5, anchor="center", width=650, height=300)

    header = tk.Label(window, text="Good day, RAMs!", bg="#7e8dbc", fg="white", font=("Arial", 24, "bold"))
    header.place(relx=0.5, y = 200, anchor="center", width=650, height=50)

    admin_button = tk.Button(main_frame, text="ADMIN", font=("Arial", 16), width=20, height=2)
    student_button = tk.Button(main_frame, text="STUDENT", font=("Arial", 16), width=20, height=2)

    admin_button.place(relx=0.5, y = 100, anchor="center")
    student_button.place(relx=0.5, y = 200, anchor="center")

    def show_admin():
        from admin_login import admin_login_frame
        main_frame.place_forget()
        header.place_forget()
        admin_login_frame(window)

    def show_student():
        from Student import student_main_frame
        header.place_forget()
        main_frame.place_forget()
        student_main_frame(window)

    admin_button.config(command=show_admin)
    student_button.config(command=show_student)

