global root
root=0
from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
from tkinter import messagebox                             
import sqlite3 as c
from time import strftime,strptime
from datetime import datetime
import re
from tkcalendar import DateEntry
import subprocess


#--RESET ENTRY BOX

def reset():
    global labelframeleft
    global txtcname
    global txtfname
    global combo_gender
    global txtpostcode
    global txtmobile
    global txtemail
    global combo_nationality
    global combo_idproof
    global txtidnumber
    global txtaddress 
    global Cust_Details_Table

    while True:
        txtcname.delete(0)
        if txtcname.get()=="":
            break

    while True:
        txtfname.delete(0)
        if txtfname.get()=="":
            break

    while True:
        combo_gender.delete(0)
        if combo_gender.get()=="":
            break 
    while True:
        txtpostcode.delete(0)
        if len(txtpostcode.get())==0:
            break
    while True:
        txtmobile.delete(0)
        if len(txtmobile.get())==0:
            break
    while True:
        txtemail.delete(0)
        if txtemail.get()=="":
            break
    while True:
        combo_nationality.delete(0)
        if combo_nationality.get()=="":
            break
    
    while True:
        combo_idproof.delete(0)
        if combo_idproof.get()=="":
            break
        
    while True:
        txtidnumber.delete(0)
        if len(txtidnumber.get())==0:
            break

    while True:
        txtaddress.delete(0)
        if txtaddress.get()=="":
            break
    
    
    
    
    

#--GET CURSOR--#

def get_cuersor(event=""):#wrong spelling dale hai
    global labelframeleft
    global txtcname
    global txtfname
    global combo_gender
    global txtpostcode
    global txtmobile
    global txtemail
    global combo_nationality
    global combo_idproof
    global txtidnumber
    global txtaddress 
    global Cust_Details_Table
    global row

    cusrsor_row=Cust_Details_Table.focus()
    content=Cust_Details_Table.item(cusrsor_row)
    row=content["values"]
    #calling reset func
    reset()

    txtcname.insert(0,str(row[0]))
    txtfname.insert(0,str(row[1]))
    combo_gender.insert(0,str(row[2]))
    #combo box ko data entry samay correct value se check karwa lena hai
    txtpostcode.insert(0,str(row[3]))
    txtmobile.insert(0,str(row[4]))
    txtemail.insert(0,str(row[5]))
    combo_nationality.insert(0,str(row[6]))
    combo_idproof.insert(0,str(row[7]))
    txtidnumber.insert(0,str(row[8]))
    txtaddress.insert(0,str(row[9]))


#--CUSTOMER FRAME--#

