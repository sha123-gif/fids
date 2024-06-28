import subprocess
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import mysql.connector

#setting the appearence for database visitor users
ctk.set_appearance_mode("light")

#default color theme for upper ribbon of window 
ctk.set_default_color_theme("blue")

#creating an object for acessing the main window layout along with the use of customtkinter 
app=ctk.CTk()

#deciding the login interface for adminstrator login 
app.geometry("210x210")
app.title('User Login')

#defining the trials value for future use and its increment procedure 
trials=0
#defining the relation for connection of user to the database
con=mysql.connector.connect(host="localhost",user="root",password="",database="new_user_infromation")
cursor=con.cursor()
#defining a function for submittting the passcode in user login window 
def Passcode_check():
    global cursor
    global trials
    passcode_verify=passcode_entry.get()
    passcode_entry.delete(0,ctk.END)
    cursor.execute("select * from user_data where Passcode='"+passcode_verify+"'")
    db_result=cursor.fetchone()
    if (db_result==None):
        trials=trials+1
        if (trials!=3):
            messagebox.showerror("Login Status",f"Invalid login {3-trials} attempts left")
        else:
            app.destroy()
    else:
        messagebox.showinfo("Login Status","Succesful Login")
        trials=0
        def execute_file_python(file_path):
            try:
                completed_process = subprocess.run(['python', file_path], capture_output=True, text=True)
                if completed_process.returncode == 0:
                    print("Execution successful.")
                    print("Output:")
                    print(completed_process.stdout)
                else:
                    print(f"Error: Failed to execute '{file_path}'.")
                    print("Error output:")
                    print(completed_process.stderr)
            except FileNotFoundError:
                print(f"Error: The file '{file_path}' does not exist.")
        file_path="C:\\Users\\hp\\Desktop\\java folder\\FIDS FOLDER\\audio file.py"
        execute_file_python(file_path)
#creating a frame for accessing the details of logging operation and matching it with the database users 
frame=ctk.CTkFrame(master=app)
frame.pack(pady=10,padx=10,fill="both",expand=True)

#creating a label for normal users login for database readers login 
label=ctk.CTkLabel(master=frame,text="User Login",font=("BankGothic Md BT",25),text_color="Red")
label.pack(pady=8,padx=8)

#creating a label for passcode
label=ctk.CTkLabel(master=frame,text="Passcode")
label.pack(pady=8,padx=8)

#creating an entry for passcode 
passcode_entry=ctk.CTkEntry(master=frame,placeholder_text="Passcode")
passcode_entry.pack(pady=8,padx=8)

#creating a button for submitting the records of passcode 
button=ctk.CTkButton(master=frame,text="Submit",fg_color="black",corner_radius=10,command=Passcode_check)
button.pack(pady=8,padx=8)
app.mainloop()