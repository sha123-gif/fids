'''rotation backup 
import tkinter as tk
from tkinter import ttk
import itertools
import mysql.connector

# Sample data
data = [("Item 1", "Value 1"),
        ("Item 2", "Value 2"),
        ("Item 3", "Value 3"),
        ("Item 4", "Value 4")]

def rotate_data():
    global data
    data = data[-1:] + data[:-1]  # Rotate the data by moving the last item to the beginning

    # Clear the Treeview
    treeview.delete(*treeview.get_children())

    # Insert the data into the Treeview
    for item in data:
        treeview.insert("", "end", values=item)

    # Schedule the next rotation
    root.after(1000, rotate_data)  # 1000ms (1 second) delay

root = tk.Tk()
root.title("Rotating Treeview")

# Create a Treeview widget
treeview = ttk.Treeview(root, columns=("Item", "Value"), show="headings")

# Define column headings
treeview.heading("Item", text="Item")
treeview.heading("Value", text="Value")

# Insert the initial data into the Treeview
for item in data:
    treeview.insert("", "end", values=item)

# Start the rotation animation
root.after(1000, rotate_data)  # Start the rotation after 1 second

# Pack the Treeview
treeview.pack()

root.mainloop()
'''