def Custmain():
    global root
    
    root=Tk()

    root.title("Customer Details")
    root.geometry("1300x580+234+225")

    #title
    lbl_title=Label(root,text="ADD CUSTOMER DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
    lbl_title.place(x=0,y=0,width=1300,height=50)

    #global 
    
    global labelframeleft
    global txtcname
    global txtfname
    global combo_gender
    global txtpostcode
    global txtmobile
    global txtemail
    global combo_nationality
    global combo_idproof
    global txtidnumber
    global txtaddress 
    global combo_Search
    global txtSearch
    global row


    labelframeleft=LabelFrame(root,bd=2,relief=RIDGE,text="Customer Details",padx=2,font=("times new roman",18,"bold"))
    labelframeleft.place(x=5,y=50,width=425,height=490)

    #cust name

    cname=Label(labelframeleft,font=("arial",11,"bold"),text="Customer Name:",padx=10,pady=8)
    cname.grid(row=0,column=0,sticky=W)

    txtcname=ttk.Entry(labelframeleft,width=29,font=("times new roman",13,"bold"))
    txtcname.grid(row=0,column=1)

    #father name
    lblfname=Label(labelframeleft,font=("arial",11,"bold"),text="Father Name:",padx=10,pady=8)
    lblfname.grid(row=1,column=0,sticky=W)

    txtfname=ttk.Entry(labelframeleft,width=29,font=("times new roman",13,"bold"))
    txtfname.grid(row=1,column=1)
    
    #gender combobox

    label_gender=Label(labelframeleft,font=("arial",11,"bold"),text="Gender:",padx=10,pady=8)
    label_gender.grid(row=2,column=0,sticky=W)
    
    combo_gender=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=27)
    combo_gender["value"]=("Male","Female","Other")
    combo_gender.current(0)   
    combo_gender.grid(row=2,column=1)

    #post code

    lblpostcode=Label(labelframeleft,font=("arial",11,"bold"),text="Pin Code:",padx=10,pady=8)
    lblpostcode.grid(row=3,column=0,sticky=W)
        
    txtpostcode=ttk.Entry(labelframeleft,width=29,font=("times new roman",13,"bold"))
    txtpostcode.grid(row=3,column=1)

    # mobile number

    lblmobilenum=Label(labelframeleft,font=("arial",11,"bold"),text="Mobile Number:",padx=10,pady=8)
    lblmobilenum.grid(row=4,column=0,sticky=W)
        
    txtmobile=ttk.Entry(labelframeleft,width=29,font=("times new roman",13,"bold"))
    txtmobile.grid(row=4,column=1)

    #email

    lblemail=Label(labelframeleft,font=("arial",11,"bold"),text="Email:",padx=10,pady=8)
    lblemail.grid(row=5,column=0,sticky=W)
        
    txtemail=ttk.Entry(labelframeleft,width=29,font=("times new roman",13,"bold"))
    txtemail.grid(row=5,column=1)

    #nationality

    lblnationality=Label(labelframeleft,font=("arial",12,"bold"),text="Nationality:",padx=10,pady=8)
    lblnationality.grid(row=6,column=0,sticky=W)

    combo_nationality=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=27)
    combo_nationality["value"]=("Indian","American","Britist","Other")
    combo_nationality.current(0)
    combo_nationality.grid(row=6,column=1)

    #id proof type combobox

    lblidproof=Label(labelframeleft,font=("arial",12,"bold"),text="ID Proof Type:",padx=10,pady=8)
    lblidproof.grid(row=7,column=0,sticky=W)

    combo_idproof=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=27)
    combo_idproof["value"]=("Aadhaar Card","Driving Licence","Passport")
    combo_idproof.current(0)
    combo_idproof.grid(row=7,column=1)

    #id num

    lblidnum=Label(labelframeleft,font=("arial",11,"bold"),text="ID Number:",padx=10,pady=8)
    lblidnum.grid(row=8,column=0,sticky=W)
        
    txtidnumber=ttk.Entry(labelframeleft,width=29,font=("times new roman",13,"bold"))
    txtidnumber.grid(row=8,column=1)

    #address

    lbladdress=Label(labelframeleft,font=("arial",11,"bold"),text="Address:",padx=10,pady=8)
    lbladdress.grid(row=9,column=0,sticky=W)
        
    txtaddress=ttk.Entry(labelframeleft,width=29,font=("times new roman",13,"bold"))
    txtaddress.grid(row=9,column=1)

    #btns of cust

    btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
    btn_frame.place(x=0,y=420,width=417,height=40)


    #add btn in custbox

    btnAdd=Button(btn_frame,text="Add",command=add_dataCust,font=("arial",12,"bold"),bg="black",fg="gold",activeforeground="gold",activebackground="black",width=9,height=1)
    btnAdd.grid(row=0,column=0,padx=1,pady=2)

    #btn update

    btnUpdate=Button(btn_frame,text="Update",command=updatecust,font=("arial",12,"bold"),bg="black",fg="gold",activeforeground="gold",activebackground="black",width=9,height=1)
    btnUpdate.grid(row=0,column=1,padx=1,pady=2)

    #btn delete

    btnDelete=Button(btn_frame,text="Delete",command=deletecust,font=("arial",12,"bold"),bg="black",fg="gold",activeforeground="gold",activebackground="black",width=9,height=1)
    btnDelete.grid(row=0,column=2,padx=1,pady=2)

    #btn reset


    btnReset=Button(btn_frame,text="Reset",command=reset,font=("arial",12,"bold"),bg="black",fg="gold",activeforeground="gold",activebackground="black",width=10,height=1)
    btnReset.grid(row=0,column=3,padx=1,pady=2)

    #cust inside frame

    Table_Frame=LabelFrame(root,bd=2,relief=RIDGE,text="View Details And Search System",padx=2,font=("times new roman",13,"bold"))
    Table_Frame.place(x=435,y=50,width=860,height=490)

    #search by (red colour)
    lblSearchBy=Label(Table_Frame,font=("arial",12,"bold"),text="Search By",bg="red",fg="white")
    lblSearchBy.grid(row=0,column=0,sticky=W,padx=3)

    #search by

    combo_Search=ttk.Combobox(Table_Frame,font=("arial",12,"bold"),width=24,state="readonly")
    combo_Search["value"]=("Mobile","Idnumber")
    combo_Search.current(0)
    combo_Search.grid(row=0,column=1,padx=2)

    #search field

    txtSearch=ttk.Entry(Table_Frame,width=24,font=("times new roman",13,"bold"))
    txtSearch.grid(row=0,column=2,padx=2)

    btnSearch=Button(Table_Frame,text="Search",command=searchCust,font=("arial",12,"bold"),bg="black",fg="gold",activeforeground="gold",activebackground="black",width=10)
    btnSearch.grid(row=0,column=3,padx=1,pady=2)

    btnShowAll=Button(Table_Frame,text="Show All",command=fetch_dataCust,font=("arial",12,"bold"),bg="black",fg="gold",activeforeground="gold",activebackground="black",width=10)
    btnShowAll.grid(row=0,column=4,padx=1,pady=2)

    #show data table

    Details_Table=Frame(Table_Frame,bd=2,relief=RIDGE)
    Details_Table.place(x=0,y=50,width=860,height=350)

    #scroll bar 

    scroll_x=ttk.Scrollbar(Details_Table,orient=HORIZONTAL)
    scroll_y=ttk.Scrollbar(Details_Table,orient=VERTICAL)

    global Cust_Details_Table

    Cust_Details_Table=ttk.Treeview(Details_Table,column=("Name","Father","Gender","Pincode","Mobile","Email","Nationality","Idproof","Idnumber","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)

    scroll_x.config(command=Cust_Details_Table.xview)

    scroll_y.config(command=Cust_Details_Table.yview)

    #scroll bar column show like name,father,......

    Cust_Details_Table.heading("Name",text="Name")
    Cust_Details_Table.heading("Father",text="Father Name")
    Cust_Details_Table.heading("Gender",text="Gender")
    Cust_Details_Table.heading("Pincode",text="Pin Code")
    Cust_Details_Table.heading("Mobile",text="Mobile")
    Cust_Details_Table.heading("Email",text="Email")
    Cust_Details_Table.heading("Nationality",text="Nationality")
    Cust_Details_Table.heading("Idproof",text="ID Proof")
    Cust_Details_Table.heading("Idnumber",text="ID Number")
    Cust_Details_Table.heading("Address",text="Address")

    #show karenge avi headings

    Cust_Details_Table["show"]="headings"

    #width shape karre columns ka

    Cust_Details_Table.column("Name",width=100)
    Cust_Details_Table.column("Father",width=100)
    Cust_Details_Table.column("Gender",width=100)
    Cust_Details_Table.column("Pincode",width=100)
    Cust_Details_Table.column("Mobile",width=100)
    Cust_Details_Table.column("Email",width=100)
    Cust_Details_Table.column("Nationality",width=100)
    Cust_Details_Table.column("Idproof",width=100)
    Cust_Details_Table.column("Idnumber",width=100)
    Cust_Details_Table.column("Address",width=100)

    #pack karre phir expand then save karke apne adjust lelega

    Cust_Details_Table.pack(fill=BOTH,expand=1)

    Cust_Details_Table.bind("<ButtonRelease-1>",get_cuersor)

    fetch_dataCust()

    #add data in cust
    root.mainloop()


#--ADD CUST DATA--#

def add_dataCust():

    global labelframeleft
    global txtcname
    global txtfname
    global combo_gender
    global txtpostcode
    global txtmobile
    global txtemail
    global combo_nationality
    global combo_idproof
    global txtidnumber
    global txtaddress
    

    patternEM=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    mobile=str(txtmobile.get())
    email=str(txtemail.get())
    pin=str(txtpostcode.get())

    #Mobile number checking code

    def isvalidmobile(s):
        Pattern=re.compile("(0|91)?[6-9][0-9]{9}")
        return Pattern.match(s)
    
    def isvalidpin(s):
        global m
        regex = "^[1-9]{1}[0-9]{2}\\s{0,1}[0-9]{3}$"
        p=re.compile(regex);
        m=re.match(p,s);
        if m is None:
            messagebox.showerror("Error","Incorrect Pincode",parent=root)            
    
    isvalidpin(pin)


    if txtcname.get()=="" or txtfname.get()=="" or txtmobile.get()=="" or txtpostcode.get()=="" or txtemail.get()=="" or txtidnumber.get()=="" or txtaddress.get()=="":

        messagebox.showerror("Error","All fields are required",parent=root)

    elif not txtcname.get().isalpha or not txtfname.get().isalpha():
        messagebox.showerror("Error","Please Enter Data in Alphabets in the desired box",parent=root)
    elif not len(str(txtidnumber.get()))==12:
        messagebox.showerror("Error","ID Number should be 12 digit",parent=root)

    elif (isvalidmobile(mobile)) is None:
        messagebox.showerror("Error","Incorrect Mobile Number"+"\nPlease Enter Indian Mobile Number",parent=root)

    #email check
    elif (re.fullmatch(patternEM,email)) is None:
        messagebox.showerror("Error","Incorrect Email",parent=root)
    
    else:
        try:
            conn=c.connect("hotel.db")
            my_cursor=conn.cursor()
            
            my_cursor.execute("insert into customer (Name,Father,Gender,Pincode,Mobile,Email,Nationality,Idproof,Idnumber,Address)values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(str(txtcname.get()),str(txtfname.get()),combo_gender.get(),str(txtpostcode.get()),str(txtmobile.get()),str(txtemail.get()),str(combo_nationality.get()),str(combo_idproof.get()),str(txtidnumber.get()),str(txtaddress.get())))
            conn.commit()
            
            messagebox.showinfo("Success","Customer has been added",parent=root)
            fetch_dataCust() #fetch data call
            conn.close()
        except Exception as es:
            messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=root)


    root.mainloop()

#--UPDATE CUST--#

def updatecust():
    global labelframeleft
    global txtcname
    global txtfname
    global combo_gender
    global txtpostcode
    global txtmobile
    global txtemail
    global combo_nationality
    global combo_idproof
    global txtidnumber
    global txtaddress
    global row

    if txtcname.get()=="" or txtfname.get()=="" or txtmobile.get()=="" or txtpostcode.get()=="" or txtemail.get()=="" or txtidnumber.get()=="" or txtaddress.get()=="":
        messagebox.showerror("Error","All fields are required",parent=root)
    elif not txtcname.get().isalpha or not txtfname.get().isalpha():
        messagebox.showerror("Error","Please Enter Data in Alphabets in the desired box",parent=root)
    elif not len(str(txtidnumber.get()))==12:
        messagebox.showerror("Error","ID Number should be 12 digit",parent=root)
    else:
        try:
            conn=c.connect("hotel.db")
            my_cursor=conn.cursor()
            na=(txtcname.get())
            fa=str(txtfname.get())
            ge=str(combo_gender.get())
            po=str(txtpostcode.get())
            mo=(txtmobile.get())
            em=str(txtemail.get())
            nat=str(combo_nationality.get())
            idt=str(combo_idproof.get())
            idn=str(txtidnumber.get())
            ad=str(txtaddress.get())
            sql1="UPDATE customer SET Mobile='%s' WHERE Mobile='%s';"%(str(mo),row[4])
            sql2="UPDATE customer SET Mobile='%s' WHERE Mobile='%s';"%(str(mo),str(idn))
            sql3="UPDATE customer SET Pincode='%s' WHERE Mobile='%s';"%(po,str(mo))
            sql4="UPDATE customer SET Email='%s' WHERE Mobile='%s';"%(em,str(mo))
            sql5="UPDATE customer SET Nationality='%s' WHERE Mobile='%s';"%(nat,str(mo))
            sql6="UPDATE customer SET Address='%s' WHERE Mobile='%s';"%(ad,str(mo))
            
            my_cursor.execute(sql1)
            conn.commit()
            my_cursor.execute(sql2)
            conn.commit()
            my_cursor.execute(sql3)
            conn.commit()
            my_cursor.execute(sql4)
            conn.commit()
            my_cursor.execute(sql5)
            conn.commit()
            my_cursor.execute(sql6)
            conn.commit()

            conn.close()
            fetch_dataCust()
            messagebox.showinfo("Update","Customer details has been updated successfully",parent=root)
            
                

        except Exception as es:
            messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=root)
            fetch_dataCust()

    root.mainloop()




#--Delete Cust Data--#

def deletecust():

    global labelframeleft
    global txtcname
    global txtfname
    global combo_gender
    global txtpostcode
    global txtmobile
    global txtemail
    global combo_nationality
    global combo_idproof
    global txtidnumber
    global txtaddress

    mDelete=messagebox.askyesno("Hotel Management System","Do you want to delete this customer",parent=root)

    if txtcname.get()=="" or txtfname.get()=="" or txtmobile.get()=="" or txtpostcode.get()=="" or txtemail.get()=="" or txtidnumber.get()=="" or txtaddress.get()=="":
        messagebox.showerror("Error","All fields are required",parent=root)
    elif not txtcname.get().isalpha or not txtfname.get().isalpha():
        messagebox.showerror("Error","Please Enter Data in Alphabets in the desired box",parent=root)
    elif not len(str(txtidnumber.get()))==12:
        messagebox.showerror("Error","ID Number should be 12 digit",parent=root)
    elif mDelete>0:
        conn=c.connect("hotel.db")
        my_cursor=conn.cursor()
        mo=(txtmobile.get())
        sql="delete from customer where Mobile='%s'"%(str(mo))
        my_cursor.execute(sql)
        fetch_dataCust()
        conn.commit()
        conn.close()
        fetch_dataCust()
        messagebox.showinfo("Deleted","Customer details has been deleted successfully",parent=root)
        
    else:
        if not mDelete:
            return
    
    

#--search Cust Data--#
def searchCust():

    global combo_Search
    global txtSearch
    global Cust_Details_Table

    conn=c.connect("hotel.db")
    my_cursor=conn.cursor()
    my_cursor.execute("select * from customer where "+str(combo_Search.get())+" LIKE '"+str(txtSearch.get())+"%'")
    rows=my_cursor.fetchall()

    if len(rows)!=0:
        Cust_Details_Table.delete(*Cust_Details_Table.get_children(),)
        for i in rows:
            Cust_Details_Table.insert("",END,values=i)
        conn.commit()
    else:
        messagebox.showerror("Error","No Customer details found",parent=root)
    conn.close()

#--Fetch Cust Table Data--#

def fetch_dataCust():


    global labelframeleft
    global txtcname
    global txtfname
    global combo_gender
    global txtpostcode
    global txtmobile
    global txtemail
    global combo_nationality
    global combo_idproof
    global txtidnumber
    global txtaddress 
    global Cust_Details_Table

    conn=c.connect("hotel.db")
    my_cursor=conn.cursor()
    my_cursor.execute("select * from customer")
    rows=my_cursor.fetchall()
    if len(rows)!=0:
        Cust_Details_Table.delete(*Cust_Details_Table.get_children())
        for i in rows:
            Cust_Details_Table.insert("",END,values=i) #inserting into table
        conn.commit()
    conn.close()


#--Reset Room--#

def resetRoom():
    global txtcontact
    global txtcheck_in_date
    global txtcheck_out_date
    global combo_roomtype
    global combo_roomno
    global combo_meal
    global txtnoofdays
    global room_table
    global txtpaidtax
    global txtsubtotal
    global txttotalcost

    while True:
        txtcontact.delete(0)
        if len(txtcontact.get())==0:
            break

    while True:
        txtcheck_in_date.delete(0)
        if str(txtcheck_in_date.get())=="":
            break

    while True:
        txtcheck_out_date.delete(0)
        if str(txtcheck_out_date.get())=="":
            break 
    while True:
        combo_roomtype.delete(0)
        if str(combo_roomtype.get())=="":
            break
    while True:
        combo_roomno.delete(0)
        if str(combo_roomno.get())=="":
            break
    
    while True:
        combo_meal.delete(0)
        if str(combo_meal.get())=="":
            break
        
    while True:
        txtnoofdays.delete(0)
        if len(txtnoofdays.get())==0:
            break

    while True:
        txtpaidtax.delete(0)
        if str(txtpaidtax.get())=="":
            break

    while True:
        txtsubtotal.delete(0)
        if str(txtsubtotal.get())=="":
            break

    while True:
        txttotalcost.delete(0)
        if str(txttotalcost.get())=="":
            break



def resetbill():
    global txtnoofdays
    global room_table
    global txtpaidtax
    global txtsubtotal
    global txttotalcost

    while True:
            txtnoofdays.delete(0)
            if len(txtnoofdays.get())==0:
                break

    while True:
            txtpaidtax.delete(0)
            if len(txtpaidtax.get())==0:
                break

    while True:
            txtsubtotal.delete(0)
            if len(txtsubtotal.get())==0:
                break

    while True:
            txttotalcost.delete(0)
            if len(txttotalcost.get())==0:
                break
    
def showbill():
    global row
    global txtcontact
    global txtpaidtax
    global txtsubtotal
    global txttotalcost

    conn=c.connect("hotel.db")
    my_cursor=conn.cursor()
    sql="select Contact from room where Contact='%s'"%(str(txtcontact.get()))
    my_cursor.execute(sql)
    row1=my_cursor.fetchall()
    
    sql="select Mobile from customer where Mobile='%s'"%(str(txtcontact.get()))
    my_cursor.execute(sql)
    row2=my_cursor.fetchall()
    L=[]
    for i in row1:
        for j in i:
            L.append(j)
    L1=[]
    for k in row2:
        for l in i:
            L1.append(l)


    if str(txtcontact.get())=="":
        messagebox.showerror("Error","Enter contact in contact box to get bill",parent=root)
    elif str(txtnoofdays.get())=="" or str(txtpaidtax.get())=="" or str(txtsubtotal.get())=="" or str(txttotalcost.get())=="":
        messagebox.showerror("Error","Please Calculate Total First by Clicking Total Button",parent=root)
    
    elif str(txtcontact.get()) not in L1:
        messagebox.showerror("Error","No Customer Details Found",parent=root)
    elif str(txtcontact.get()) not in L:
        messagebox.showerror("Error","No Bookings Yet",parent=root)

    
    else:

        conn=c.connect("hotel.db")
        my_cursor=conn.cursor()
        sql="select Name from customer where Mobile='%s'"%(str(txtcontact.get()))
        my_cursor.execute(sql)
        row1=my_cursor.fetchone()
        filename="filebill.txt"
        f=open(filename,"w")
        f.write("-"*200+"\n")
        f.write("\t\t\t\t\t\tHOTEL ROYAL RESIDENCY"+"\n")
        f.write("-"*200)


        f.write("-"*200+"\n")
        f.write("\t\t\t\t\t\t\tBILL"+"\n")

    
        f.write("\n\t\t\t\t\t    "+"Name :-"+"\t\t"+row1[0])

        sql="select Gender from customer where Mobile='%s'"%(str(txtcontact.get()))
        my_cursor.execute(sql)
        row1=my_cursor.fetchone()
        f.write("\n\t\t\t\t\t    "+"Gender :-"+"\t\t"+row1[0])

        sql="select Pincode from customer where Mobile='%s'"%(str(txtcontact.get()))
        my_cursor.execute(sql)
        row1=my_cursor.fetchone()
        f.write("\n\t\t\t\t\t    "+"Pincode :-"+"\t\t"+row1[0])

        sql="select Mobile from customer where Mobile='%s'"%(str(txtcontact.get()))
        my_cursor.execute(sql)
        row1=my_cursor.fetchone()
        f.write("\n\t\t\t\t\t    "+"Mobile :-"+"\t\t"+row1[0])

        sql="select Nationality from customer where Mobile='%s'"%(str(txtcontact.get()))
        my_cursor.execute(sql)
        row1=my_cursor.fetchone()
        f.write("\n\t\t\t\t\t    "+"Nationality :-"+"\t\t"+row1[0])

        sql="select Idproof from customer where Mobile='%s'"%(str(txtcontact.get()))
        my_cursor.execute(sql)
        row1=my_cursor.fetchone()
        f.write("\n\t\t\t\t\t    "+"ID Proof :-"+"\t\t"+row1[0])

        sql="select Idnumber from customer where Mobile='%s'"%(str(txtcontact.get()))
        my_cursor.execute(sql)
        row1=my_cursor.fetchone()
        f.write("\n\t\t\t\t\t    "+"ID Number :-"+"\t\t"+row1[0])

        sql="select checkin from room where Contact='%s'"%(str(txtcontact.get()))
        my_cursor.execute(sql)
        row1=my_cursor.fetchone()
        f.write("\n\t\t\t\t\t    "+"Check In Date :-"+"\t\t"+row1[0])


        sql="select checkout from room where Contact='%s'"%(str(txtcontact.get()))
        my_cursor.execute(sql)
        row1=my_cursor.fetchone()
        f.write("\n\t\t\t\t\t    "+"Check Out Date :-"+"\t"+row1[0])

        sql="select roomtype from room where Contact='%s'"%(str(txtcontact.get()))
        my_cursor.execute(sql)
        row1=my_cursor.fetchone()
        f.write("\n\t\t\t\t\t    "+"Room Type :-"+"\t\t"+row1[0])

        sql="select roomavailable from room where Contact='%s'"%(str(txtcontact.get()))
        my_cursor.execute(sql)
        row1=my_cursor.fetchone()
        f.write("\n\t\t\t\t\t    "+"Room No. :-"+"\t\t"+row1[0])

        sql="select meal from room where Contact='%s'"%(str(txtcontact.get()))
        my_cursor.execute(sql)
        row1=my_cursor.fetchone()
        f.write("\n\t\t\t\t\t    "+"Meal :-"+"\t\t\t"+row1[0])

        sql="select noofdays from room where Contact='%s'"%(str(txtcontact.get()))
        my_cursor.execute(sql)
        row1=my_cursor.fetchone()
        f.write("\n\t\t\t\t\t    "+"No of Days :-"+"\t\t"+row1[0])

        f.write("\n\t\t\t\t\t    "+"Paid Tax :-"+"\t\t"+str(txtpaidtax.get()))
        f.write("\n\t\t\t\t\t    "+"Sub Total :-"+"\t\t"+str(txtsubtotal.get()))
        f.write("\n\t\t\t\t\t    "+"Total :-"+"\t\t\t"+str(txttotalcost.get()))
        f.write("\n"+"-"*200+"\n\n")
        f.write("*"*44+"   Thank You Visit Again\t"+"*"*100)

        f.flush()
        f.close()
        program="notepad.exe"
        subprocess.Popen([program,filename])



#get cursor room


def get_cuersorRoom(event=""):#wrong spelling dale hai
    global txtcontact
    global txtcheck_in_date
    global txtcheck_out_date
    global combo_roomtype
    global combo_roomno
    global combo_meal
    global txtnoofdays
    global room_table

    cusrsor_row=room_table.focus()
    content=room_table.item(cusrsor_row)
    row=content["values"]

    resetRoom()

    txtcontact.insert(0,str(row[0]))
    txtcheck_in_date.insert(0,str(row[1]))
    txtcheck_out_date.insert(0,str(row[2]))
    combo_roomtype.insert(0,str(row[3]))
    combo_roomno.insert(0,str(row[4]))
    combo_meal.insert(0,str(row[5]))


#--Room Booking--#

def Roombooking():

    global root
    
    global txtcontact
    global txtcheck_in_date
    global txtcheck_out_date
    global combo_roomtype
    global combo_roomno
    global combo_meal
    global txtnoofdays
    global room_table

    global combo_Searchroom
    global txtSearchroom
    
    global txtpaidtax
    global txtsubtotal
    global txttotalcost

    root=Tk()

    root.title("Room Booking")
    root.geometry("1300x580+234+225")

    #title roombooking
    lbl_title=Label(root,text="ROOM BOOKING DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
    lbl_title.place(x=0,y=0,width=1300,height=50)

    labelframeleft=LabelFrame(root,bd=2,relief=RIDGE,text="Room Booking Details",padx=2,font=("times new roman",18,"bold"))
    labelframeleft.place(x=5,y=65,width=425,height=504)

    #contact box

    lbl_contact=Label(labelframeleft,font=("arial",11,"bold"),text="Customer Contact:",padx=10,pady=8)
    lbl_contact.grid(row=0,column=0,sticky=W)

    txtcontact=ttk.Entry(labelframeleft,width=20,font=("times new roman",13,"bold"))
    txtcontact.grid(row=0,column=1,sticky=W)

    #fetch data button of contact

    btnfetchdata=Button(labelframeleft,command=fetchcontact,text="Fetch Data",font=("arial",8,"bold"),bg="black",fg="gold",width=8,height=1)
    btnfetchdata.place(x=350,y=4)

    #chech in date

    check_in_date=Label(labelframeleft,font=("arial",13,"bold"),text="Check in Date:",padx=10,pady=8)
    check_in_date.grid(row=1,column=0,sticky=W)

    txtcheck_in_date=DateEntry(labelframeleft,selectmode='day',date_pattern='dd/mm/y',width=21,font=("times new roman",14,"bold"))
    txtcheck_in_date.grid(row=1,column=1)

    #check out date

    check_out_date=Label(labelframeleft,font=("arial",13,"bold"),text="Check out Date:",padx=10,pady=8)
    check_out_date.grid(row=2,column=0,sticky=W)

    txtcheck_out_date=DateEntry(labelframeleft,selectmode='day',date_pattern='dd/mm/y',width=21,font=("times new roman",14,"bold"))
    txtcheck_out_date.grid(row=2,column=1)

    #room type

    
    label_roomtype=Label(labelframeleft,font=("arial",13,"bold"),text="Room Type:",padx=10,pady=8)
    label_roomtype.grid(row=3,column=0,sticky=W)

    conn=c.connect("hotel.db")
    my_cursor=conn.cursor()
    my_cursor.execute("select distinct roomtype from details")
    rowsroomtype=my_cursor.fetchall()

    combo_roomtype=ttk.Combobox(labelframeleft,font=("arial",13,"bold"),width=23)
    combo_roomtype["value"]=rowsroomtype
    combo_roomtype.current(0)
    combo_roomtype.grid(row=3,column=1)

    #available room 
    
    lblroomavailable=Label(labelframeleft,font=("arial",13,"bold"),text="Available Room:",padx=10,pady=8)
    lblroomavailable.grid(row=4,column=0,sticky=W)

    conn=c.connect("hotel.db")
    my_cursor=conn.cursor()
    my_cursor.execute("select roomavailable from details")
    rowsroomno=my_cursor.fetchall()


    combo_roomno=ttk.Combobox(labelframeleft,font=("arial",13,"bold"),width=23)
    combo_roomno["value"]=rowsroomno
    combo_roomno.current(0)
    combo_roomno.grid(row=4,column=1)

    #meal
    lblmeal=Label(labelframeleft,font=("arial",14,"bold"),text="Meal:",padx=10,pady=8)
    lblmeal.grid(row=5,column=0,sticky=W)

    combo_meal=ttk.Combobox(labelframeleft,font=("arial",13,"bold"),width=23)
    combo_meal["value"]=("Regular","Premium","No Meal")
    combo_meal.current(0)
    combo_meal.grid(row=5,column=1)

    #no of days
    lblnoofdays=Label(labelframeleft,font=("arial",14,"bold"),text="No of Days:",padx=10,pady=8)
    lblnoofdays.grid(row=6,column=0,sticky=W)

    txtnoofdays=ttk.Entry(labelframeleft,width=22,font=("times new roman",14,"bold"))
    txtnoofdays.grid(row=6,column=1)

    #Paid Tax

    lblpaidtax=Label(labelframeleft,font=("arial",14,"bold"),text=" Paid Tax:",padx=5,pady=8)
    lblpaidtax.grid(row=7,column=0,sticky=W)

    txtpaidtax=ttk.Entry(labelframeleft,width=22,font=("times new roman",14,"bold"))
    txtpaidtax.grid(row=7,column=1)

    #Sub total

    lblsubtotal=Label(labelframeleft,font=("arial",14,"bold"),text="Sub Total:",padx=10,pady=8)
    lblsubtotal.grid(row=8,column=0,sticky=W)

    txtsubtotal=ttk.Entry(labelframeleft,width=22,font=("times new roman",14,"bold"))
    txtsubtotal.grid(row=8,column=1)

    #total cost

    lbltotalcost=Label(labelframeleft,font=("arial",14,"bold"),text="Total Cost:",padx=10,pady=8)
    lbltotalcost.grid(row=9,column=0,sticky=W)

    txttotalcost=ttk.Entry(labelframeleft,width=22,font=("times new roman",14,"bold"))
    txttotalcost.grid(row=9,column=1)

    #bill button

    btnbill=Button(labelframeleft,text="Total",command=totaldaysautoRoom,font=("arial",11,"bold"),bg="black",fg="gold",width=8,height=1)
    btnbill.grid(row=10,column=0,padx=15,sticky=W)

    #show bill 

    btnshowbill=Button(labelframeleft,text="Show Bill",command=showbill,font=("arial",11,"bold"),bg="black",fg="gold",width=8,height=1)
    btnshowbill.grid(row=10,column=1,padx=80,sticky=W)

    #room booking buttons

    btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
    btn_frame.place(x=10,y=434,width=400,height=40)

    #add button in room 

    btnAdd=Button(btn_frame,text="Add",command=addRooom,font=("arial",12,"bold"),bg="black",fg="gold",width=9,height=1)
    btnAdd.grid(row=0,column=0,padx=1,pady=2)

    #btn update

    btnUpdate=Button(btn_frame,text="Update",command=updateroom,font=("arial",12,"bold"),bg="black",fg="gold",width=9,height=1)
    btnUpdate.grid(row=0,column=1,padx=1,pady=2)

    #btn delete

    btnDelete=Button(btn_frame,text="Delete",command=deleteroom,font=("arial",12,"bold"),bg="black",fg="gold",width=9,height=1)
    btnDelete.grid(row=0,column=2,padx=1,pady=2)

    #btn reset


    btnReset=Button(btn_frame,text="Reset",command=resetRoom,font=("arial",12,"bold"),bg="black",fg="gold",width=9,height=1)
    btnReset.grid(row=0,column=3,padx=1,pady=2)

     #room img
    

    imgroom=Image.open("images\\roomimg.jpg")
    imgroom=imgroom.resize((520,200),Image.ANTIALIAS)
    photoimgroom=ImageTk.PhotoImage(imgroom,master=root)

    lblimgroom=Label(root,image=photoimgroom,bd=0,relief=RIDGE)
    lblimgroom.image=photoimgroom
    lblimgroom.place(x=770,y=65,width=520,height=200)

    #search system for room
    Table_Frame=LabelFrame(root,bd=2,relief=RIDGE,text="View Details And Search System",padx=2,font=("times new roman",13,"bold"))
    Table_Frame.place(x=435,y=280,width=860,height=260)

    #search by (red colour)

    lblSearchBy=Label(Table_Frame,font=("arial",12,"bold"),text="Search By",bg="red",fg="white")
    lblSearchBy.grid(row=0,column=0,sticky=W,padx=3)

    #search type combo box

    combo_Searchroom=ttk.Combobox(Table_Frame,font=("arial",12,"bold"),width=24)
    combo_Searchroom["value"]=("contact","roomavailable")
    combo_Searchroom.current(0)
    combo_Searchroom.grid(row=0,column=1,padx=2)

    #search type field

    txtSearchroom=ttk.Entry(Table_Frame,width=24,font=("times new roman",13,"bold"))
    txtSearchroom.grid(row=0,column=2,padx=2)

    btnSearch=Button(Table_Frame,text="Search",command=searchroom,font=("arial",12,"bold"),bg="black",fg="gold",activeforeground="gold",activebackground="black",width=10)
    btnSearch.grid(row=0,column=3,padx=1,pady=2)

    btnShowAll=Button(Table_Frame,text="Show All",command=fetch_dataRoomTable,font=("arial",12,"bold"),bg="black",fg="gold",activeforeground="gold",activebackground="black",width=10)
    btnShowAll.grid(row=0,column=4,padx=1,pady=2)

    #show data table register wala.....

    Details_Table=Frame(Table_Frame,bd=2,relief=RIDGE)
    Details_Table.place(x=0,y=50,width=860,height=180)

        #scroll bar 

    scroll_x=ttk.Scrollbar(Details_Table,orient=HORIZONTAL)
    scroll_y=ttk.Scrollbar(Details_Table,orient=VERTICAL)

    room_table=ttk.Treeview(Details_Table,column=("contact","checkin","checkout","roomtype","roomavailable","meal","noofdays"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)

    scroll_x.config(command=room_table.xview)

    scroll_y.config(command=room_table.yview)

        #scroll bar column show like ref,name.....

    room_table.heading("contact",text="Contact")
    room_table.heading("checkin",text="Check-in")
    room_table.heading("checkout",text="Check-out")
    room_table.heading("roomtype",text="Room Type")
    room_table.heading("roomavailable",text="Room No.")
    room_table.heading("meal",text="Meal")
    room_table.heading("noofdays",text="No of Days")

    #show karenge avi headings

    room_table["show"]="headings"

        #width shape karre columns ka

    room_table.column("contact",width=100)
    room_table.column("checkin",width=100)
    room_table.column("checkout",width=100)
    room_table.column("roomtype",width=100)
    room_table.column("roomavailable",width=100)
    room_table.column("meal",width=100)
    room_table.column("noofdays",width=100)


        #pack karre phir expand then save karke apne adjust lelega
        
    room_table.pack(fill=BOTH,expand=1)

    room_table.bind("<ButtonRelease-1>",get_cuersorRoom)

    fetch_dataRoomTable()

    root.mainloop()

    



#--add roombooking--#

def addRooom(): 
    global txtcontact
    global txtcheck_in_date
    global txtcheck_out_date
    global combo_roomtype
    global combo_roomno
    global combo_meal
    global txtnoofdays
    global room_table

    #contact check from customer
    conn=c.connect("hotel.db")
    my_cursor=conn.cursor()
    sql=("select Mobile from customer")
    my_cursor.execute(sql)
    conn.commit()
    row=my_cursor.fetchall()
    L=[]
    for i in row:
        for j in i:
            L.append(j)
    conn.close()

    contact=txtcontact.get()
    def isvalidmobile(s):
        Pattern=re.compile("(0|91)?[6-9][0-9]{9}")
        return Pattern.match(s)


    inDate=txtcheck_in_date.get()
    outDate=txtcheck_out_date.get()
    inDate=datetime.strptime(inDate,"%d/%m/%Y")
    outDate=datetime.strptime(outDate,"%d/%m/%Y")
    x=(outDate-inDate).days
    

    if str(txtcontact.get())=="" or str(txtcheck_in_date.get())=="" or str(txtcheck_out_date.get())=="":
        messagebox.showerror("Error","All fields are required",parent=root)

    elif str(txtcontact.get()) not in L:
        messagebox.showerror("Error","This contact customer details is not available\nKindly add Customer Details First.",parent=root)

    elif (isvalidmobile(contact)) is None:
        messagebox.showerror("Error","Incorrect Mobile Number",parent=root)

    elif x<=0:
        messagebox.showerror("Error","Kindly add the Checkin Date and Checkout Date Correct",parent=root)

    
    else:

        try:
            conn=c.connect("hotel.db")
            my_cursor=conn.cursor()
            
            my_cursor.execute("insert into room (contact,checkin,checkout,roomtype,roomavailable,meal,noofdays)values('%s','%s','%s','%s','%s','%s','%s')"%(str(txtcontact.get()),str(txtcheck_in_date.get()),str(txtcheck_out_date.get()),str(combo_roomtype.get()),str(combo_roomno.get()),str(combo_meal.get()),str(txtnoofdays.get())))
            conn.commit()
            fetch_dataRoomTable() #fetch data call for room booking
            conn.close()
            messagebox.showinfo("Success","Room Booking has been done",parent=root)
        
        except Exception as es:
            messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=root)


#--Update Roombooking--#

def updateroom():
    global txtcontact
    global txtcheck_in_date
    global txtcheck_out_date
    global combo_roomtype
    global combo_roomno
    global combo_meal
    global txtnoofdays
    global room_table

    if str(txtcontact.get())=="":
        messagebox.showerror("Error","Please Enter Mobile Number",parent=root)
    
    else:
        try:
            conn=c.connect("hotel.db")
            my_cursor=conn.cursor()
            ca=(txtcontact.get())
            ci=str(txtcheck_in_date.get())
            co=str(txtcheck_out_date.get())
            rt=str(combo_roomtype.get())
            rn=(combo_roomno.get())
            me=str(combo_meal.get())
            nod=str(txtnoofdays.get())
            
            sql1="UPDATE room SET checkin='%s' WHERE contact='%s'"%(ci,str(ca))
            sql2="UPDATE room SET checkout='%s' WHERE contact='%s';"%(co,str(ca))
            sql3="UPDATE room SET roomtype='%s' WHERE contact='%s';"%(rt,str(ca))
            sql4="UPDATE room SET roomavailable='%s' WHERE contact='%s';"%(rn,str(ca))
            sql5="UPDATE room SET meal='%s' WHERE contact='%s';"%(me,str(ca))
            sql6="UPDATE room SET noofdays='%s' WHERE contact='%s';"%(nod,str(ca))

        
            
            my_cursor.execute(sql1)
            conn.commit()
            my_cursor.execute(sql2)
            conn.commit()
            my_cursor.execute(sql3)
            conn.commit()
            my_cursor.execute(sql4)
            conn.commit()
            my_cursor.execute(sql5)
            conn.commit()
            my_cursor.execute(sql6)
            conn.commit()

            
            conn.close()
            fetch_dataRoomTable()
            messagebox.showinfo("Update","Customer details has been updated successfully",parent=root)
        

        except Exception as es:
            messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=root)
            fetch_dataRoomTable()


    root.mainloop()



#--Delete Roombooking data--#

def deleteroom():
    mDelete=messagebox.askyesno("Hotel Management System","Do you want to delete this Roombooking",parent=root)
    if mDelete>0:
        conn=c.connect("hotel.db")
        my_cursor=conn.cursor()
        co=(txtcontact.get())
        sql="delete from room where contact='%s'"%(str(co))
        my_cursor.execute(sql)
        fetch_dataRoomTable()
        conn.commit()
        conn.close()
        fetch_dataRoomTable()
        messagebox.showinfo("Deleted","Customer details has been deleted successfully",parent=root)
        
    else:
        if not mDelete:
            return

#--Fetchcontact data button--#

def fetchcontact():

    if str(txtcontact.get())=="":
        messagebox.showerror("Error","Please enter contact number",parent=root)
    
    else:
        conn=c.connect("hotel.db")
        my_cursor=conn.cursor()

        sql="select Name from customer where Mobile='%s'"%(str(txtcontact.get()))
        my_cursor.execute(sql)
        row=my_cursor.fetchone()

        if row==None:
            messagebox.showerror("Error","This number is not found",parent=root)

        else:
            conn.commit()
            conn.close()

            #regis data fetch frame
            showdataframe=Frame(root,bd=4,relief=RIDGE,padx=2)
            showdataframe.place(x=450,y=85,width=300,height=180)

            #Name show 

            lblName=Label(showdataframe,text="Name:",font=("arial",12,"bold"))
            lblName.place(x=0,y=0)

            lblN=Label(showdataframe,text=row[0],font=("arial",12,"bold"))
            lblN.place(x=90,y=0)

            #gender show

            conn=c.connect("hotel.db")
            my_cursor=conn.cursor()
            sql="select Gender from customer where Mobile='%s'"%(str(txtcontact.get()))
            my_cursor.execute(sql)
            row=my_cursor.fetchone()

            lblGender=Label(showdataframe,text="Gender:",font=("arial",12,"bold"))
            lblGender.place(x=0,y=35)

            lblG=Label(showdataframe,text=row,font=("arial",12,"bold"))
            lblG.place(x=90,y=35)

            #email show

            conn=c.connect("hotel.db")
            my_cursor=conn.cursor()
            sql="select Email from customer where Mobile='%s'"%(str(txtcontact.get()))
            my_cursor.execute(sql)
            row=my_cursor.fetchone()

            lblEmail=Label(showdataframe,text="Email:",font=("arial",12,"bold"))
            lblEmail.place(x=0,y=70)

            lblE=Label(showdataframe,text=row[0],font=("arial",12,"bold"))
            lblE.place(x=90,y=70)

            #nationality show

            conn=c.connect("hotel.db")
            my_cursor=conn.cursor()
            sql="select Nationality from customer where Mobile='%s'"%(str(txtcontact.get()))
            my_cursor.execute(sql)
            row=my_cursor.fetchone()

            lblNationality=Label(showdataframe,text="Nationality:",font=("arial",12,"bold"))
            lblNationality.place(x=0,y=105)

            lblNN=Label(showdataframe,text=row,font=("arial",12,"bold"))
            lblNN.place(x=90,y=105)

            #address show

            conn=c.connect("hotel.db")
            my_cursor=conn.cursor()
            sql="select Address from customer where Mobile='%s'"%(str(txtcontact.get()))
            my_cursor.execute(sql)
            row=my_cursor.fetchone()

            lblAddress=Label(showdataframe,text="Address:",font=("arial",12,"bold"))
            lblAddress.place(x=0,y=135)

            lblA=Label(showdataframe,text=row,font=("arial",12,"bold"))
            lblA.place(x=90,y=135)


def searchroom():

    global combo_Searchroom
    global txtSearchroom
    global room_table

    conn=c.connect("hotel.db")
    my_cursor=conn.cursor()

    global combo_Searchroom
    global txtSearchroom
    global room_table

    my_cursor.execute("select * from room where "+str(combo_Searchroom.get())+" LIKE '"+str(txtSearchroom.get())+"%'")
    rows=my_cursor.fetchall()

    if len(rows)!=0:
        room_table.delete(*room_table.get_children(),)
        for i in rows:
            room_table.insert("",END,values=i)
        conn.commit()
        
    else:
        messagebox.showerror("Error","No Roombooking details found",parent=root)
    conn.close()


#--total bill--#

def totaldaysautoRoom():

    global txtcontact
    global txtcheck_in_date
    global txtcheck_out_date
    global combo_roomtype
    global combo_roomno
    global combo_meal
    global txtnoofdays
    global room_table
    global txtpaidtax
    global txtsubtotal
    global txttotalcost

    resetbill()

    inDate=txtcheck_in_date.get()
    outDate=txtcheck_out_date.get()
    inDate=datetime.strptime(inDate,"%d/%m/%Y")
    outDate=datetime.strptime(outDate,"%d/%m/%Y")
    txtnoofdays.insert(0,str(abs(outDate-inDate).days))
    


    inDateC=txtcheck_in_date.get()
    outDateC=txtcheck_out_date.get()
    inDateC=datetime.strptime(inDateC,"%d/%m/%Y")
    outDateC=datetime.strptime(outDateC,"%d/%m/%Y")
    x=(outDate-inDate).days
    if x<=0:
        messagebox.showerror("Error","Kindly add the Checkin Date and Checkout Date Correct",parent=root)

        
    elif str(combo_meal.get())=="Regular"and str(combo_roomtype.get())=="Single":
        q1=float(300) #food
        q2=float(700) #single
        q3=float(txtnoofdays.get())
        q4=float(q1+q2)
        q5=float(q3*q4)
        Tax="Rs."+str("%.2f"%((q5)*0.1))
        SubTotal="Rs."+str("%.2f"%(q5))
        TotalTax="Rs."+str("%.2f"%(q5+((q5)*0.1)))
        txtpaidtax.insert(0,Tax)
        txtsubtotal.insert(0,SubTotal)
        txttotalcost.insert(0,TotalTax)

    elif str(combo_meal.get())=="Regular"and str(combo_roomtype.get())=="Double":
        q1=float(300) #food
        q2=float(1000) #single
        q3=float(txtnoofdays.get())
        q4=float(q1+q2)
        q5=float(q3*q4)
        Tax="Rs."+str("%.2f"%((q5)*0.1))
        SubTotal="Rs."+str("%.2f"%(q5))
        TotalTax="Rs."+str("%.2f"%(q5+((q5)*0.1)))
        txtpaidtax.insert(0,Tax)
        txtsubtotal.insert(0,SubTotal)
        txttotalcost.insert(0,TotalTax)

    elif str(combo_meal.get())=="Regular"and str(combo_roomtype.get())=="Luxury":
        q1=float(300) #food
        q2=float(1500) #single
        q3=float(txtnoofdays.get())
        q4=float(q1+q2)
        q5=float(q3*q4)
        Tax="Rs."+str("%.2f"%((q5)*0.1))
        SubTotal="Rs."+str("%.2f"%(q5))
        TotalTax="Rs."+str("%.2f"%(q5+((q5)*0.1)))
        txtpaidtax.insert(0,Tax)
        txtsubtotal.insert(0,SubTotal)
        txttotalcost.insert(0,TotalTax)

    elif str(combo_meal.get())=="Premium"and str(combo_roomtype.get())=="Single":
        q1=float(500) #food
        q2=float(700) #single
        q3=float(txtnoofdays.get())
        q4=float(q1+q2)
        q5=float(q3*q4)
        Tax="Rs."+str("%.2f"%((q5)*0.1))
        SubTotal="Rs."+str("%.2f"%(q5))
        TotalTax="Rs."+str("%.2f"%(q5+((q5)*0.1)))
        txtpaidtax.insert(0,Tax)
        txtsubtotal.insert(0,SubTotal)
        txttotalcost.insert(0,TotalTax)

    elif str(combo_meal.get())=="Premium"and str(combo_roomtype.get())=="Double":
        q1=float(300) #food
        q2=float(1000) #single
        q3=float(txtnoofdays.get())
        q4=float(q1+q2)
        q5=float(q3*q4)
        Tax="Rs."+str("%.2f"%((q5)*0.1))
        SubTotal="Rs."+str("%.2f"%(q5))
        TotalTax="Rs."+str("%.2f"%(q5+((q5)*0.1)))
        txtpaidtax.insert(0,Tax)
        txtsubtotal.insert(0,SubTotal)
        txttotalcost.insert(0,TotalTax)

    elif str(combo_meal.get())=="Premium"and str(combo_roomtype.get())=="Luxury":
        q1=float(500) #food
        q2=float(1500) #single
        q3=float(txtnoofdays.get())
        q4=float(q1+q2)
        q5=float(q3*q4)
        Tax="Rs."+str("%.2f"%((q5)*0.1))
        SubTotal="Rs."+str("%.2f"%(q5))
        TotalTax="Rs."+str("%.2f"%(q5+((q5)*0.1)))
        txtpaidtax.insert(0,Tax)
        txtsubtotal.insert(0,SubTotal)
        txttotalcost.insert(0,TotalTax)

    elif str(combo_meal.get())=="No Meal"and str(combo_roomtype.get())=="Single":
        q1=float(100) #food
        q2=float(700) #single
        q3=float(txtnoofdays.get())
        q4=float(q1+q2)
        q5=float(q3*q4)
        Tax="Rs."+str("%.2f"%((q5)*0.1))
        SubTotal="Rs."+str("%.2f"%(q5))
        TotalTax="Rs."+str("%.2f"%(q5+((q5)*0.1)))
        txtpaidtax.insert(0,Tax)
        txtsubtotal.insert(0,SubTotal)
        txttotalcost.insert(0,TotalTax)

    elif str(combo_meal.get())=="No Meal"and str(combo_roomtype.get())=="Double":
        q1=float(100) #food
        q2=float(1000) #single
        q3=float(txtnoofdays.get())
        q4=float(q1+q2)
        q5=float(q3*q4)
        Tax="Rs."+str("%.2f"%((q5)*0.1))
        SubTotal="Rs."+str("%.2f"%(q5))
        TotalTax="Rs."+str("%.2f"%(q5+((q5)*0.1)))
        txtpaidtax.insert(0,Tax)
        txtsubtotal.insert(0,SubTotal)
        txttotalcost.insert(0,TotalTax)


    elif str(combo_meal.get())=="No Meal"and str(combo_roomtype.get())=="Luxury":
        q1=float(100) #food
        q2=float(1500) #single
        q3=float(txtnoofdays.get())
        q4=float(q1+q2)
        q5=float(q3*q4)
        Tax="Rs."+str("%.2f"%((q5)*0.1))
        SubTotal="Rs."+str("%.2f"%(q5))
        TotalTax="Rs."+str("%.2f"%(q5+((q5)*0.1)))
        txtpaidtax.insert(0,Tax)
        txtsubtotal.insert(0,SubTotal)
        txttotalcost.insert(0,TotalTax)

#--Fetch Data Room Table

def fetch_dataRoomTable():
    global txtcontact
    global txtcheck_in_date
    global txtcheck_out_date
    global combo_roomtype
    global combo_roomno
    global combo_meal
    global txtnoofdays
    global room_table

    conn=c.connect("hotel.db")
    my_cursor=conn.cursor()
    my_cursor.execute("select * from room")
    rows=my_cursor.fetchall()
    if len(rows)!=0:
        room_table.delete(*room_table.get_children())
        for i in rows:
            room_table.insert("",END,values=i) #inserting into table
        conn.commit()
    conn.close()

#--End of Room--#

def DetailsBar(): 
    global root
    
    root=Tk()

    root.title("Hotel Management Details")
    root.geometry("1300x580+234+225")

    global txtfloor
    global txtroomno
    global combo_roomtypeD
    global room_table

    #title
    lbl_title=Label(root,text="ROOM BOOKING DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
    lbl_title.place(x=0,y=0,width=1300,height=50)

    #hotel logo


    #label frame(cust details)

    labelframeleft=LabelFrame(root,bd=2,relief=RIDGE,text="New Room Add",padx=2,font=("times new roman",18,"bold"))
    labelframeleft.place(x=5,y=50,width=425,height=290)

    #contact box

    lbl_floor=Label(labelframeleft,font=("arial",13,"bold"),text="Floor:",padx=10,pady=8)
    lbl_floor.grid(row=0,column=0,sticky=W)

    txtfloor=ttk.Entry(labelframeleft,width=20,font=("times new roman",13,"bold"))
    txtfloor.grid(row=0,column=1,sticky=W)

    #room no 

    lbl_room=Label(labelframeleft,font=("arial",13,"bold"),text="Room No:",padx=10,pady=8)
    lbl_room.grid(row=1,column=0,sticky=W)

    txtroomno=ttk.Entry(labelframeleft,width=20,font=("times new roman",13,"bold"))
    txtroomno.grid(row=1,column=1,sticky=W)
    
    #room type

    label_roomtypeD=Label(labelframeleft,font=("arial",11,"bold"),text="Room Type:",padx=10,pady=8)
    label_roomtypeD.grid(row=2,column=0,sticky=W)

    combo_roomtypeD=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=18)
    combo_roomtypeD["value"]=("Single","Double","Luxury")
    combo_roomtypeD.current(0)
    combo_roomtypeD.grid(row=2,column=1)


    #details table buttons

    btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
    btn_frame.place(x=0,y=220,width=417,height=40)

        #add btn in custbox

    btnAdd=Button(btn_frame,text="Add",command=adddetails,font=("arial",12,"bold"),bg="black",fg="gold",width=9,height=1)
    btnAdd.grid(row=0,column=0,padx=1,pady=2)

    #btn update

    btnUpdate=Button(btn_frame,text="Update",command=updatedetails,font=("arial",12,"bold"),bg="black",fg="gold",width=9,height=1)
    btnUpdate.grid(row=0,column=1,padx=1,pady=2)

    #btn delete

    btnDelete=Button(btn_frame,text="Delete",command=deletedetails,font=("arial",12,"bold"),bg="black",fg="gold",width=9,height=1)
    btnDelete.grid(row=0,column=2,padx=1,pady=2)

    #btn reset


    btnReset=Button(btn_frame,text="Reset",command=resetDetails,font=("arial",12,"bold"),bg="black",fg="gold",width=10,height=1)
    btnReset.grid(row=0,column=3,padx=1,pady=2)


   
    #table frame

    Table_Frame=LabelFrame(root,bd=2,relief=RIDGE,text="Show Room Details",padx=2,font=("times new roman",13,"bold"))
    Table_Frame.place(x=600,y=55,width=600,height=350)

    #scroll bar with coloumn name 

    scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
    scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)


    room_table=ttk.Treeview(Table_Frame,column=("floor","roomavailable","roomtype"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)

    scroll_x.config(command=room_table.xview)

    scroll_y.config(command=room_table.yview)

    #heading

    room_table.heading("floor",text="Floor")
    room_table.heading("roomavailable",text="Room No")
    room_table.heading("roomtype",text="Room Type")

    #show karenge avi headings

    room_table["show"]="headings"

        #width shape karre columns ka

    room_table.column("floor",width=100)
    room_table.column("roomavailable",width=100)
    room_table.column("roomtype",width=100)

    #pack karre phir expand then save karke apne adjust lelega
        
    room_table.pack(fill=BOTH,expand=1)

    #bind get cursor

    room_table.bind("<ButtonRelease-1>",get_cuersorDetails)

    fetch_dataDetailsTable()


def adddetails():

    global txtfloor
    global txtroomno
    global combo_roomtypeD
    global room_table

    if str(txtfloor.get())=="" or str(txtroomno.get())=="" or str(combo_roomtypeD.get())=="":

        messagebox.showerror("Error","All fields are required",parent=root)

    elif not str(txtfloor.get()).isdigit():
        messagebox.showerror("Error","Please enter floor in digits",parent=root)

    elif not str(txtroomno.get()).isdigit():
        messagebox.showerror("Error","Please enter Room No in digits",parent=root)

    else:
        try:
            conn=c.connect("hotel.db")
            my_cursor=conn.cursor()

            my_cursor.execute("insert into details (floor,roomavailable,roomtype)values('%s','%s','%s')"%(str(txtfloor.get()),str(txtroomno.get()),str(combo_roomtypeD.get())))
            conn.commit()
            fetch_dataDetailsTable()

            conn.close()
            messagebox.showinfo("Success","New Room Added Successfully",parent=root)
            funcresetdetails()

        except Exception as es:
            messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=root)

