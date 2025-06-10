import tkinter as tk
from tkinter import messagebox 
import win32com.client as win32

appointments_data = []

def send_outlook_email(to_email, subject, body):
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)  # 0: Mail item

    mail.To = to_email
    mail.Subject = subject
    mail.Body = body

    # Uncomment to display the mail before sending (for debugging):
    # mail.Display()
    
    mail.Send()
    print("Email sent successfully.")

def add_appointments(new_data):
        appointments_data.append(new_data)
        print(appointments_data)

def authorize_frame(root):

    frames = {}
    row_widgets = [] 

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
        tk.Label(header_frame, text="Date Sent", width=10, font=("Arial", 11, "bold"), bg="#cccccc").pack(side="left",padx=2)

        def render_appointments(container):
            for appointment in appointments_data:
                student_id = appointment['Student_ID']
                time = appointment['Time']
                date_sent = appointment['Date_sent']
                date = f"{appointment['Month']}/{appointment['Day']}/{appointment['Year']}"

                row_frame = tk.Frame(container, bg="#d9d9d9", bd=1, relief="solid")
                row_frame.pack(pady=5, padx=20, fill="x")

                tk.Label(row_frame, text=date, width=15, font=("Arial", 11), bg="#d9d9d9").grid(row=0, column=0, padx=2)
                tk.Label(row_frame, text=student_id, width=15, font=("Arial", 11), bg="#d9d9d9").grid(row=0, column=1, padx=2)
                tk.Label(row_frame, text=time, width=15, font=("Arial", 11), bg="#d9d9d9").grid(row=0, column=2, padx=2)
                tk.Label(row_frame, text=date_sent, width=15, font=("Arial", 11), bg="#d9d9d9").grid(row=0, column=3, padx=2)

                btn_frame = tk.Frame(row_frame, bg="#d9d9d9")
                btn_frame.grid(row=0, column=3, padx=2)

                appt_str = f"{date}-{student_id} Scheduled for {time}"
                idx = appointments_data.index(appointment)
                tk.Button(btn_frame, text="✅", font=("Arial", 12), command=lambda a=(date, student_id, time), rf=row_frame, i=idx: approve(a, rf, i)).pack(side="left", padx=2)
                tk.Button(btn_frame, text="❌", font=("Arial", 12), command=lambda a=appt_str, rf=row_frame, i=idx: cancel_frame(a, rf, i)).pack(side="left", padx=2)

                tk.Label(row_frame, text=date_sent, width=15, font=("Arial", 11), bg="#d9d9d9").grid(row=0, column=4, padx=2)

                row_widgets.append(row_frame)
        appointments_container = tk.Frame(frame, bg="#d9d9d9")
        appointments_container.pack(fill="both", expand=True)

        render_appointments(appointments_container)

    def approve(appointment, row_frame, index):
        if index != 0:
            messagebox.showwarning("Action Not Allowed", "Please approve the top appointment first.")
        else:
            from history import add_to_history
            date, student_id, time = appointment
            add_to_history(appointments_data[0])
            send_outlook_email(
                appointments_data[0]['student_email'],
                "GYM EQUIPMENT APPOINTMENT",
                f"Good day, your appointment of {date} and {time} is approved")
            from history import add_to_history
            appointments_data.pop(0)  # Remove from data
            row_frame.destroy()
            messagebox.showinfo("Approved", "Appointment approved. (Added to history)")
            main_frame()     # Refresh list

    def cancel_frame(appointment, row_frame, index):
        if index != 0:
            messagebox.showwarning("Action Not Allowed", "Please approve or cancel the top appointment first.")
        else:
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
                        confirm_processing = tk.Label(frame, text="Please wait for it to process", font=("Arial", 11), bg="#d9d9d9")
                        date = f"{appointments_data[0]['Month']}/{appointments_data[0]['Day']}/{appointments_data[0]['Year']}"
                        messagebox.showinfo("Cancelled", f"Appointment cancelled.\nReason: {reason}")
                        send_outlook_email(
                        appointments_data[0]['student_email'],
                        "GYM EQUIPMENT APPOINTMENT",
                        f"Good day, your appointment of {date} and {appointments_data[0]['Time']} is cancelled\nreason of which is\n {reason}")
                        confirm_processing.pack_forget()
                        appointments_data.pop(0)  # Remove the canceled appointment
                        row_frame.destroy()
                        main_frame()      # Refresh list
                        show_frame('main')
                tk.Button(button_frame, text="Confirm", command=confirm, bg="white", font=("Arial", 10, "bold")).pack(side="left", padx=10)
                
            show_frame('cancel')

    main_frame()
    show_frame('main')
