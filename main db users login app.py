#importing the rquired modules for performing the function and creating the GUI for FIDS 

import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import random 
import mysql.connector

ctk.set_appearance_mode("light")

#setting the blue color ribbon for upperframe 
ctk.set_default_color_theme("blue")

#creating an object for acessing the main window layout along with the use of customtkinter 
app=ctk.CTk()

#deciding the login interface for users
app.geometry("200x200")
app.title("Login")

#defining the login function for receiving the passcode and undergo verification

def login():
    user_entry1=user_entry.get()
    if (str(user_entry1)=="2021shashi"):
        messagebox.showinfo("Login Status","Successful Login")
        app.destroy()
        app1=ctk.CTk()
        app1.geometry("350x350")
        app1.title("Admin Verify")
        
        #defining the function for receving the username and password 
        
        def login_pass():
            user_entry2=user_entry_pass.get()
            password=user_pass.get()
            con=mysql.connector.connect(host="localhost",user="root",password="",database="new_user_infromation")
            cursor=con.cursor()
            cursor.execute("select count(*) from user_data where username='"+user_entry2+"' and password='"+password+"'")
            db_result=cursor.fetchone()[0]
            if (db_result==None):
                messagebox.showinfo("Login Status",'User not exists')
            else:
                messagebox.showinfo("Login Status","Succesful Login")
                app1.destroy()
                app2=ctk.CTk()
                app2.geometry("300x300")
                app2.title("Functions Window")
                
                #defining the functions for new _user 
                
                def new_user():
                    new_window1=ctk.CTk()
                    new_window1.geometry("570x570")
                    new_window1.title("New User Registration")
                    
                    #defining the register function for submission of records to database 
                    def register():
                        name1=name.get()
                        email1=email_entry.get()
                        phone1=phone_entry.get()
                        user1=username.get()
                        pass1=password1.get()
                        con=mysql.connector.connect(host="localhost",user="root",password="",database="new_user_infromation")
                        cursor=con.cursor()
                        cursor.execute("select count(*) from user_data where Phone_number='"+phone1+"'")
                        db_result=cursor.fetchone()[0]
                        if (db_result==None):
                            #pass_c=random.randint(0,1400)
                            cursor.execute("insert into user_data values('"+name1+"','"+email1+"','"+phone1+"','"+user1+"','"+pass1+"','"+str(random.randint(0,1400))+"','"+str(random.randint(0,30))+"')")
                            cursor.execute("commit")
                            messagebox.showinfo("Insert Status","Succesfully Registered")
                            new_window1.destroy()
                        else:
                            messagebox.showinfo("Insert Status","User Exists")
                
                    #defining the frame for receiving details
                    frame3=ctk.CTkFrame(master=new_window1)
                    frame3.pack(pady=10,padx=10,fill='both',expand=True)
                    
                    #defining the label for receiving the name  
                    
                    label=ctk.CTkLabel(master=frame3,text="Name")
                    label.pack(pady=8,padx=8)
                    
                    #creating the user entry for Name 
                    name=ctk.CTkEntry(master=frame3,placeholder_text="Name")
                    name.pack(pady=8,padx=8)
                    
                    #creating a label for email
                    label=ctk.CTkLabel(master=frame3,text="Email")
                    label.pack(pady=8,padx=8)
                    
                    #creating entry for email
                    email_entry=ctk.CTkEntry(master=frame3,placeholder_text="Email")
                    email_entry.pack(pady=8,padx=8)
                    
                    #creating label for phone number
                    label=ctk.CTkLabel(master=frame3,text="Phone Number")
                    label.pack(pady=8,padx=8)
                    
                    #creating entry for phone number 
                    phone_entry=ctk.CTkEntry(master=frame3,placeholder_text="Phone Number")
                    phone_entry.pack(pady=8,padx=8)
                    
                    #creating label for username 
                    label=ctk.CTkLabel(master=frame3,text="Username")
                    label.pack(pady=8,padx=8)
                    
                    #creating entry for username 
                    username=ctk.CTkEntry(master=frame3,placeholder_text="Username")
                    username.pack(pady=8,padx=8)
                    
                    #creating a label for password 
                    label=ctk.CTkLabel(master=frame3,text='Password')
                    label.pack(pady=8,padx=8)
                    
                    #creating entry for password
                    password1=ctk.CTkEntry(master=frame3,placeholder_text="Password")
                    password1.pack(pady=8,padx=8)
                    
                    #creating a button for submission of records 
                    button=ctk.CTkButton(master=frame3,text="Submit",fg_color="black",corner_radius=10,command=register)
                    button.pack(pady=8,padx=8)
                    
                    new_window1.mainloop()
                    
                #defining the function for generating the passcode
                def update_passcode():
                    con=mysql.connector.connect(host="localhost",user="root",password="",database="new_user_infromation")
                    cursor=con.cursor()
                    cursor.execute("update user_data set Passcode='"+str(random.randint(0,1400))+"'")
                    cursor.execute("commit")
                    messagebox.showinfo("Update status","Succesful Updation")
                
                #defining the function for updating the secret code
                def change_code():
                    con=mysql.connector.connect(host="localhost",user="root",password="",database="new_user_infromation")
                    new_window2=ctk.CTk()
                    new_window2.geometry("400x400")
                    new_window2.title("Update Code")
                    
                    #defining the function for updating the records 
                    def change():
                        con=mysql.connector.connect(host="localhost",user="root",password="",database="new_user_infromation")
                        cursor=con.cursor()
                        password_user=pass_entry.get()
                        changecode=new_code.get()
                        cursor.execute("update user_data set Code='"+changecode+"' where Password='"+password_user+"'")
                        cursor.execute("commit")
                        messagebox.showinfo("Update Code","Code Updated")
                        new_window2.destroy()
                        
                    #creating a frame for updating the secret Code
                    frame4=ctk.CTkFrame(master=new_window2)
                    frame4.pack(pady=20,padx=10,fill='both',expand=True)
                    
                    #creating a label for receiving the password
                    label=ctk.CTkLabel(master=frame4,text="Password")
                    label.pack(pady=8,padx=8)
                    
                    #creating a entry for receving the password 
                    pass_entry=ctk.CTkEntry(master=frame4,placeholder_text="Password")
                    pass_entry.pack(pady=8,padx=8)
                    
                    #creating a label for new code 
                    label=ctk.CTkLabel(master=frame4,text="New Code")
                    label.pack(pady=8,padx=8)
                    
                    #creating an entry for receiving the new code
                    new_code=ctk.CTkEntry(master=frame4,placeholder_text="New code")
                    new_code.pack(pady=8,padx=8)
                    
                    #creating a button for submitting the records 
                    button=ctk.CTkButton(master=frame4,text="Submit",fg_color="black",corner_radius=10,command=change)
                    button.pack(pady=8,padx=8)
                    
                    new_window2.mainloop()
                    
                #defining frame for executing some precious commands 
                
                frame2=ctk.CTkFrame(master=app2)
                frame2.pack(pady=20,padx=20,fill='both',expand=True)
                
                #creating a button for New user Registration 
                
                button=ctk.CTkButton(master=frame2,text="New Registration",fg_color="black",corner_radius=10,command=new_user)
                button.pack(pady=10,padx=8)
                
                #creating a button for receiving the command of modify pass code 
                button1=ctk.CTkButton(master=frame2,text="Update PassCode",fg_color="black",corner_radius=10,command=update_passcode)
                button1.pack(pady=10,padx=8)
                
                #creating a button for receiving the command of changing secret code
                button2=ctk.CTkButton(master=frame2,text="Change Code",fg_color="black",corner_radius=10,command=change_code)
                button2.pack(pady=10,padx=8)
                
                app2.mainloop()
        #defining the frame for receiving the username and password 
        
        frame1=ctk.CTkFrame(master=app1)
        frame1.pack(pady=20,padx=10,fill="both",expand=True)
        
        #defining the label for username 
        label=ctk.CTkLabel(master=frame1,text="Username")
        label.pack(pady=8,padx=8)
        
        #defining the entry for username
        user_entry_pass=ctk.CTkEntry(master=frame1,placeholder_text="Username")
        user_entry_pass.pack(pady=8,padx=8)
        
        #defining the label for password 
        label=ctk.CTkLabel(master=frame1,text="Password")
        label.pack(pady=8,padx=8)
        
        #defining the entry for password 
        user_pass=ctk.CTkEntry(master=frame1,placeholder_text='Password')
        user_pass.pack(pady=8,padx=8)
        
        #creating a check box for remembering user 
        
        checkbox=ctk.CTkCheckBox(master=frame1,text="Remember Me")
        checkbox.pack(pady=8,padx=8)
        
        #creating a button final authentication 
        button=ctk.CTkButton(master=frame1,text='Submit',fg_color="black",corner_radius=10,command=login_pass)
        button.pack(pady=8,padx=8)
        
        
        app1.mainloop()
    else:
        messagebox.showinfo("Login Status","Inavlid Login")
#creating the frame for receiving the passcode 
frame=ctk.CTkFrame(master=app,fg_color="white")
frame.pack(padx=20,pady=10,fil="none",expand=True)

#creating the label for entering the passcode 
label=ctk.CTkLabel(master=frame,text="PassCode",text_color="black")
label.pack(pady=10,padx=10)

#creating the entry for receiving the passcode 
user_entry=ctk.CTkEntry(master=frame,placeholder_text="Passcode",text_color="black")
user_entry.pack(pady=10,padx=10)

#creating the button for receiving the entry and submitting it for verification 
button=ctk.CTkButton(master=frame,text="Submit",fg_color="black",command=login,corner_radius=10)
button.pack(pady=10,padx=10)

app.mainloop()
