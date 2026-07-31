#import mysql.connector
from tkinter import *
from tkinter import messagebox

# MySQL Database setup
# conn = mysql.connector.connect(
#     host="localhost",
#     user="your_username",  # Replace with your MySQL username
#     password="your_password",  # Replace with your MySQL password
#     database="college_events_db"  # Replace with your database name
# )

# cursor = conn.cursor()

# # Create tables if they don't exist
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS events (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         name VARCHAR(255),
#         date VARCHAR(50),
#         venue VARCHAR(255)
#     )
# ''')

# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS registrations (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         name VARCHAR(255),
#         event_id INT,
#         feedback TEXT,
#         FOREIGN KEY (event_id) REFERENCES events(id)
#     )
# ''')

# conn.commit()

# GUI setup
root = Tk()
root.title("College Event Management")
root.geometry('600x400')

def add_event():
    event_name = event_name_entry.get()
    event_date = event_date_entry.get()
    event_venue = event_venue_entry.get()

    if event_name and event_date and event_venue:
        # cursor.execute("INSERT INTO events (name, date, venue) VALUES (%s, %s, %s)", (event_name, event_date, event_venue))
        # conn.commit()
        messagebox.showinfo("Success", "Event added successfully!")
        event_name_entry.delete(0, END)
        event_date_entry.delete(0, END)
        event_venue_entry.delete(0, END)
        load_events()
    else:
        messagebox.showerror("Error", "All fields are required!")

def load_events():
    events_listbox.delete(0, END)
    # cursor.execute("SELECT id, name, date, venue FROM events")
    # events = cursor.fetchall()
    # for event in events:
    #     events_listbox.insert(END, f"{event[0]} - {event[1]} ({event[2]} at {event[3]})")

def register_for_event():
    selected_event = events_listbox.get(ACTIVE)
    if selected_event:
        event_id = selected_event.split(' ')[0]
        registrant_name = registrant_name_entry.get()
        if registrant_name:
            # cursor.execute("INSERT INTO registrations (name, event_id) VALUES (%s, %s)", (registrant_name, event_id))
            # conn.commit()
            messagebox.showinfo("Success", "Registered successfully!")
            registrant_name_entry.delete(0, END)
        else:
            messagebox.showerror("Error", "Please enter your name to register.")
    else:
        messagebox.showerror("Error", "Please select an event to register.")

def give_feedback():
    selected_event = events_listbox.get(ACTIVE)
    if selected_event:
        event_id = selected_event.split(' ')[0]
        feedback = feedback_entry.get()
        if feedback:
            # cursor.execute("UPDATE registrations SET feedback = %s WHERE event_id = %s AND name = %s", (feedback, event_id, registrant_name_entry.get()))
            # conn.commit()
            messagebox.showinfo("Success", "Feedback submitted!")
            feedback_entry.delete(0, END)
        else:
            messagebox.showerror("Error", "Please enter feedback.")
    else:
        messagebox.showerror("Error", "Please select an event to provide feedback.")

# Widgets for adding an event
Label(root, text="Add Event").grid(row=0, column=0, columnspan=2)
Label(root, text="Event Name").grid(row=1, column=0)
event_name_entry = Entry(root)
event_name_entry.grid(row=1, column=1)

Label(root, text="Event Date").grid(row=2, column=0)
event_date_entry = Entry(root)
event_date_entry.grid(row=2, column=1)

Label(root, text="Event Venue").grid(row=3, column=0)
event_venue_entry = Entry(root)
event_venue_entry.grid(row=3, column=1)

Button(root, text="Add Event", command=add_event).grid(row=4, column=1)

# List of events
Label(root, text="Events").grid(row=5, column=0, columnspan=2)
events_listbox = Listbox(root, width=50)
events_listbox.grid(row=6, column=0, columnspan=2)

# Widgets for registering for an event
Label(root, text="Register for Event").grid(row=7, column=0, columnspan=2)
Label(root, text="Your Name").grid(row=8, column=0)
registrant_name_entry = Entry(root)
registrant_name_entry.grid(row=8, column=1)
Button(root, text="Register", command=register_for_event).grid(row=9, column=1)

# Widgets for providing feedback
Label(root, text="Give Feedback").grid(row=10, column=0, columnspan=2)
Label(root, text="Feedback").grid(row=11, column=0)
feedback_entry = Entry(root)
feedback_entry.grid(row=11, column=1)
Button(root, text="Submit Feedback", command=give_feedback).grid(row=12, column=1)

load_events()

root.mainloop()
