''' main login page recovery details 
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox 

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")
app=ctk.CTk()
trials=0
app.geometry("350x350")
app.title('User Login')
def pass_login():
    passcode_entry=passcode.get()
    code_entry=code.get()
    global trials
    if ((str(passcode_entry)=="284") and (str(code_entry)=="sha1234")):
        messagebox.showinfo("Insert Status","Login Succesful")
    else:
        trials=trials+1
        if (trials!=3):
            messagebox.showerror("Insert Status",f'Inavlid login {3-trials} trials left')
        else:
            button.destroy()
            messagebox.showwarning("Insert Status",'restart the program')
            
frame=ctk.CTkFrame(master=app)
frame.pack(pady=20,padx=10,fill='none',expand=True)

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
button=ctk.CTkButton(master=frame,text="Submit",fg_color="black",corner_radius=10,command=pass_login)
button.pack(pady=8,padx=8)

app.mainloop()
'''
'''
style=ttk.Style(app3)
app3.tk.call("source","forest-light.tcl")
app3.tk.call("source","forest-dark.tcl")
style.theme_use("forest-light")

#creating a frame for inserting updating and deleting the flight details 
frame=ctk.CTkFrame(app3)
frame.pack(fill='both',expand=True)
terminals_values=['T1','T2','T3','T4','T5','T6','T7','T8','T9','T10','T11','T12','T13','T14','T15']
entry_status=['ARRIVED','DELAYED','CANCELLED','DEPARTED','BOARDING','TAXIED','ON TIME']
#creating the widgets frame for inserting deleting and viewing the records 
widgets_frame=ttk.LabelFrame(frame,text="Flight Details")

widgets_frame.grid(row=0,column=0)

#creating a name entry for inserting the flight name 
time_entry=ttk.Entry(widgets_frame)
time_entry.insert(0,"Time")
time_entry.bind("<FocusIn>",lambda e: time_entry.delete('0','end'))
time_entry.grid(row=0,column=0,sticky="ew") 

#age_spinbox= ttk.Spinbox(widgets_frame,from 1 to 100)
#age_spinbox.insert(0,"Gate")
#age_spinbox.grid(row=1,column=0,sticky="ew")
#creating an entry for departing destination of flights 
destination_entry=ttk.Entry(widgets_frame)
destination_entry.insert(0,"Destination")
destination_entry.bind("<FocusIn>",lambda e: destination_entry.delete('0','end'))
destination_entry.grid(row=1,column=0,sticky="ew")

#creating an entry for flight name and its authorisation company 
flight_name=ttk.Entry(widgets_frame)
flight_name.insert(0,"Flight Name")
flight_name.bind("<FocusIn>",lambda e: flight_name.delete('0','end'))
flight_name.grid(row=2,column=0,sticky='ew')

#creating an entry for flight number 
flight_number=ttk.Entry(widgets_frame)
flight_number.insert(0,"Flight Number")
flight_number.bind("<FocusIn>",lambda e: flight_number.delete('0','end'))
flight_number.grid(row=3,column=0,sticky='ew')

#creating an entry for Terminal
terminal_entry=ttk.Combobox(widgets_frame, values=terminals_values)
terminal_entry.current(0)
terminal_entry.grid(row=4,column=0,sticky="ew")

#creating an entry status of planes 
entry_status_planes=ttk.Combobox(widgets_frame,values=entry_status)
entry_status_planes.current(0)
entry_status_planes.grid(row=5,column=0,sticky='ew')

#creating an entry for gate values 
gate_values=ttk.Entry(widgets_frame)
gate_values.insert(0,"Gate")
gate_values.bind("<FocusIn>",lambda e: gate_values.delete('0','end'))
gate_values.grid(row=6,column=0,sticky='ew')'''

'''import customtkinter as ctk 
import tkinter as tk 
from tkinter import END, ttk
import mysql.connector 
from tkinter import messagebox

app3=ctk.CTk()
app3.geometry("800x600")
app3.title("Fight Details")
con=mysql.connector.connect(host="localhost",user="root",password="",database="new_user_infromation")
cursor=con.cursor()

#display function for dislaying the data in the table in the for of treeview 
def displayall():
    global cursor
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
    global cursor
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
    global cursor
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
    global cursor
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
style=ttk.Style()
style.configure("mystyle.Treeview",font=('Calibri',18),rowheight=50)
style.configure("mystyle.Treeview.Heading",font=('Calibri',18),)

#creating a treeview for displaying the records 
tv=ttk.Treeview(frame8,columns=(1,2,3,4,5,6,7),show="headings",style="mystyle.Treeview")

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
flight data updation window recovery 
'''

from tkinter import *
import customtkinter as ctk
from tkinter import ttk,END
import mysql.connector
from PIL import Image
import time
import tkinter as tk