#--Update Details--#
def updatedetails():
    global txtfloor
    global txtroomno
    global combo_roomtypeD
    global room_table

    if str(txtfloor.get())=="" or str(txtroomno.get())=="" or str(combo_roomtypeD.get())=="":

        messagebox.showerror("Error","All fields are required",parent=root)

    elif not str(txtfloor.get()).isdigit():
        messagebox.showerror("Error","Please enter floor in digits",parent=root)

    elif not str(txtroomno.get()).isdigit():
        messagebox.showerror("Error","Please enter Room No in digits",parent=root)

    else:
        try:
            conn=c.connect("hotel.db")
            my_cursor=conn.cursor()
            fl=str(txtfloor.get())
            rn=txtroomno.get()
            rd=str(combo_roomtypeD.get())
        
            sql1="UPDATE details SET floor='%s' WHERE roomavailable=='%s'"%(fl,str(rn))
            sql2="UPDATE details SET roomtype='%s' WHERE roomavailable='%s';"%(rd,str(rn))
        
            
            my_cursor.execute(sql1)
            conn.commit()
            my_cursor.execute(sql2)
            conn.commit()
        
            
            conn.close()
            fetch_dataDetailsTable()
            messagebox.showinfo("Update","Customer details has been updated successfully",parent=root)
            funcresetdetails()
        

        except Exception as es:
            messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=root)
            fetch_dataDetailsTable()


    root.mainloop()


