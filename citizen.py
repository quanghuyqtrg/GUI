
        
from tkinter import *
from PIL import Image, ImageTk

class CitizenInformation:
    def __init__(self, root):
        self.root = root
        self.root.title("Citizen Information")
        self.root.geometry("1350x700+0+0")

        # title
        lbl_title = Label(self.root, text="Citizen Information", font=("times new roman", 40, "bold"), bg="white", fg="green")
        lbl_title.place(x=0, y=110, width=1450, height=50)

         #main frame
        main_frame = Frame(self.root, bd=4, relief=RIDGE)       
        main_frame.place(x=0, y=160, width=1450, height=500)  
         # menu frame
        lbl_menu=Label(main_frame, text="Menu", font=("times new roman", 20, "bold"), bg="white", fg="green")
        lbl_menu.place(x=0, y=0, width=230) 
        # button frame
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=50, width=230, height=450)
        
        
         
        cust_btn = Button(btn_frame, text="Citizen infomation", font=("times new roman", 15, "bold"), bg="white", fg="green", cursor="hand2")
        cust_btn.grid(row=0, column=0, padx=10, pady=10, sticky="w")
          
        cust_btn = Button(btn_frame, text="Citizen infomation", font=("times new roman", 15, "bold"), bg="white", fg="green", cursor="hand2")
        cust_btn.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        
        cust_btn = Button(btn_frame, text="Citizen infomation", font=("times new roman", 15, "bold"), bg="white", fg="green", cursor="hand2")
        cust_btn.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        
        cust_btn = Button(btn_frame, text="Citizen infomation", font=("times new roman", 15, "bold"), bg="white", fg="green", cursor="hand2")
        cust_btn.grid(row=3, column=0, padx=10, pady=10, sticky="w")
         
         
         
         
         
         
         
         
         
         
root = Tk()
obj = CitizenInformation(root)
root.mainloop()
