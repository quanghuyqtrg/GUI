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
        
        #citizen address
        lbl_citizen_address=Label(lableframeleft,text="Address",font=("times new roman",12,"bold"),bg="white")
        lbl_citizen_address.grid(row=5,column=0,padx=10,pady=5,sticky="w")

        txt_citizen_address=Entry(lableframeleft,font=("times new roman",12,"bold"),bg="lightyellow")

        txt_citizen_address.grid(row=5,column=1,padx=10,pady=5,sticky="w")

        #citizen Nationality with combobox
        lbl_citizen_nation=Label(lableframeleft,text="Nationality",font=("times new roman",12,"bold"),bg="white")

        lbl_citizen_nation.grid(row=6,column=0,padx=10,pady=5,sticky="w")

        # create a list of countries
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

    





            
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Information(root)
    root.mainloop()
