#importing the required modules for performing the opeartion 

import os
import subprocess
import customtkinter as ctk
from tkinter import END,ttk
from PIL import Image
import tkinter as tk
from tkinter import messagebox
import random 
import mysql.connector

#setting the appearence for administrator users 
ctk.set_appearance_mode("light")

#default color theme for upper ribbon of window 
ctk.set_default_color_theme("blue")

#creating an object for acessing the main window layout along with the use of customtkinter 
app=ctk.CTk()

#deciding the login interface for adminstrator login 
app.geometry("240x340")
app.title('User Login')
trials=0

#defining the passlogin funtion for performing the login opeartion
def pass_login():
    global trials
    pass1=passcode.get()
    code1=code.get()
    passcode.delete(0,ctk.END)
    code.delete(0,ctk.END)
    con=mysql.connector.connect(host="localhost",user="root",password="",database="new_user_infromation")
    cursor=con.cursor()
    cursor.execute("select * from user_data where Passcode='"+pass1+"' and Code='"+code1+"'")
    db_result=cursor.fetchone()
    if (db_result==None):
        trials=trials+1
        if (trials!=3):
            messagebox.showerror("Login Status",f'Invalid Login {3-trials} attempts left')
        else:
            button1.destroy()
            messagebox.showwarning("Login Status",'Restart the Program')
    else:
        messagebox.showinfo("Login Status","Succesful Login")
        app.destroy()
        
        #creating a new window for entering the user_details such as username and password
        app1=ctk.CTk() 
        app1.geometry("350x350")
        app1.title("User Login")
        trials=0
        
        #defining the function for submit button 
        def submit():
            global trials
            user1=username.get()
            pass2=password.get()
            username.delete(0,ctk.END)
            password.delete(0,ctk.END)
            con=mysql.connector.connect(host="localhost",user="root",password="",database="new_user_infromation")
            cursor=con.cursor()
            cursor.execute("select * from user_data where Username='"+user1+"' and Password='"+pass2+"'")
            db_result=cursor.fetchone()
            if (db_result==None):
                trials=trials+1
                if (trials!=3):
                    messagebox.showerror("Login Status",f'Inavlid login {3-trials} attempts left')
                else:
                    app1.destroy()
                    messagebox.showwarning("Login status","Restart the program")
                
            else:
                messagebox.showinfo("Login Status","Succesful Login")
                app1.destroy()
                app2=ctk.CTk()
                app2.geometry("300x300")
                app2.title("Functions Panel")
                
                def flight_update():
                    new_window1=ctk.CTk()
                    new_window1.geometry("300x300")
                    new_window1.title("Verify")
                    global trials
                    
                    # definig a function for checking the insertion code password
                    def check_code():
                        global trials
                        insertion_code=label_entry.get()
                        label_entry.delete(0,ctk.END)
                        if (str(insertion_code)=="1234"):
                            messagebox.showinfo("Insert Status","Login succesful")
                            new_window1.destroy()
                            app3=ctk.CTk()
                            app3.geometry("800x600")
                            app3.title("Fight Details")
                            con=mysql.connector.connect(host="localhost",user="root",password="",database="new_user_infromation")
                            cursor=con.cursor()

                            #display function for dislaying the data in the table in the for of treeview 
                            def displayall():
                                for rows in tv.get_children():
                                    tv.delete(rows)
                                cursor.execute("select * from flight_data")
                                for row in cursor.fetchall():
                                    tv.insert("",END,values=row)
                                tv.after(1000,displayall)  
                                
                            #exit window function 
                            def exit_window():
                                app3.destroy()
                                con.close()
                                
                            #insert record function
                            def insert_record():
                                flight_time=time_entry.get()
                                destination=destination_entry.get()
                                flight_name=flight_name_entry.get()
                                flight_number=flight_number_entry.get()
                                terminal=terminal_values.get()
                                flight_status=flight_status_entry.get()
                                gate=gate_number_entry.get()
                                cursor.execute("select * from flight_data where Flight_number='"+flight_number+"'")
                                db_result=cursor.fetchone()
                                if (db_result==None):
                                    cursor.execute("Insert into flight_data values('"+flight_time+"','"+destination+"','"+flight_name+"','"+flight_number+"','"+terminal+"','"+flight_status+"','"+gate+"')")
                                    cursor.execute("commit")
                                    messagebox.showinfo('Insert Status',"Record Inserted")
                                else:
                                    messagebox.showwarning("Insert Status","Record Already Present")
                                clear_all()
                            #delete record function 
                            def delete_record():
                                flight_number=flight_number_entry.get()
                                gate=gate_number_entry.get()
                                cursor.execute("select * from flight_data where Flight_number='"+flight_number+"'")
                                db_result=cursor.fetchone()
                                if (db_result!=None):
                                    cursor.execute("delete from flight_data where Flight_number='"+flight_number+"'")
                                    cursor.execute("commit")
                                    messagebox.showinfo("Delete Status","Flight Deleted")
                                else:
                                    messagebox.showwarning("Delete Status","Flight Not Exists")
                                clear_all()

                            #update record function 
                            def update_record():
                                flight_time=time_entry.get()
                                destination=destination_entry.get()
                                flight_name=flight_name_entry.get()
                                flight_number=flight_number_entry.get()
                                terminal=terminal_values.get()
                                flight_status=flight_status_entry.get()
                                gate=gate_number_entry.get()
                                cursor.execute("select * from flight_data where Flight_number='"+flight_number+"'")
                                db_result=cursor.fetchone()
                                if (db_result==None):
                                    messagebox.showwarning("Update Status","Flight Not Exists")
                                else:
                                    cursor.execute("update flight_data set Time='"+flight_time+"',Destination='"+destination+"',Flight_name='"+flight_name+"',Flight_number='"+flight_number+"',Terminal='"+terminal+"',Plane_status='"+flight_status+"',Gate='"+gate+"' where Flight_number='"+flight_number+"'")
                                    cursor.execute("commit")
                                    messagebox.showinfo("Update Status","Flight Updated")
                                clear_all()
                                
                            #creating a clear button for removing the details if filled uneccessary
                            def clear_all():
                                time_entry.delete(0,ctk.END)
                                destination_entry.delete(0,ctk.END)
                                flight_name_entry.delete(0,ctk.END)
                                flight_number_entry.delete(0,ctk.END)
                                gate_number_entry.delete(0,ctk.END)

                            #terminal and flight status values for helpful purpose and for displaying the contents in the database 

                            terminal_values=['T1','T2','T3','T4','T5','T6','T7','T8','T9','T10','T11','T12','T13','T15']
                            flight_status_values=['CANCELLED','ARRIVED','DEPARTED','BOARDING','TAXIED','DELAYED','ON TIME','DEPARTING']

                            #creating a frame for inserting the flight details 
                            frame6=ctk.CTkFrame(master=app3,corner_radius=10,height=300,border_width=3)
                            frame6.pack(pady=10,padx=10,fill='x')

                            #creating a label for flight information display system
                            title=ctk.CTkLabel(master=frame6,text="FlIGHT INFORMATION DISPLAY SYSTEM")
                            title.grid(row=0,columnspan=2,padx=50,pady=7)

                            #creating a label for Time entry of flights 
                            time_label=ctk.CTkLabel(master=frame6,text="Flight Time")
                            time_label.grid(row=1,column=0)

                            #creating an entry for Time of flights
                            time_entry=ctk.CTkEntry(master=frame6,placeholder_text="Flight Time")
                            time_entry.grid(row=1,column=1,padx=10,pady=10)

                            #creating a label for Destination 
                            destination=ctk.CTkLabel(master=frame6,text="Destination")
                            destination.grid(row=2,column=0)

                            #creating an entry for destination 
                            destination_entry=ctk.CTkEntry(master=frame6,placeholder_text="Destination")
                            destination_entry.grid(row=2,column=1,padx=10,pady=10)

                            #creating a label for flight name 
                            flight_name=ctk.CTkLabel(master=frame6,text="Flight Name")
                            flight_name.grid(row=3,column=0)

                            #creating an entry for flight name
                            flight_name_entry=ctk.CTkEntry(master=frame6,placeholder_text="Flight Name")
                            flight_name_entry.grid(row=3,column=1,padx=10,pady=10)

                            #creating a label for flight number 
                            flight_number=ctk.CTkLabel(master=frame6,text="Flight Number")
                            flight_number.grid(row=1,column=2)

                            #creating an entry for flight number 
                            flight_number_entry=ctk.CTkEntry(master=frame6,placeholder_text="Flight Number")
                            flight_number_entry.grid(row=1,column=3,padx=20,pady=10)

                            #creating a label for Terminal 
                            terminal=ctk.CTkLabel(master=frame6,text="Terminal Number")
                            terminal.grid(row=2,column=2)

                            #creating an entry for terminals
                            terminal_values=ctk.CTkComboBox(master=frame6, dropdown_hover_color="grey",values=terminal_values)
                            terminal_values.grid(row=2,column=3,padx=20,pady=10)

                            #creating a label for status of planes 
                            flight_status=ctk.CTkLabel(master=frame6,text="Flight Status")
                            flight_status.grid(row=3,column=2)

                            #creating an entry for flight status 
                            flight_status_entry=ctk.CTkComboBox(master=frame6,dropdown_hover_color="grey",values=flight_status_values)
                            flight_status_entry.grid(row=3,column=3,padx=10,pady=10)

                            #creating a label for gate number 
                            gate_number=ctk.CTkLabel(master=frame6,text="Gate Number")
                            gate_number.grid(row=4,columnspan=1)

                            #creating an entry for gate number 
                            gate_number_entry=ctk.CTkEntry(master=frame6,placeholder_text="Gate Number")
                            gate_number_entry.grid(row=4,column=1,padx=10,pady=10)

                            #creating a button for exiting the flight details window 
                            button=ctk.CTkButton(master=frame6,text="EXIT",fg_color="black",command=exit_window,height=50,corner_radius=10)
                            button.grid(row=2,column=6,padx=20,pady=10)

                            #creating a frame for buttons and their actions 
                            frame7=ctk.CTkFrame(master=app3,corner_radius=10,height=50,border_width=2)
                            frame7.pack(padx=10,pady=10,fill='x')

                            #creating a tree view for different types of buttons and their functions 
                            button=ctk.CTkButton(master=frame7,text="Insert",corner_radius=10,fg_color="black",height=30,command=insert_record)
                            button.grid(row=0,column=0,padx=50,pady=10)

                            #creating a button for updating the flight records 
                            button=ctk.CTkButton(master=frame7,text="Update",corner_radius=10,fg_color="black",height=30,command=update_record)
                            button.grid(row=0,column=2,padx=120,pady=10)

                            #creating a button for deleting the record 
                            button=ctk.CTkButton(master=frame7,text="Delete",corner_radius=10,fg_color="black",height=30,command=delete_record)
                            button.grid(row=0,column=3,padx=80,pady=10)

                            #creating a button for exiting the system for inserting the records 
                            button=ctk.CTkButton(master=frame7,text="Clear All",corner_radius=10,fg_color="black",height=30,command=clear_all)
                            button.grid(row=0,column=4,padx=80,pady=10)

                            #creating a frame for displaying the records which are inserted updated and deleted 
                            frame8=ctk.CTkFrame(master=app3,corner_radius=10,border_width=2)
                            frame8.pack(padx=10,pady=10,fill='both',expand=True)
                            style=ttk.Style(frame8)
                            style.theme_use("clam")
                            style.configure("Treeview",font=('Calibri',18),rowheight=50)
                            style.configure("Treeview.Heading",font=('Calibri',18),fg_color="lightblue")
                            #creating a treeview for displaying the records 
                            tv=ttk.Treeview(frame8,selectmode='browse',columns=(1,2,3,4,5,6,7),show="headings",style="Treeview")

                            #defining the scrollbar for y-axis
                            scrollbar=ttk.Scrollbar(frame8,orient="vertical", command=tv.yview)
                            tv.configure(yscrollcommand=scrollbar.set)
                            scrollbar.pack(side='right',fill='y')

                            #passing the headings and values in flight details window

                            tv.heading("1",text="Flight Time",anchor=tk.CENTER)
                            tv.heading("2",text="Destination",anchor=tk.CENTER)
                            tv.column("2",width=250)
                            tv.heading("3",text="Flight Name",anchor=tk.CENTER)
                            tv.heading("4",text="Flight Number",anchor=tk.CENTER)
                            tv.heading("5",text="Terminal",anchor=tk.CENTER)
                            tv.heading("6",text="Flight Status",anchor=tk.CENTER)
                            tv.heading("7",text="Gate Number",anchor=tk.CENTER)
                            tv.pack(fill='x',pady=5,padx=5)

                            displayall()
                            app3.mainloop()
          
                        else:
                            global trials
                            trials=trials+1
                            if (trials!=3):
                                messagebox.showerror("Login Status",f'Invalid Login {3-trials} attempts left')
                            else:
                                new_window1.destroy()
                                app2.destroy()
                                messagebox.showwarning("Login Status","Restart the Program")
                    #creating a frame for accesing the details 
                    frame3=ctk.CTkFrame(master=new_window1)
                    frame3.pack(pady=8,padx=8)
                    
                    #creating a label for receiving the secret code for insertion 
                    label=ctk.CTkLabel(master=frame3,text="PassCode")
                    label.pack(pady=10,padx=8)
                    
                    #creating an entry for passcode 
                    label_entry=ctk.CTkEntry(master=frame3,placeholder_text="Passcode")
                    label_entry.pack(pady=10,padx=8)
                    
                    #creating a submit for accessing the details 
                    button=ctk.CTkButton(master=frame3,text='Submit',fg_color='black',corner_radius=10,command=check_code)
                    button.pack(pady=10,padx=8)
                    
                    new_window1.mainloop()
                
                #defining the function for displaying the flight details in new window with full screeen view
                def flight_display_button():
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
                #defining the function for updating code
                def change_code():
                    new_window3=ctk.CTk()
                    new_window3.geometry("300x300")
                    new_window3.title("Change Code")
                    
                    #defining afunction for receiving new code
                    def new_code():
                        new_code1=label_new_code.get()
                        old_code1=label_code.get()
                        label_new_code.delete(0,ctk.END)
                        label_code.delete(0,ctk.END)
                        con=mysql.connector.connect(host="localhost",user="root",password="",database="new_user_infromation")
                        cursor=con.cursor()
                        cursor.execute("select * from user_data where Code='"+old_code1+"'")
                        db_result=cursor.fetchone()
                        if (db_result==None):
                            messagebox.showinfo("Update Code","Invalid code")
                        else:
                            con=mysql.connector.connect(host="localhost",user="root",password="",database="new_user_infromation")
                            cursor=con.cursor()
                            cursor.execute("update user_data set Code='"+new_code1+"' where Code='"+old_code1+"'")
                            cursor.execute("commit")
                            messagebox.showinfo("Update Status","Code Updated")
                            new_window3.destroy()
                        
                    #creating a frame for receiving the records
                    frame5=ctk.CTkFrame(master=new_window3)
                    frame5.pack(pady=10,padx=10,fill='both',expand=True)
                    
                    #creating a label for entering the change code details 
                    label=ctk.CTkLabel(master=frame5,text='Old Code') 
                    label.pack(pady=10,padx=10)
                    
                    #creating an entry for old code
                    label_code=ctk.CTkEntry(master=frame5,placeholder_text="Old Code")    
                    label_code.pack(pady=10,padx=10)
                    
                    #creating a label for new code 
                    label=ctk.CTkLabel(master=frame5,text="New Code")
                    label.pack(pady=10,padx=10)
                    
                    #creating an entry for new code
                    label_new_code=ctk.CTkEntry(master=frame5,placeholder_text='New code')
                    label_new_code.pack(pady=10,padx=10)
                    
                    #creating a button for submitting the details 
                    button=ctk.CTkButton(master=frame5,text="Submit",fg_color="black",corner_radius=10,command=new_code)
                    button.pack(pady=10,padx=10)
                    
                    new_window3.mainloop()            
                #defining the frame for accessing the details and updating
                frame2=ctk.CTkFrame(master=app2)
                frame2.pack(pady=20,padx=10,fill="both",expand=True)
                
                #creating a button for inserting the record 
                button=ctk.CTkButton(master=frame2,text="Flight Data",fg_color="black",corner_radius=10,command=flight_update)
                button.pack(pady=12,padx=12)
                
                #creating a button for flight display layout
                button=ctk.CTkButton(master=frame2,text="Flight Display",fg_color="black",corner_radius=10,command=flight_display_button)
                button.pack(pady=12,padx=12)
                
                #creating a button for changing the secret code 
                button=ctk.CTkButton(master=frame2,text="Change Code",fg_color="black",corner_radius=10,command=change_code)
                button.pack(pady=12,padx=12)
                
                app2.mainloop()
        
        #creating a function for resetting the password 
        def forgot_pass():
            new_window2=ctk.CTk()
            new_window2.geometry("300x300")
            new_window2.title("Forgot Password")
            
            #defining the function for submission of details of new password 
            def update_password():
                new_pass=label1.get()
                old_pass=label2.get()
                label1.delete(0,ctk.END)
                label2.delete(0,ctk.END)
                con=mysql.connector.connect(host="localhost",user="root",password="",database="new_user_infromation")
                cursor=con.cursor()
                cursor.execute("select * from user_data where password='"+old_pass+"'")
                db_result=cursor.fetchone()
                if (db_result==None):
                    messagebox.showinfo("Update status","Record Not Exists")
                else:
                    cursor.execute("update user_data set Password='"+new_pass+"' where Password='"+old_pass+"'")
                    cursor.execute("commit")
                    messagebox.showinfo('Update Status','Password Updated Succesfully')
                    new_window2.destroy()
            # creating a frame for receiving the forgot password details
            frame4=ctk.CTkFrame(master=new_window2)
            frame4.pack(pady=20,padx=20,fill='both',expand=True)
            
            #creating a label for old password
            label=ctk.CTkLabel(master=frame4,text="Old Password")
            label.pack(pady=8,padx=8)
            
            #creating an entry for old password 
            label2=ctk.CTkEntry(master=frame4,placeholder_text="Old Password",show="*")
            label2.pack(pady=8,padx=8)
            
            #creating a label for receving the new password 
            label=ctk.CTkLabel(master=frame4,text="New Password")
            label.pack(pady=8,padx=8)
            
            #creating a entry for receiving the new password 
            label1=ctk.CTkEntry(master=frame4,placeholder_text="New Password",show="*")
            label1.pack(pady=8,padx=8)
            
            #creating a button for submitting the record 
            button=ctk.CTkButton(master=frame4,text="Submit",fg_color="black",corner_radius=10,command=update_password)
            button.pack(pady=8,padx=8)
                                 
            new_window2.mainloop()
        #creating a frame for accessing the user_details for username and password 
        frame1=ctk.CTkFrame(master=app1)
        frame1.pack(pady=20,padx=10,fill="both",expand=True)
        
        #creating a label for entering the username 
        label=ctk.CTkLabel(master=frame1,text="Username")
        label.pack(pady=8,padx=8)
        
        #creating an entry for username
        username=ctk.CTkEntry(master=frame1,placeholder_text="Username")
        username.pack(pady=8,padx=8)
        
        #creating a label for passsword
        label=ctk.CTkLabel(master=frame1,text="Password")
        label.pack(pady=8,padx=8)
        
        #creating an entry for password 
        password=ctk.CTkEntry(master=frame1,placeholder_text="Password",show="*")
        password.pack(pady=8,padx=8)
        
        #creating a  checkbox for receiving the details 
        checkbox=ctk.CTkCheckBox(master=frame1,text="Remember Me")
        checkbox.pack(pady=8,padx=8)
        
        #creating a submit for final submissison of details 
        button=ctk.CTkButton(master=frame1,text="Submit",fg_color="black",corner_radius=10,command=submit)
        button.pack(pady=8,padx=8)
        
        #creating a button for forgot password 
        button=ctk.CTkButton(master=frame1,text="Forgot Password",fg_color="black",corner_radius=10,command=forgot_pass)
        button.pack(pady=8,padx=8)
        app1.mainloop()