#--Delete Details--#

def deletedetails():

    global txtfloor
    global txtroomno
    global combo_roomtypeD
    global room_table

    mDelete=messagebox.askyesno("Hotel Management System","Do you want to delete this Room Details",parent=root)
    if mDelete>0:
        conn=c.connect("hotel.db")
        my_cursor=conn.cursor()
        rn=(txtroomno.get())
        sql="delete from details where roomavailable='%s'"%(str(rn))
        my_cursor.execute(sql)
        fetch_dataDetailsTable()
        conn.commit()
        conn.close()
        fetch_dataDetailsTable()
        messagebox.showinfo("Deleted","Customer details has been deleted successfully",parent=root)
        funcresetdetails()
        
    else:
        if not mDelete:
            return


def fetch_dataDetailsTable():

    global txtfloor
    global txtroomno
    global combo_roomtypeD
    global room_table

    conn=c.connect("hotel.db")
    my_cursor=conn.cursor()
    my_cursor.execute("select * from details")
    rows=my_cursor.fetchall()
    if len(rows)!=0:
        room_table.delete(*room_table.get_children())
        for i in rows:
            room_table.insert("",END,values=i) #inserting into table
        conn.commit()
    conn.close()

#--Get cursor--#


def get_cuersorDetails(event=""):#wrong spelling dale hai

    global txtfloor
    global txtroomno
    global combo_roomtypeD
    global room_table

    cusrsor_row=room_table.focus()
    content=room_table.item(cusrsor_row)
    row=content["values"]

    resetDetails()

    txtfloor.insert(0,str(row[0])),
    txtroomno.insert(0,str(row[1])),
    combo_roomtypeD.insert(0,str(row[2]))
