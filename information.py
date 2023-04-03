 from tkinter import *
from tkinter import ttk

class Information:
    def __init__(self, root):
        self.root=root
        self.root.title("Information")
        self.root.geometry("1295x550+230+220")
        
        #title
        lbl_title=Label(self.root,text="Information",font=("times new roman",18,"bold"),bg="white",fg="green")
        lbl_title.place(x=0,y=0,width=1295,height=50)
        

        #label frame
        
        lableframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Citizen details",font=("times new roman",12,"bold"),padx=2)
        
        lableframeleft.place(x=5,y=50,width=425,height=490)
        ## labels and entry
        #citizen ref
        lbl_citizen_ref=Label(lableframeleft,text="Citizen ref",font=("times new roman",12,"bold"),bg="white")
        lbl_citizen_ref.grid(row=0,column=0,padx=10,pady=5,sticky="w")

        txt_citizen_ref=Entry(lableframeleft,font=("times new roman",12,"bold"),bg="lightyellow")

        txt_citizen_ref.grid(row=0,column=1,padx=10,pady=5,sticky="w")

         #citizen name
        lbl_citizen_name=Label(lableframeleft,text="Citizen Name",font=("times new roman",12,"bold"),bg="white")
        lbl_citizen_name.grid(row=1,column=0,padx=10,pady=5,sticky="w")

        txt_citizen_name=Entry(lableframeleft,font=("times new roman",12,"bold"),bg="lightyellow")

        txt_citizen_name.grid(row=1,column=1,padx=10,pady=5,sticky="w")
        
        #citizen ID
        lbl_citizen_ID=Label(lableframeleft,text="Citizen ID",font=("times new roman",12,"bold"),bg="white")
        lbl_citizen_ID.grid(row=2,column=0,padx=10,pady=5,sticky="w")

        txt_citizen_ID=Entry(lableframeleft,font=("times new roman",12,"bold"),bg="lightyellow")

        txt_citizen_ID.grid(row=2,column=1,padx=10,pady=5,sticky="w")
        
        #citizen DOB
        lbl_citizen_DOB=Label(lableframeleft,text="DOB",font=("times new roman",12,"bold"),bg="white")
        lbl_citizen_DOB.grid(row=3,column=0,padx=10,pady=5,sticky="w")

        txt_citizen_DOB=Entry(lableframeleft,font=("times new roman",12,"bold"),bg="lightyellow")

        txt_citizen_DOB.grid(row=3,column=1,padx=10,pady=5,sticky="w")
        #citizen gender with combobox
        lbl_citizen_gender=Label(lableframeleft,text="Gender",font=("times new roman",12,"bold"),bg="white")
        lbl_citizen_gender.grid(row=4,column=0,padx=10,pady=5,sticky="w")

        combo_gender=ttk.Combobox(lableframeleft,font=("arial",12,"bold"),state="readonly")
        combo_gender["value"]=("Male","Female","Other") 
        combo_gender.current(0)
        
        combo_gender.grid(row=4,column=1,padx=10,pady=5,sticky="w")
        
        #citizen Footer
        lbl_citizen_nationnality=Label(lableframeleft,text="Nationality",font=("times new roman",12,"bold"),bg="white")
        countries = ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda","Viet Nam" ]

        # create the combobox
        combo_nationality = ttk.Combobox(lableframeleft, font=("arial",12,"bold"), state="readonly")
        combo_nationality["values"] = countries
        combo_nationality.grid(row=6, column=1, padx=10, pady=5)
        ## citizen marriage status with combobox
        lbl_citizen_marriage=Label(lableframeleft,text="Marriage Status",font=("times new roman",12,"bold"),bg="white")
        lbl_citizen_marriage.grid(row=7,column=0,padx=10,pady=5,sticky="w")

        combo_marriage=ttk.Combobox(lableframeleft,font=("arial",12,"bold"),state="readonly")
        combo_marriage["value"]=("Married","Unmarried","Divorced",)
        combo_marriage.current(0)

        combo_marriage.grid(row=7,column=1,padx=10,pady=5,sticky="w")
        
         
       


        ## button frame
        btn_frame=Frame(lableframeleft,bd=2,relief=RIDGE,)
        btn_frame.place(x=0,y=400,width=412,height=40)
        
        #add button
        btn_add=Button(btn_frame,text="Add",font=("arial",11,"bold"),bg="black",fg="yellow",width=10)
        btn_add.grid(row=0,column=0)
        #update button  
        btn_update=Button(btn_frame,text="Update",font=("arial",11,"bold"),bg="black",fg="yellow",width=10)
        btn_update.grid(row=0,column=1)
        #delete button
        btn_delete=Button(btn_frame,text="Delete",font=("arial",11,"bold"),bg="black",fg="yellow",width=10)

        btn_delete.grid(row=0,column=2)
        #clear button
        btn_clear=Button(btn_frame,text="Clear",font=("arial",11,"bold"),bg="black",fg="yellow",width=10)
        btn_clear.grid(row=0,column=3)
        
        ##            Table SEARCH FRAME
        
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Citizen Information Details",font=("arial",12,"bold"),fg="gold",bg="white",padx=2)
        Table_Frame.place(x=435,y=50,width=860,height=490)
       
        lblSearch=Label(Table_Frame,text="Search By",font=("arial",12,"bold"),bg="white",fg="black")
        lblSearch.grid(row=0,column=0,padx=2,sticky="w")
        
        combo_Search=ttk.Combobox(Table_Frame,font=("arial",12,"bold"),state="readonly",width=10)
        combo_Search["value"]=["Citizen ref","Citizen ID","Citizen Name"]
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1)
        
        txt_Search=Entry(Table_Frame,font=("arial",13,"bold"),bg="lightyellow",bd=5,relief=GROOVE,width=25)
        txt_Search.grid(row=0,column=2,padx=2)
        
        btn_Search=Button(Table_Frame,text="Search By",font=("arial",11,"bold"),bg="black",fg="yellow",width=10)
        btn_Search.grid(row=0,column=3,padx=1)
        
        
        btn_ShowAll=Button(Table_Frame,text="Show All",font=("arial",11,"bold"),bg="black",fg="yellow",width=10)
        btn_ShowAll.grid(row=0,column=4,padx=1)
        


        

       
        
        
       
        ## data table
        
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=850,height=410)
        
        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
        

        self.Cust_Details_Table=ttk.Treeview(details_table,column=("Ref","Name","ID","DOB","Gender","Address","Nationality","Marriage"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("Ref",text="Ref")
        self.Cust_Details_Table.heading("Name",text="Name")
        self.Cust_Details_Table.heading("ID",text="ID")
        self.Cust_Details_Table.heading("DOB",text="DOB")
        self.Cust_Details_Table.heading("Gender",text="Gender")
        self.Cust_Details_Table.heading("Address",text="Address")
        self.Cust_Details_Table.heading("Nationality",text="nation")
        self.Cust_Details_Table.heading("Marriage",text="Marriage")
        
        self.Cust_Details_Table["show"]="headings"
        
    
        self.Cust_Details_Table.column("Ref",width=100)
        
        self.Cust_Details_Table.column("Name",width=100)
        self.Cust_Details_Table.column("ID",width=100)
        self.Cust_Details_Table.column("DOB",width=100)
        self.Cust_Details_Table.column("Gender",width=100)
        self.Cust_Details_Table.column("Address",width=100)
        self.Cust_Details_Table.column("Nationality",width=100)
        self.Cust_Details_Table.column("Marriage",width=100)


        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        

        
        

            
                    
        
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Information(root)
    root.mainloop()