#deciding the frame for accessing the records 
frame=ctk.CTkFrame(master=app)
frame.pack(pady=10,padx=10,fill="none",expand=True)

#creating a label for inserting the image in frame and with some text 
img = ctk.CTkImage(dark_image=Image.open("C:\\Users\\hp\\Desktop\\java folder\\FIDS FOLDER\\download (2).jpeg"),size=(100,70))
#creating a label for placing the image in frame 
labelimage=ctk.CTkLabel(master=frame,image=img,text="")
labelimage.pack(pady=8,fill="none",expand=True)

#creating a label for entering the passcode
label=ctk.CTkLabel(master=frame,text="PassCode")
label.pack(pady=8,padx=8)

#creating an entry for receiving the passcode 
passcode=ctk.CTkEntry(master=frame,placeholder_text="PassCode",show="*")
passcode.pack(pady=8,padx=8)

#creating a label for receiving the Secret Code
label=ctk.CTkLabel(master=frame,text="Code")
label.pack(pady=8,padx=8)

#creating an entry for receiving the Secret Code
code=ctk.CTkEntry(master=frame,placeholder_text="Code",show="*")
code.pack(pady=8,padx=8)

#creating a button for receiving the details 
button1=ctk.CTkButton(master=frame,text="Submit",text_color="white",fg_color="black",corner_radius=10,command=pass_login)
button1.pack(pady=8,padx=8)

app.mainloop()

 