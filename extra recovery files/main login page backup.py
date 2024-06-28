import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import mysql.connector
import random 
import threading 
import time 
#set the desired theme for custom window setup 

ctk.set_appearance_mode("dark")
  
#setting the blue color theme for upper ribbon 
ctk.set_default_color_theme("blue")
  
app = ctk.CTk()
#deciding the login interface for users
app.geometry("520x520")
app.title("Modern Login UI using Customtkinter")

#defining the login pag editor areas
def login():
    '''new_window=ctk.CTkToplevel(app)
    new_window.title("New window for Fligth informations")
    new_window.geometry("600x700")'''
    def start_timer():
        timer_thread=threading
    username=user_entry.get()
    password=user_pass.get()
    if (username=="" or password==""):
        new_window=ctk.CTkToplevel(app)
        new_window.title("Login details verification")
        new_window.geometry("600x700")
        
        #creating a frame for accepting the phone number and otp generated 
        frame1=ctk.CTkFrame(master=new_window)
        frame1.pack(pady=20,padx=10,fill='both',expand=True)
        
        #creating a label for entering the phone number
        label=ctk.CTkLabel(master=frame,text="Phone number")
        label.pack(pady=12,padx=10)
        
        #creating a entry for phone Number
        phone_entry=ctk.CTkEntry(master=frame,placeholder_text="Phone number")
        phone_entry.pack(pady=12,padx=10)
        
        #creating a button for sending the OTP to registered mobile number  
        button=ctk.CTkButton(master=frame,text="Send OTP",command=send_otp)
        button.pack(pady=12,padx=10)
        
        #creating a button for resend otp 
        button=ctk.CTkButton(master=frame,placeholder_text="Resend OTP",command=resend_otp)
    else:
        messagebox.showinfo("Insert Status","User not exists")

#defining the new registration frame for receiving new users 
def register():
    new_window1=ctk.CTkToplevel(app)
    new_window1.title("New User Regsitration")
    new_window1.geometry("600x600")
    #defining function for logging details and registry details 
    def login1():
        name=name_entry.get()
        email=email_id.get()
        phone=phone_entry.get()
        username=user_name.get()
        password=pass_entry.get()
        #now checking for existence of details in the database 
        if (name=="" or email=="" or phone=="" or username=="" or password==""):
            messagebox.showinfo("Insert Status"," User Already Exists")
        else:
            con=mysql.connector.connect(host="localhost",user="root",password="",database="new_user_infromation")
            cursor=con.cursor()
            cursor.execute("insert into user_data values('"+name+"','"+email+"','"+phone+"','"+username+"','"+password+"')")
            cursor.execute("commit")
            messagebox.showinfo("Insert Status","Registered successfully")
            con.close()
            new_window1.destroy()
    
    #creating the frame for new user registration
    
    frame1=ctk.CTkFrame(master=new_window1)
    frame1.pack(pady=20,padx=40,fill='both',expand=True)
    
    #creating the label for first name 
    label=ctk.CTkLabel(master=frame1,text="Name")
    label.pack(pady=8,padx=8)
    #creating the name entry field
    name_entry=ctk.CTkEntry(master=frame1,placeholder_text="First Name")
    name_entry.pack(pady=8,padx=8)
    #creating label for email id 
    
    label=ctk.CTkLabel(master=frame1,text="EMAIL ID")
    label.pack(pady=8,padx=8)
    
    #creating entry for email id 
    email_id=ctk.CTkEntry(master=frame1,placeholder_text="EMAIL ID")
    email_id.pack(pady=8,padx=8)
    
    #creating label for phone number
    label=ctk.CTkLabel(master=frame1,text="Phone No.")
    label.pack(pady=8,padx=8)
    
    #creating entry for phone number 
    phone_entry=ctk.CTkEntry(master=frame1,placeholder_text="Phone No.")
    phone_entry.pack(pady=8,padx=8)
    
    #creating label for username 
    label=ctk.CTkLabel(master=frame1,text="Username")
    label.pack(pady=8,padx=8)
    
    #creating entry for username 
    user_name=ctk.CTkEntry(master=frame1,placeholder_text="Username")
    user_name.pack(pady=8,padx=8)
    
    #creating label for password
    label=ctk.CTkLabel(master=frame1,text="Password")
    label.pack(pady=8,padx=8)
    
    #creating entry for password
    pass_entry=ctk.CTkEntry(master=frame1,placeholder_text="Password")
    pass_entry.pack(pady=8,padx=8)
    
    #creating submit button for fetching the data and redirecting it to main login page 
    button=ctk.CTkButton(master=frame1,text="Submit",command=login1)
    button.pack(pady=8,padx=8)