def funcresetdetails():
    #after update add or delete
    global txtfloor
    global txtroomno
    global combo_roomtypeD
    global room_table


    while True:
            txtfloor.delete(0)
            if len(txtfloor.get())==0:
                break

    while True:
            txtroomno.delete(0)
            if len(txtroomno.get())==0:
                break

def resetDetails():
    global txtfloor
    global txtroomno
    global combo_roomtypeD
    global room_table


    while True:
            txtfloor.delete(0)
            if len(txtfloor.get())==0:
                break

    while True:
            txtroomno.delete(0)
            if len(txtroomno.get())==0:
                break

    while True:
        combo_roomtypeD.delete(0)
        if str(combo_roomtypeD.get())=="":
            break

def adminsmain():

    global root
    global txtuser
    global txtpass
    global admin_table
    global photoimg1
    global fname_entry
    global l_entry
    global txt_contact
    global txt_recode
    global txt_pass
    global txt_conpass
    
    root=Tk()

    root.title("Hotel Management Details")
    root.geometry("1300x580+234+225")

    img4=Image.open("images\\adminsimg.jpg")
    img4=img4.resize((1310,610),Image.ANTIALIAS)
    photoimg4=ImageTk.PhotoImage(img4,master=root)



    lblimg=Label(root,image=photoimg4,bd=4,relief=RIDGE)
    lblimg.image=photoimg4
    lblimg.place(x=0,y=0,width=1310,height=610)

    #inner black frame
    frame=Frame(root,bg="black")
    frame.place(x=453,y=85,width=340,height=450)

    img1=Image.open(r"images\loginicon.png")
    img1=img1.resize((100,100),Image.ANTIALIAS)
    photoimage1=ImageTk.PhotoImage(img1,master=root)
    lblimg1=Label(root,image=photoimage1,bg="black",borderwidth=0)
    lblimg1.image=photoimg1
    lblimg1.place(x=575,y=105,width=100,height=100)

    #get started label

    get_str=Label(frame,text="Welcome to Admins Pannel",font=("times new roman",14,"bold"),fg="white",bg="black")
    get_str.place(x=58,y=130)

    #user name label

    username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
    username.place(x=60,y=184)
        
    txtuser=ttk.Entry(frame,font=("times new roman",13,"bold"))       
    txtuser.place(x=35,y=210,width=270)

        #password label

    password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
    password.place(x=60,y=262)

    txtpass=ttk.Entry(frame,font=("times new roman",13,"bold"),show="*")       
    txtpass.place(x=35,y=290,width=270)

    #Icon Images of username 

    img2=Image.open(r"images\loginusericon.png")
    img2=img2.resize((25,25),Image.ANTIALIAS)
    photoimage2=ImageTk.PhotoImage(img2,master=root)
    lblimg1=Label(root,image=photoimage2,bg="black",borderwidth=0)
    lblimg1.place(x=490,y=268,width=25,height=25)

        #Icon Images of password

    img3=Image.open(r"images\loginpassicon.png")
    img3=img3.resize((55,25),Image.ANTIALIAS)
    photoimage3=ImageTk.PhotoImage(img3,master=root)
    lblimg1=Label(root,image=photoimage3,bg="black",borderwidth=0)
    lblimg1.place(x=490,y=345,width=25,height=25)
    
    def click():
        if txtuser.get() == "Pranav" and txtpass.get() == "pranav123" :
            root.destroy()
            admintable()

    loginbtn=Button(root,command=click,text="Login",font=("times new roman",13,"bold"),bd=3,relief=RIDGE,fg="black",bg="aqua",activeforeground="black",activebackground="aqua")
    loginbtn.place(x=561,y=420,width=120,height=35)
    root.mainloop()

