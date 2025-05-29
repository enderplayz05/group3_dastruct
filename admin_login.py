import tkinter 

standard_font = ("Arial", 12, "bold")

def admin_login():
    password = login_entry.get()
    if password == "admin123":
        hide_login_frame()
        import admin_borrow


def hide_login_frame():
    login_frame.place_forget()
    login_button.place_forget()

root = tkinter.Tk()
root.title("EAMS ADMIN")
root.geometry("1920x720")
root.configure(bg="#00205B")  # APC blue
root.state('zoomed')            # Zoomed means that it goes to windowed fullscreen 

title = tkinter.Label(
    root,
    text='ADMIN LOGIN',
    relief=tkinter.RAISED,
    font=standard_font,
    height=2,              
    width=15, 
    )

title.place(relx = 0.5, rely = 0.05, anchor = tkinter.CENTER)

login_frame = tkinter.Frame(root)
login_password = tkinter.Label(
    login_frame, 
    text='Password',
    font=standard_font
    ).grid(row=0)
login_entry = tkinter.Entry(login_frame)
login_entry.grid(row=0, column=1)

login_button = tkinter.Button(
    root, 
    text="login",
    font=standard_font,
    activebackground="blue", 
    activeforeground="white",
    disabledforeground="gray",
    fg="black",
    command=admin_login,
    )

login_frame.place(relx = 0.5, rely = 0.12, anchor = tkinter.CENTER)
login_button.place(relx = 0.5, rely = 0.2, anchor = tkinter.CENTER)
root.mainloop()