#defining the forgot password function for password reset
def forgot_pass():
    new_window2=ctk.CTkToplevel(app)
    new_window2.title("Forgot Password")
    new_window2.geometry("500x500")
    
    #defining the new_pass function for receiving new password details
    
    def new_password():
        user_name=user_entry.get()
        forgot_pass=new_pass.get()
        confirm_new=confirm_pass.get()
        if (user_name=="" or forgot_pass=="" or confirm_new==""):
            messagebox.showinfo("Insert Status","Password can't be similar")
        elif (user_name!=""):
            messagebox.showinfo("Insert Status","Username does not exist")
        else:
            con=mysql.connector.connect(host="localhost",user="root",password="",database="new_user_infromation")
            cursor=con.cursor()
            cursor.execute("update user_data set password='"+forgot_pass+"' where username='"+user_name+"'")
            cursor.execute("commit")
            messagebox.showinfo("Insert Status","Password Upadated succesfully") 
            con.close()
            new_window2.destroy()           
    #creating the frame for receiving the password reset details
    
    frame2=ctk.CTkFrame(master=new_window2)
    frame2.pack(pady=20,padx=40,fill='both',expand=True)
    
    #creating the label for username entry
    label=ctk.CTkLabel(master=frame2,text="Username")
    label.pack(pady=12,padx=10)
    
    #creating the user_entry for receiving username
    user_entry=ctk.CTkEntry(master=frame2,placeholder_text="Username")
    user_entry.pack(pady=12,padx=10)
    
    #creating the label for new password 
    label=ctk.CTkLabel(master=frame2,text="New Password")
    label.pack(pady=12,padx=10)
    #creating the user_new pass area 
    new_pass=ctk.CTkEntry(master=frame2,placeholder_text="New Password")
    new_pass.pack(pady=12,padx=10)
    
    #confirm password label 
    label=ctk.CTkLabel(master=frame2,text="Confirm Password")
    label.pack(pady=12,padx=10)
    
    #creating the confirm entry pass
    confirm_pass=ctk.CTkEntry(master=frame2,placeholder_text="Confirm Password")
    confirm_pass.pack(pady=12,padx=10) 
    
    #creating a submission button for receiving the inputs
    button=ctk.CTkButton(master=frame2,text="Submit",command=new_password)
    button.pack(pady=12,padx=20)
       
#creating the frame for receiving the user details 

frame=ctk.CTkFrame(master=app)
frame.pack(pady=20,padx=40,fill='both',expand=True)

#label for the main login page content including username and password 
label = ctk.CTkLabel(master=frame,text="Main Login page")
label.pack(pady=12,padx=10)     
  
#now creating frame for lable of username and password 
label=ctk.CTkLabel(master=frame,text="USERNAME")
label.pack(pady=12,padx=10)
#now creating the user entry label for receiving the input from the user

user_entry=ctk.CTkEntry(master=frame,placeholder_text="Username")
user_entry.pack(pady=12,padx=10)

label=ctk.CTkLabel(master=frame,text="Password")
label.pack(pady=12,padx=10)

#creating entry for users password 
user_pass=ctk.CTkEntry(master=frame,placeholder_text="Password")
user_pass.pack(pady=12,padx=10)

button=ctk.CTkButton(master=frame,text="Login",command=login)
button.pack(pady=12,padx=10)

#creating forgot password area
Button=ctk.CTkButton(master=frame,text="Forgot Password",command=forgot_pass)
Button.pack(pady=12,padx=10)

#creating a remeber checkbox for futher recordings
checkbox=ctk.CTkCheckBox(master=frame,text="Remember Me")
checkbox.pack(pady=12,padx=10)

#creating the button for new registration 
button=ctk.CTkButton(master=frame,text="Register",command=register)
button.pack(pady=12,padx=10)
app.mainloop()