def admintable():
    global admin_table
    global photoimg1
    global fname_entry
    global l_entry
    global txt_contact
    global txt_recode
    global txt_pass
    global txt_conpass

    root=Tk()

    root.title("Hotel Management Details")
    root.geometry("1300x580+234+225")

    lbl_admtable=Label(root,text="ADMINS TABLE",font=("times new roman",30,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
    lbl_admtable.place(x=0,y=2,width=1300,height=90)
    #table frame

    Table_Frame=LabelFrame(root,bd=2,relief=RIDGE,text="Show Admins Details",padx=2,font=("times new roman",13,"bold"))
    Table_Frame.place(x=0,y=100,width=1300,height=570)

    #scroll bar with coloumn name 

    scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
    scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)

    admin_table=ttk.Treeview(Table_Frame,column=("fullname","username","contact","recode","pass"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)

    scroll_x.config(command=admin_table.xview)

    scroll_y.config(command=admin_table.yview)

    #heading

    admin_table.heading("fullname",text="Name")
    admin_table.heading("username",text="User Name")
    admin_table.heading("contact",text="Contact")
    admin_table.heading("recode",text="Recovery Code")
    admin_table.heading("pass",text="Password")

    #show karenge avi headings

    admin_table["show"]="headings"

        #width shape karre columns ka

    admin_table.column("fullname",width=100,anchor=CENTER)
    admin_table.column("username",width=100,anchor=CENTER)
    admin_table.column("contact",width=100,anchor=CENTER)
    admin_table.column("recode",width=100,anchor=CENTER)
    admin_table.column("pass",width=100,anchor=CENTER)

    #pack karre phir expand then save karke apne adjust lelega
        
    admin_table.pack(fill=BOTH,expand=1)

    fetch_dataAdminsTable()

    root.mainloop()
#--Fetch Data Admins--#

def fetch_dataAdminsTable():


    global admin_table

    conn=c.connect("hotel.db")
    my_cursor=conn.cursor()
    my_cursor.execute("select * from login")
    rows=my_cursor.fetchall()
    if len(rows)!=0:
        admin_table.delete(*admin_table.get_children())
        for i in rows:
            admin_table.insert("",END,values=i) #inserting into table
        conn.commit()
    conn.close()




#--Main--#

#--ADD TABLES--#

def addtables():
    conn=c.connect("hotel.db")
    my_cursor=conn.cursor()
    sql="CREATE TABLE if not exists customer (\
        Name varchar(30),\
        Father varchar(30),\
        Gender char(15),\
        Pincode varchar(20),\
        Mobile varchar(10),\
        Email varchar(50),\
        Nationality varchar(50),\
        Idproof varchar(20),\
        Idnumber varchar(20) UNIQUE,\
        Address varchar(20),\
        PRIMARY KEY (Mobile));"
    my_cursor.execute(sql)

    sql="CREATE TABLE if not exists room (\
        contact varchar(30),\
        checkin varchar(30),\
        checkout varchar(30),\
        roomtype varchar(30),\
        roomavailable varchar(30),\
        meal varchar(30),\
        noofdays varchar(30),\
        PRIMARY KEY (contact));"
    my_cursor.execute(sql)

    sql="CREATE TABLE if not exists details (\
        floor varchar(30),\
        roomavailable varchar(30),\
        roomtype varchar(30),\
        PRIMARY KEY (roomavailable));"
    my_cursor.execute(sql)

    sql="CREATE TABLE if not exists login (\
        fullname varchar(30),\
        username varchar(30) UNIQUE,\
        contact varchar(30),\
        recode varchar(30),\
        pass varchar(30),\
        conpass varchar(30),\
        PRIMARY KEY (recode));"
    my_cursor.execute(sql)


#--MAIN--#
def Devilmain():
    rootmain=Tk() 
    rootmain.title("Hotel Management System")
    rootmain.geometry("1550x890+0+0")



    global labelframeleft
    global txtcname
    global txtfname
    global combo_gender
    global txtpostcode
    global txtmobile
    global txtemail
    global combo_nationality
    global combo_idproof
    global txtidnumber
    global txtaddress 
    global Cust_Details_Table
    global photoimg1


    #image 1 upper right corner
    img1=Image.open(r"images\2000x700.jpg")
    img1=img1.resize((410,140),Image.ANTIALIAS)
    photoimg1=ImageTk.PhotoImage(img1)

    lblimg=Label(rootmain,image=photoimg1,bd=4,relief=RIDGE)
    lblimg.place(x=1126,y=0,width=410,height=140)

    #image 2 upper middle corner
    img2=Image.open(r"images\1550x170.jfif")
    img2=img2.resize((400,140),Image.ANTIALIAS)
    photoimg2=ImageTk.PhotoImage(img2)

    lblimg=Label(rootmain,image=photoimg2,bd=4,relief=RIDGE)
    lblimg.place(x=730,y=0,width=400,height=140)

    #image 3 upper left corner
    img3=Image.open(r"images\3rdimageupperpart.jpg")
    img3=img3.resize((400,140),Image.ANTIALIAS)
    photoimg3=ImageTk.PhotoImage(img3)

    lblimg=Label(rootmain,image=photoimg3,bd=4,relief=RIDGE)
    lblimg.place(x=330,y=0,width=400,height=140)

    #logo full left corner

    imgl=Image.open("images\\logo.png")
    imgl=imgl.resize((330,140),Image.ANTIALIAS)
    photoimgl=ImageTk.PhotoImage(imgl)

    lblimgl=Label(rootmain,image=photoimgl,bd=4,relief=RIDGE)
    lblimgl.place(x=0,y=0,width=330,height=140)

        #title "HOTEL MANAGEMENT SYSTEM"

    lbl_title=Label(rootmain,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
    lbl_title.place(x=0,y=140,width=1550,height=50)

    def time():
        string=strftime('%H:%M:%S %p')
        lbl.config(text=string)
        lbl.after(1000,time)
    lbl=Label(lbl_title,font=("Times New Roman",16,"bold"),bg="black",fg="gold")
    lbl.place(x=15,y=1,width=120,height=37)
    time()



        #MAIN FRAME

    main_frame=Frame(rootmain,bd=4,relief=RIDGE)
    main_frame.place(x=0,y=190,width=1550,height=620)

    #MENU

    lbl_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
    lbl_menu.place(x=1,y=0 ,width=230)

        #BTN FRAME 

    btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
    btn_frame.place(x=0,y=40,width=228,height=190)

    #customer btn

    cust_btn=Button(btn_frame,text="CUSTOMER",command=Custmain,width=20,font=("times new roman",14,"bold"),bg="black",fg="gold",activeforeground="gold",activebackground="black",bd=0,cursor="hand2")
    cust_btn.grid(row=0,column=0,pady=1)

        #room btn
    
    room_btn=Button(btn_frame,text="ROOM",command=Roombooking,width=20,font=("times new roman",14,"bold"),bg="black",fg="gold",activeforeground="gold",activebackground="black",bd=0,cursor="hand2")
    room_btn.grid(row=1,column=0,pady=1)

        #details btn

    details_btn=Button(btn_frame,text="DETAILS",width=20,command=DetailsBar,font=("times new roman",14,"bold"),bg="black",fg="gold",activeforeground="gold",activebackground="black",bd=0,cursor="hand2")
    details_btn.grid(row=2,column=0,pady=1)

        #admins btn

    admins_btn=Button(btn_frame,text="ADMINS",width=20,command=adminsmain,font=("times new roman",14,"bold"),bg="black",fg="gold",activeforeground="gold",activebackground="black",bd=0,cursor="hand2")
    admins_btn.grid(row=3,column=0,pady=1)

        #logout btn
    def logoutfunc():
        x=messagebox.askyesno("Logout","Do you want to logout ?",parent=rootmain)
        if x>0:
            rootmain.destroy()
            log() 
        

    logout_btn=Button(btn_frame,command=logoutfunc,text="LOGOUT",width=20,font=("times new roman",14,"bold"),bg="black",fg="gold",activeforeground="gold",activebackground="black",bd=0,cursor="hand2")
    logout_btn.grid(row=4,column=0,pady=1)

    #image 4 main center image
    img4=Image.open(r"images\HOTEL_INTERFACE_BGF.jpg")
    img4=img4.resize((1310,610),Image.ANTIALIAS)
    photoimg4=ImageTk.PhotoImage(img4)

    lblimg=Label(main_frame,image=photoimg4,bd=4,relief=RIDGE)
    lblimg.place(x=230,y=0,width=1300,height=610)


        #1st down images(after menu option)
    img5=Image.open(r"images\1stdownimagefood.jpg")
    img5=img5.resize((230,210),Image.ANTIALIAS)
    photoimg5=ImageTk.PhotoImage(img5)

    lblimg=Label(main_frame,image=photoimg5,bd=4,relief=RIDGE)
    lblimg.place(x=0,y=225,width=230,height=210)
            
        #2nd down image (after menu option)
    img6=Image.open(r"images\paneerfooddownimage2nd.jpg")
    img6=img6.resize((230,190),Image.ANTIALIAS)
    photoimg6=ImageTk.PhotoImage(img6)

    lblimg=Label(main_frame,image=photoimg6,bd=4,relief=RIDGE)
    lblimg.place(x=0,y=420,width=230,height=190)

    addtables()
    rootmain.mainloop()



#--Login--#

def log():
    global root
    global fname_entry
    global l_entry
    global txt_contact
    global txt_recode
    global txt_pass
    global txt_conpass
    root=Tk()
    def Register():
        global fname_entry
        global l_entry
        global txt_contact
        global txt_recode
        global txt_pass
        global txt_conpass
        global checkbtn

        root.title("Register")
        root.geometry("1600x900+0+0")

        #background image

        bg1=ImageTk.PhotoImage(file="images\\2000x700.jpg")
            
        bg1_lbl=Label(root,image=bg1,relief=RIDGE)
        bg1_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        #bg 2
        bgimage=Image.open("images\\regbg2.jpg")
        bgimage=bgimage.resize((460,550),Image.ANTIALIAS)
        bg2=ImageTk.PhotoImage(bgimage)

        
        bg2_lbl=Label(root,image=bg2,bd=4,relief=RIDGE)
        bg2_lbl.place(x=130,y=130,width=460,height=550)

        #side frame

        frame=Frame(root,bg="white")
        frame.place(x=590,y=130,width=800,height=550)

        #frame inside work

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen")
        register_lbl.place(x=20,y=20)

        #--login button--#

        loginbtnreg=Button(frame,command=Login_Window,text="Login Now",font=("Arial",13,"bold"),bd=3,relief=RIDGE,fg="black",bg="aqua",activeforeground="black",activebackground="aqua")
        loginbtnreg.place(x=630,y=20,width=120,height=35)

        #labels and entry fields

        framename=Label(frame,text="Full Name",font=("times new roman",20,"bold"),bg="white")
        framename.place(x=50,y=100)

        #entry field for first name

        fname_entry=ttk.Entry(frame,font=("times new roman",16,"bold"))
        fname_entry.place(x=50,y=135,width=230)

        #last name

        l_name=Label(frame,text="User Name",font=("times new roman",20,"bold"),bg="white")
        l_name.place(x=370,y=100)

        l_entry=ttk.Entry(frame,font=("times new roman",16,"bold"))
        l_entry.place(x=370,y=136,width=230)

        #contact

        contact_name=Label(frame,text="Contact No",font=("times new roman",20,"bold"),bg="white")
        contact_name.place(x=50,y=170)

        txt_contact=ttk.Entry(frame,font=("times new roman",16,"bold"))
        txt_contact.place(x=50,y=210,width=230)

        #recovery  code

        recode=Label(frame,text="Recovery Code",font=("times new roman",20,"bold"),bg="white")
        recode.place(x=370,y=170)

        txt_recode=ttk.Entry(frame,font=("times new roman",16,"bold"))
        txt_recode.place(x=370,y=207,width=230)
        
        #password

        password=Label(frame,text="Password",font=("times new roman",20,"bold"),bg="white")
        password.place(x=50,y=245)

        txt_pass=ttk.Entry(frame,font=("times new roman",16,"bold"))
        txt_pass.place(x=50,y=282,width=230)

        #confirm pass

        conpass=Label(frame,text="Confirm Password",font=("times new roman",20,"bold"),bg="white")
        conpass.place(x=370,y=240)

        txt_conpass=ttk.Entry(frame,font=("times new roman",16,"bold"))
        txt_conpass.place(x=370,y=277,width=230)


        #check btn terms and conditions
        global var_check
        var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=var_check,text="I Agree the Terms & Conditions",font=("times new roman",15,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=330)
        def registerclick():
            global var_check
            global fname_entry
            global l_entry
            global txt_contact
            global txt_recode
            global txt_pass
            global txt_conpass



            if str(fname_entry.get())=="" or str(l_entry.get())=="" or str(txt_contact.get())=="" or str(txt_recode.get())=="" or str(txt_pass.get())=="" or str(txt_conpass.get())=="":
                messagebox.showerror("Error","All fields are required",parent=root)

            
                       

            elif not l_entry.get().isalpha():
                messagebox.showerror("Error","Please user Name in alphabets",parent=root)
            elif not str(txt_contact.get()).isdigit() or not str(txt_recode.get()).isdigit():
                messagebox.showerror("Error","Please Enter Digits in the desired box",parent=root)
            elif str(txt_pass.get())!=str(txt_conpass.get()):
                messagebox.showerror("Error","Password & Confirm Password must be same",parent=root)
            elif var_check.get()==0:
                messagebox.showerror("Error","Please agree our terms and conditions",parent=root)
            else:
                        
                messagebox.showinfo("Done","Welcome to our Hotel Management",parent=root)
                conn=c.connect("hotel.db")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from login where username='%s'"%(str(l_entry.get())))
                row=my_cursor.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already exist with same details\nPlease try again",parent=root)
                else:
                    my_cursor.execute("insert into login (fullname,username,contact,recode,pass,conpass)values('%s','%s','%s','%s','%s','%s')"%(str(fname_entry.get()),str(l_entry.get()),str(txt_contact.get()),str(txt_recode.get()),str(txt_pass.get()),str(txt_conpass.get())))
                    conn.commit()
                    messagebox.showinfo("Registered","Data registered successfully",parent=root)
                    conn.close()
        #register now

        img=Image.open("images\\regisnow.png")
        img=img.resize((170,50),Image.ANTIALIAS)
        photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=photoimage,borderwidth=0,command=registerclick,cursor="hand2",font=("times new roman",15,"bold"))
        b1.place(x=203,y=390,width=300)

        

        root.mainloop()

    def Login_Window():
        global root
        global fname_entry
        global l_entry
        global txt_contact
        global txt_recode
        global txt_pass
        global txt_conpass
        global txtuser
        global txtpass
        global txt_newpass
        
        root.title("Hotel Management Login Pannel")
        root.geometry("1550x800+0+0")

        bgimage=Image.open(r"images\Hotel_Login_BGF.jpg")
        bgimage=bgimage.resize((1550,800),Image.ANTIALIAS)
        bg=ImageTk.PhotoImage(bgimage)

        lbl_bg=Label(root,image=bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(root,bg="black")
        frame.place(x=603,y=175,width=340,height=450) #x and y pos value and width and height size of box

        img1=Image.open(r"images\loginicon.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=180,width=100,height=100)

            #get started label

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=107,y=100)

            #user name label

        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=60,y=155)
            
        txtuser=ttk.Entry(frame,font=("times new roman",13,"bold"))       
        txtuser.place(x=35,y=180,width=270)

            #password label

        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=60,y=225)

        txtpass=ttk.Entry(frame,font=("times new roman",13,"bold"),show="*")       
        txtpass.place(x=35,y=250,width=270)

            #Icon Images of username 

        img2=Image.open(r"images\loginusericon.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=640,y=330,width=25,height=25)

            #Icon Images of password

        img3=Image.open(r"images\loginpassicon.png")
        img3=img3.resize((55,25),Image.ANTIALIAS)
        photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=photoimage3,bg="black",borderwidth=0)
        lblimg1.place(x=639,y=400,width=25,height=25)
            
            #login btn in login pannel               here command ka kaam click karne par def login ko call karna hai
        def login():
            global txtuser
            global txtpass
            global txt_recode

            if str(txtuser.get())=="" or str(txtpass.get())=="":
                messagebox.showerror("Error","All fields required",parent=root)
            else:
                conn=c.connect("hotel.db")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from login where username='%s' and pass='%s'"%(str(txtuser.get()),str(txtpass.get())))
                row=my_cursor.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Username & Password",parent=root)
                else:
                    root.destroy()
                    Devilmain()


        loginbtn=Button(frame,command=login,text="Login",font=("times new roman",13,"bold"),bd=3,relief=RIDGE,fg="black",bg="aqua",activeforeground="black",activebackground="aqua")
        loginbtn.place(x=105,y=300,width=120,height=35)

            # registerbutton for new users

        registerbtn=Button(frame,text="New User Register",command=Register,font=("times new roman",11,"bold"),bd=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=5,y=353,width=160)

            #forgot passbtn
        def forgotpass():
            global txtuser
            global txtpass
            global txt_recode
            global txt_newpass

            if str(txtuser.get())=="":
                messagebox.showerror("Error","Please Enter User Name to reset Password",parent=root)
            else:
                conn=c.connect("hotel.db")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from login where username='%s'"%(str(txtuser.get())))
                row=my_cursor.fetchone()

                if row==None:
                    messagebox.showerror("Error","Please enter valid username",parent=root)
                else:
                    conn.close()
                    root2=Toplevel()
                    root2.title("Forgot Password")
                    root2.geometry("360x480+590+170")

                    l=Label(root2,text="Forgot Password",font=("times new roman",20,"bold"),fg="blue",bg="cyan")
                    l.place(x=0,y=10,relwidth=1)

                    #recovery  code

                    recode=Label(root2,text="Recovery Code",font=("times new roman",20,"bold"),bg="cyan")
                    recode.place(x=88,y=80)

                    txt_recode=ttk.Entry(root2,font=("times new roman",16,"bold"))
                    txt_recode.place(x=50,y=130,width=250)
                    
                    #password

                    newpassword=Label(root2,text="New Password",font=("times new roman",20,"bold"),bg="cyan")
                    newpassword.place(x=88,y=180)

                    txt_newpass=ttk.Entry(root2,font=("times new roman",16,"bold"))
                    txt_newpass.place(x=50,y=220,width=250)
                    
                    def resetpass():
                        global txtuser
                        global txt_newpass
                        global txt_recode

                        

                        if str(txt_recode.get())=="":
                            messagebox.showerror("Error","Please enter Recovery Code",parent=root2)
                        elif not str(txt_recode.get()).isdigit():
                            messagebox.showerror("Error","Please enter Recovery Code in Digits",parent=root2)
                        else:
                            conn=c.connect("hotel.db")
                            my_cursor=conn.cursor()
                            my_cursor.execute("select * from login where username='%s' and recode='%s'"%(str(txtuser.get()),str(txt_recode.get())))
                            row=my_cursor.fetchone()
                            if row==None:
                                messagebox.showerror("Error","Please enter Correct Recovery Code",parent=root2)
                            else:
                                my_cursor.execute("update login set pass='%s' where username='%s' and recode='%s'"%(str(txt_newpass.get()),str(txtuser.get()),str(txt_recode.get())))
                                conn.commit()
                                conn.close()
                                messagebox.showinfo("Info","Your password has been reset\nYou can login with your new password",parent=root2) 
                                root2.destroy()


                        



                    #btn for reset

                    btn=Button(root2,text="Reset Password",command=resetpass,font=("times new roman",15,"bold"),fg="white",bg="blue")
                    btn.place(x=100,y=290)

        forgotpassbtn=Button(frame,text="Forgot Password",command=forgotpass,font=("times new roman",11,"bold"),bd=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgotpassbtn.place(x=7,y=382,width=140)

        #click login func

        

        root.mainloop()
    Login_Window()



log()







