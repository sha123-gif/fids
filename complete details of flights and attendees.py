#importing the required modules for creating the main project 

import customtkinter as ctk
from tkinter import END,ttk
from PIL import Image
import tkinter as tk
from tkinter import messagebox
import random 
import mysql.connector

#declaring the figure of app and its required settings in order to update and delete the details 

#declaring the appearence of app
ctk.set_appearance_mode("light")

#declaring the default color theme for upper ribbon 
ctk.set_default_color_theme("blue")

#declaring the size of window 
app=ctk.CTk()

#defining the geometry if window based application 
width= app.winfo_screenwidth()
height= app.winfo_screenheight()
app.geometry("%dx%d" % (width, height)) 

#defining the title of application 
app.title("Flight and Users Details Backup")

app.mainloop()