ctk.set_appearance_mode("dark")
app4=ctk.CTk()
width= app4.winfo_screenwidth()
height= app4.winfo_screenheight()
app4.geometry("%dx%d" % (width, height))
#app4.geometry("700x600")
app4.title("DISPLAY SCREEN")
app4.config(bg="#EEE8CD")
#defining the link for real time updation of data in the database 
con=mysql.connector.connect(host="localhost",user="root",password="",database="new_user_infromation")
cursor=con.cursor()
#creating a function for displaying the time
def clock():
   hh= time.strftime("%I")
   mm= time.strftime("%M")
   ss= time.strftime("%S")
   day=time.strftime("%A")
   ap=time.strftime("%p")
   time_zone= time.strftime("%Z")
   clock_time.configure(text= hh + ":" + mm +":" + ss)
   clock_time.after(1000,clock)
   country_label.configure(text=day+" "+time_zone)

#now creating a function for upadting the time 
def updateTime():
   clock_time.configure(text="New Text")
   
#now defining the display function for displaying the records fethched from the database
def display():
    for rows in tv.get_children():
        tv.delete(rows)
    cursor.execute("select * from flight_data")
    for row in cursor.fetchall():
        tv.insert("",END,values=row)

#now defining a rotate function for rotating the records fetchded continuosly after 5 seconds
def rotate_data(): 
    '''cursor.execute("select * from flight_data")
    data=cursor.fetchall()
    data = data[-1:] + data[:-1]  # Rotate the data by moving the last item to the beginning

    # Clear the Treeview
    for rows in tv.get_children():
        tv.delete(rows)

    # Insert the data into the Treeview
    for i in data:
        tv.insert("",END,values=i)
    # Schedule the next rotation
    tv.after(2000,rotate_data)  # 3000ms (3 second) delay'''
    
    records = [tv.item(item)["values"] for item in tv.get_children()]

    # Shift the last record to the top
    first_record = records.pop()
    records.insert(0, first_record)

    # Clear the TreeView
    tv.delete(*tv.get_children())

    # Insert the rotated records back into the TreeView
    for record in records:
        tv.insert("", "end", values=record)

    tv.after(4000, rotate_data) 
#creating a frame for displaying the flight data with different results such as logo amd time 
frame9=ctk.CTkFrame(app4,corner_radius=10,border_width=2,height=150,fg_color="#696969")
frame9.pack(padx=8,pady=7,fill="x")

#creating a label for inserting the image in frame and with some text 
img = ctk.CTkImage(dark_image=Image.open("C:\\Users\\hp\\Desktop\\java folder\\FIDS FOLDER\\flight logo.jpeg"),size=(100,70))
#creating a label for placing the image in frame 
labelimage=ctk.CTkLabel(master=frame9,image=img,text="")
labelimage.grid(row=0,column=0,padx=5,pady=7)

#creating a label for text of flights status and its departure time
flight_departure=ctk.CTkLabel(master=frame9,text="FLIGHT DEPARTURES", font=('BANKGOTHIC MD BT',35),text_color="yellow")
flight_departure.grid(row=0,column=1,padx=60,pady=10)

#create a timer or clock for rela time display management
clock_time=ctk.CTkLabel(master=frame9,text="",font=('BANKGOTHIC MD BT',30),text_color="yellow")
clock_time.grid(row=0,column=2,padx=2,pady=7)

#creating a label for Country for which time is displayed
country_label=ctk.CTkLabel(master=frame9,text="",font=('BANKGOTHIC MD BT',23),text_color="yellow")
country_label.grid(row=0,column=4,padx=6,pady=4)

#now creating another frame for updation of records fetched from the flight_data table as per the records mentioned 
frame10=ctk.CTkFrame(master=app4,corner_radius=10,border_width=2,fg_color="red",bg_color="black")
frame10.pack(padx=10,pady=10,fill='both',expand=True)

#now creating the treeview for fetching the records from the database
style=ttk.Style()
style.theme_use("clam")
style.configure("Treeview",font=('Calibri',20),rowheight=50)
style.configure("Treeview.Heading",font=('BANKGOTHIC MD BT',23))
#creating a treeview for displaying the records 
tv=ttk.Treeview(frame10,columns=(1,2,3,4,5,6,7),show="headings",style="Treeview",selectmode="browse")

#passing the headings and values in flight details window

tv.heading("1",text="Flight Time",anchor=tk.CENTER)
tv.heading("2",text="Destination",anchor=tk.CENTER)
tv.column("2",width=250)
tv.heading("3",text="Flight Name",anchor=tk.CENTER)
tv.column("3",width=300)
tv.heading("4",text="Flight Number",anchor=tk.CENTER)
tv.column("4",width=250)
tv.heading("5",text="Terminal",anchor=tk.CENTER)
tv.heading("6",text="Flight Status",anchor=tk.CENTER)
tv.column("6",width=250)
tv.heading("7",text="Gate",anchor=tk.CENTER)
tv.pack(fill='both',pady=10,padx=10,expand=True)
#calling the function clock for real time upadation of values in the display
clock()

#now calling the display function for fetching the details from the database with real time upadation
display()
app4.after(1000,display)
rotate_data()

app4.mainloop()
