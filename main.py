import tkinter as tk
from tkinter import messagebox
import main_menu
root = tk.Tk()
root.title("EAMS")
root.geometry("1920x1080")
root.configure(bg='#1A3B8A')
root.state('zoomed')

main_menu_gui =  main_menu.main_menu_frame(root)
#admin_login_GUI = admin_login.admin_login_frame(root)

root.mainloop()