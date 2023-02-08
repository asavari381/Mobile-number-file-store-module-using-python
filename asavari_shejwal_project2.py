from tkinter import *
from tkinter import messagebox
from tkinter import Text
import tkinter as tk

root = Tk()
root.title('Product Deal')
root.geometry('1400x900+0+0')

input_userid = StringVar()
input_username = StringVar()
input_price = StringVar()
input_quantity = StringVar()

def insert():
    Id = input_userid.get()
    name = input_username.get()
    price = input_price.get()
    quantity = input_quantity.get()
    
    inventory = open('inventory_management.txt', 'a')
    inventory_data = open('inventory_management.txt', 'r')
    file = inventory_data.read()

    
    if Id=="" or name=="" or price=="" or quantity=="":
        messagebox.showmessage("Please Enter Information")
    elif price.isdigit()==False or quantity.isdigit()==False:
        messagebox.showmessage("Please Enter Valid selling price and quantity")
        txt1_price.delete(0,'end')
        txt1_quantity.delete(0,'end')
    elif Id in file:
        messagebox.showmessage( "Product id already exists.")
    else :
        inventory_data = open("inventory_management.txt","r")
        count = file.splitlines()
        if len(count) == 0:
                item_no = 1
        else:
            lastline = count[-1]
            item_no = int(lastline[0]) + 1

        entry = "\n\n"+str(item_no)+"\t\t\t" + Id +"\t\t\t"+ name +"\t\t\t"+ price +"\t\t\t"+ quantity +"\n"
        inventory.write(entry)
        messagebox.showinfo("Success","Data has been inserted successfully!")
        txt1_userid.delete(0,'end')
        txt1_username.delete(0,'end')
        txt1_price.delete(0,'end')
        txt1_quantity.delete(0,'end')

def show():
    tf_show.delete("1.0","end")
    inventory = open("inventory_management.txt","r")
    for data in inventory.readlines():
        tf_show.insert(tk.END,data)
    inventory.close()


F1=LabelFrame(root, text='Inventory management',font=('times new roman',16, 'bold'),relief=GROOVE)
F1.place(x=0,y=80,width=500,height=800)

labl1_userid= Label(F1, text='Product id:',font=('helvetica',24,''))
labl1_userid.grid(row=0,column=0,padx=15, pady=15,sticky='w')

txt1_userid= Entry(F1,width=16,font='arial 15',textvar=input_userid)
txt1_userid.grid(row=10,column=0, padx=15, pady=15)

labl1_username= Label(F1, text='Product Name:',font=('helvetica',20,''))
labl1_username.grid(row=15,column=0,padx=20, pady=20,sticky='w')

txt1_username= Entry(F1,width=21,font='arial 15',textvar=input_username)
txt1_username.grid(row=18,column=0, padx=10, pady=10)

labl1_price= Label(F1, text='Selling price:',font=('helvetica',21,''))
labl1_price.grid(row=12,column=0,padx=5, pady=5,sticky='w')

txt1_price= Entry(F1,width=28,font='arial 15',textvar=input_price)
txt1_price.grid(row=45,column=0, padx=6, pady=6)

labl1_quantity= Label(F1, text='Quantity:',font=('helvetica',22,''))
labl1_quantity.grid(row=25,column=0,padx=6, pady=6, sticky='w')

txt1_quantity= Entry(F1,width=20,font='arial 15',textvar=input_quantity)
txt1_quantity.grid(row=30,column=0, padx=10, pady=10)

butnFrame=Frame(F1)
butnFrame.place(x=20,y=800,width=160,height=30)

butn_insert = Button(butnFrame, text='Insert' ,width=10, font=('helvetica',24,'bold'), bg='red',command=insert)
butn_insert.grid(row=0, column=0,padx=0, pady=0,sticky='w')

butn_show = Button (butnFrame, text='Show',width=6, font=('helvetica',29,'bold'), bg='red',command=show)
butn_show.grid(row=0, column=1,padx=0, pady=0)

F2=LabelFrame(root, text='Product list',font=('helvetica',16, 'bold'),relief=GROOVE)
F2.place(x=140,y=50,width=1900, height=300)

tf_show= Text(F2,width=200,height=150,font='helvetica')
tf_show.grid(row=10,column=0,pady=5,padx=8,sticky='w')

F3 = Frame(F2)
F3.place(x=10,y=15,width=500,height=60)

labl1_showno= Label(F3, text='Item no:',bd=8,relief='raised',font=('arial',19,'bold'),width=20)
labl1_showno.grid(row=0,column=0,padx=0, pady=10,sticky='w')

labl1_showid= Label(F3, text='Product id:',bd=8,relief='raised' ,font=('arial',19,'bold'),width=20)
labl1_showid.grid(row=0,column=10,padx=0, pady=10,sticky='w')

labl1_showname= Label(F3, text='Name:',bd=8,relief='raised' ,font=('arial',19,'bold'),width=20)
labl1_showname.grid(row=0,column=20,padx=0, pady=10,sticky='w')

labl1_showprice= Label(F3, text='Selling price:',bd=8,relief='raised' ,font=('arial',19,'bold'),width=20)
labl1_showprice.grid(row=0,column=24,padx=0, pady=10,sticky='w')

labl1_showquantity= Label(F3, text='Quantity:',bd=2,relief='raised' ,font=('arial',19,'bold'),width=20)
labl1_showquantity.grid(row=0,column=21,padx=0, pady=10,sticky='w')

root.mainloop()
