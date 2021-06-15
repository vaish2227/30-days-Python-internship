from tkinter import *
import tkinter.messagebox
root=Tk()
root.title("Employee Registration Form")
root.geometry('500x500')
root.configure(background="grey94")

label1=Label(root,text="Employee registration form",font=("bold",20)).grid(row=0,column=2)

Firstname=Label(root,text="First Name",bg="red",fg="white",width=20,font=("bold",10)).grid(row=1,column=1)
Lastname=Label(root,text="Last Name",width=20,font=("bold",10)).grid(row=2,column=1)
Address=Label(root,text="Address",bg="red",fg="white",width=20,font=("bold",10)).grid(row=3,column=1)
City=Label(root,text="City",width=20,font=("bold",10)).grid(row=4,column=1)
State=Label(root,text="State",bg="red",fg="white",width=20,font=("bold",10)).grid(row=5,column=1)
Contry=Label(root,text="Country",width=20,font=("bold",10)).grid(row=6,column=1)
list1=['Canada','India','South Africa','America','Japan']
c=StringVar()
droplist=OptionMenu(root,c,*list1)
droplist.config(width=15)
c.set('select your country')
droplist.grid(row=7,column=2)
Mobile=Label(root,text="Contact no.",bg="red",fg="white",width=20,font=("bold",10)).grid(row=8,column=1)
Email=Label(root,text="Email",width=20,font=("bold",10)).grid(row=9,column=1)
Gender=Label(root,text="Gender",bg="red",fg="white",width=20,font=("bold",10)).grid(row=10,column=1)
var=IntVar()
Radiobutton(root,text="Male",padx=30,variable=var,value=1).grid(row=10,column=2)
Radiobutton(root,text="Female",padx=20,variable=var,value=2).grid(row=10,column=3)

F1=Entry(root).grid(row=1,column=2)
L1=Entry(root).grid(row=2,column=2)
Ad1=Entry(root).grid(row=3,column=2)
c1=Entry(root).grid(row=4,column=2)
s1=Entry(root).grid(row=5,column=2)
m1=Entry(root).grid(row=8,column=2)
e1=Entry(root).grid(row=9,column=2)

def onClick():
    tkinter.messagebox.showinfo("Welcome","Your Details Submitted Successfully!")

Button(root,text="Submit",command=onClick,width=20,bg="red",fg="white").grid(row=14,column=2)
root.mainloop()
