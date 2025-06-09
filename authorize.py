import tkinter as tk
from tkinter import messagebox  

def authorize_frame(root):
    frames = {}
    row_widgets = []


    appointments_data = []
        

    def show_frame(name):
        for frame in frames.values():
            frame.pack_forget()
        frames[name].pack(fill="both", expand=True)

    def main_frame():
        def back_action():
            from admin_menu import admin_menu_frame
            hide_everything()
            admin_menu_frame(root)


        def hide_everything():
            header_frame.pack_forget()
            frame.pack_forget()

        frame = tk.Frame(root, bg="#d9d9d9")
        frames['main'] = frame

        tk.Button(frame, text="← Back", command=back_action, font=("Arial", 10)).pack(anchor="w", padx=10, pady=(10, 0))
        tk.Label(frame, text="Authorize Appointments", bg="white", font=("Arial", 14, "bold")).pack(pady=10)

        header_frame = tk.Frame(frame, bg="#cccccc")
        header_frame.pack(fill="x", padx=20, pady=(0, 5))
        tk.Label(header_frame, text="Date", width=15, font=("Arial", 11, "bold"), bg="#cccccc").pack(side="left")
        tk.Label(header_frame, text="Student ID", width=15, font=("Arial", 11, "bold"), bg="#cccccc").pack(side="left")
        tk.Label(header_frame, text="Time", width=15, font=("Arial", 11, "bold"), bg="#cccccc").pack(side="left")
        tk.Label(header_frame, text="Action", width=10, font=("Arial", 11, "bold"), bg="#cccccc").pack(side="left")
        tk.Label(header_frame, text="Date Sent", width=10, font=("Arial", 11, "bold"), bg="#cccccc").pack(side="left")

        for date, student_id, time in appointments_data:
            row_frame = tk.Frame(frame, bg="#d9d9d9", bd=1, relief="solid")
            row_frame.pack(pady=5, padx=20, fill="x")

            tk.Label(row_frame, text=date, width=15, font=("Arial", 11), bg="#d9d9d9").pack(side="left")
            tk.Label(row_frame, text=student_id, width=15, font=("Arial", 11), bg="#d9d9d9").pack(side="left")
            tk.Label(row_frame, text=time, width=15, font=("Arial", 11), bg="#d9d9d9").pack(side="left")

            btn_frame = tk.Frame(row_frame, bg="#d9d9d9")
            btn_frame.pack(side="left")

            appt_str = f"{date}-{student_id} Scheduled for {time}"
            tk.Button(btn_frame, text="✅", font=("Arial", 12), command=lambda a=(date, student_id, time), rf=row_frame: approve(a, rf)).pack(side="left", padx=5)
            tk.Button(btn_frame, text="❌", font=("Arial", 12), command=lambda a=appt_str, rf=row_frame: cancel_frame(a, rf)).pack(side="left", padx=5)

            row_widgets.append(row_frame)

    def approve(appointment, row_frame):
        from history import history_frame
        row_frame.pack_forget()
        date, student_id, time = appointment
        #history.add_to_history(student_id, "Sports Item", date, "1")
        messagebox.showinfo("Approved", "Appointment approved. (Added to history)")

    def cancel_frame(appointment, row_frame):
        if 'cancel' not in frames:
            frame = tk.Frame(root, bg="#d9d9d9")
            frames['cancel'] = frame

            tk.Label(frame, text="Cancelled Appointments?", font=("Arial", 14, "bold"), bg="white").pack(pady=10)
            tk.Label(frame, text="Are you sure you want to cancel?", font=("Arial", 12, "bold"), bg="#d9d9d9").pack(pady=5)
            tk.Label(frame, text="Reason:", font=("Arial", 11), bg="#d9d9d9").pack()

            reason_text = tk.Text(frame, height=5, width=40)
            reason_text.pack(pady=5)

            button_frame = tk.Frame(frame, bg="#d9d9d9")
            button_frame.pack(pady=10)

            tk.Button(button_frame, text="Cancel", command=lambda: show_frame('main'), bg="white", font=("Arial", 10, "bold")).pack(side="left", padx=10)

            def confirm():
                reason = reason_text.get("1.0", "end").strip()
                if not reason:
                    messagebox.showwarning("Reason Needed", "Please provide a reason.")
                else:
                    row_frame.pack_forget()
                    messagebox.showinfo("Cancelled", f"Appointment cancelled.\nReason: {reason}")
                    show_frame('main')

            tk.Button(button_frame, text="Confirm", command=confirm, bg="white", font=("Arial", 10, "bold")).pack(side="left", padx=10)
        show_frame('cancel')

    main_frame()
    show_frame('main')
