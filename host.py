# Importing all the modules from the tkinter library.
from tkinter import *
# Importing the ttk module from the tkinter library.
from tkinter import ttk
# Importing the random module.
import random
# Importing the time module.
import time 
# Importing the datetime module.
import datetime
# Importing the messagebox module from the tkinter library.
from tkinter import messagebox
# Importing the mysql.connector module.
import mysql.connector


class Hospital:
    def __init__(self,root):
        """
        The above function is used to create a window with a title and a size
        
        :param root: The root window is the main window of your application. It is the window that
        contains all other widgets
        """
        # The above function is used to create a window with a title and a size
        self.root=root
        # Setting the title of the window.
        self.root.title("Hospital Management System")
        # Setting the size of the window.
        self.root.geometry(# Setting the size of the window.
        "1540x800+0+0")
 # The above code is creating a label with the text "Hospital Management System" and the font size is
 
 
        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="[PUBLIC GOVERMENTAL SERVICES INFORMATION MANAGEMENT SYSTE]",fg="red",bg="white",font=("times new roman",50,"bold"))

        lbltitle.pack(side=TOP,fill=X)
        
        # Create the Dataframe
        Dataframe=Frame(self.root,bd=20,relief=RIDGE,padx=20)
        Dataframe.place(x=0,y=130,width=1530,height=400)
        
        DataframeLeft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,text="Patient Information",font=("times new roman",12,"bold"),fg="red")
        DataframeLeft.place(x=0,y=5,width=980,height=350)
        
        DataframeRight=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,text="Prescription",font=("times new roman",12,"bold"),fg="red")
        DataframeRight.place(x=990,y=5,width=460,height=350)
        
        ## Create buttons frame
        # Creating a frame for the buttons.
        Buttonframe=Frame(self.root,bd=20,relief=RIDGE,)
        Buttonframe.place(x=0,y=530,width=1530,height=70)
        
        ## create detail frame
        Detailsframe=Frame(self.root,bd=20,relief=RIDGE,)
        Detailsframe.place(x=0,y=600,width=1530,height=190)
        
        ##Create DataframeLeft
        lblName=Label(DataframeLeft,text="Name OF Tablet",font=("times new roman",12,"bold"),)
    
        lblName.grid(row=0,column=0,padx=10,pady=10,# Aligning the text to the left.
        sticky=W)
        
        comNameTablet=ttk.Combobox(DataframeLeft,font=("times new roman",12,"bold"),state="readonly",width=30)
        comNameTablet['values']=("","Paracetamol","Ibuprofen","Aspirin","Naproxen","Diclofenac","Acetaminophen","Ketoprofen","Dextropropoxyphene","Piroxicam","Fenoprofen","Flurbiprofen","Mefenamic Acid","Meclofenamate","Methocarbamol","Methyl Salicylate","Nabumetone","Nimesulide","Oxaprozin","Pentazocine","Piroxicam","Propoxyphene","Salsalate","Sulindac","Tolmetin","Tolmetin Sodium","Zomepirac")
        comNameTablet.grid(row=0,column=1,padx=10,pady=10)
        
        lblref=Label(DataframeLeft,font=("arial",12,"bold"),text="Reference No",)
        lblref.grid(row=1,column=0,padx=10,pady=10,sticky=W)
        txtref=Entry(DataframeLeft,font=("arial",13,"bold"),width=26)
        txtref.grid(row=1,column=1,padx=10,pady=10)
        
        lblref=Label(DataframeLeft,font=("arial",12,"bold"),text="Reference No",)
        lblref.grid(row=1,column=0,padx=10,pady=10,sticky=W)
        txtref=Entry(DataframeLeft,font=("arial",13,"bold"),width=26)
        txtref.grid(row=2,column=1,padx=10,pady=10)
        
        lblref=Label(DataframeLeft,font=("arial",12,"bold"),text="Reference No",)
        lblref.grid(row=1,column=0,padx=10,pady=10,sticky=W)
        txtref=Entry(DataframeLeft,font=("arial",13,"bold"),width=26)
        txtref.grid(row=3,column=1,padx=10,pady=10)
        
        lblref=Label(DataframeLeft,font=("arial",12,"bold"),text="Reference No",)
        lblref.grid(row=1,column=0,padx=10,pady=10,sticky=W)
        txtref=Entry(DataframeLeft,font=("arial",13,"bold"),width=26)
        txtref.grid(row=3,column=1,padx=10,pady=10)
        
        lblref=Label(DataframeLeft,font=("arial",12,"bold"),text="Reference No",)
        lblref.grid(row=1,column=0,padx=10,pady=10,sticky=W)
        txtref=Entry(DataframeLeft,font=("arial",13,"bold"),width=26)
        txtref.grid(row=4,column=1,padx=10,pady=10)
        
        lblref=Label(DataframeLeft,font=("arial",12,"bold"),text="Reference No",)
        lblref.grid(row=1,column=0,padx=10,pady=10,sticky=W)
        txtref=Entry(DataframeLeft,font=("arial",13,"bold"),width=26)
        txtref.grid(row=5,column=1,padx=10,pady=10)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        ## Create DataframeRight
        self.txtPrescription=Text(DataframeRight,font=("arial",12,"bold"),width=46,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)
        ## Create Buttonframe
        btnPrescription=Button(Buttonframe,bg="blue",fg="white",font=("arial",12,"bold"),width=27,height=16,padx=2,pady=2)
        btnPrescription.grid(row=0,column=0)
        
        btnPrescription=Button(Buttonframe,bg="blue",fg="white",font=("arial",12,"bold"),width=27,height=16,padx=2,pady=2)
        btnPrescription.grid(row=0,column=1)
        
        btnPrescription=Button(Buttonframe,bg="blue",fg="white",font=("arial",12,"bold"),width=27,height=16,padx=2,pady=2)
        btnPrescription.grid(row=0,column=2)
        
        btnPrescription=Button(Buttonframe,bg="blue",fg="white",font=("arial",12,"bold"),width=27,height=16,padx=2,pady=2)
        btnPrescription.grid(row=0,column=3)
        
        btnPrescription=Button(Buttonframe,bg="blue",fg="white",font=("arial",12,"bold"),width=27,height=16,padx=2,pady=2)
        btnPrescription.grid(row=0,column=4)
        
        btnPrescription=Button(Buttonframe,bg="blue",fg="white",font=("arial",12,"bold"),width=27,height=16,padx=2,pady=2)
        btnPrescription.grid(row=0,column=5)
        
# Create the root window
root = Tk()

# Create an instance of the Hospital class
hospital = Hospital(root)

# Start the mainloop
root.mainloop()