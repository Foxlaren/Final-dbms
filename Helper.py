import tkinter
from tkinter import ttk,messagebox
from tkinter import *
# import mysql.connector

#creating main window

window=tkinter.Tk()
window.title("Helper Registering")
window.geometry('600x500')

#connecting database

# def insert(hid,hname,hph,hos_name):
#     if(hid==''or hname=='' or hph==''or hos_name==''):
#         messagebox.showinfo("Insert status","Error-all fields required")
#     else:
#         connection = mysql.connector.connect(host = 'localhost',database = 'mhms',user='root',password='sam13102001')
#         mySql_insert_query = "INSERT INTO helper VALUES(%s,%s,%s,%s)"
#         record=(hid,hname,hph,hos_name)
#         cursor = connection.cursor()
#         cursor.execute(mySql_insert_query,record)
#         messagebox.showinfo("Insert status","Successfully Inserted")
#         connection.commit()


#creating Heading

label=tkinter.Label(
    window,
    text="Helper Record Register",
    font=("consolas", 14, 'bold'),
    bg="black",
    fg="white"
)
label.pack()

#declaring string variables

name_var1=tkinter.StringVar()
name_var2=tkinter.StringVar()
name_var3=tkinter.StringVar()
name_var4=tkinter.StringVar()

options = ["Government Mental Helath Hospital, Belagaum",
            "Government Mental Helath Hospital, Bengaluru",
            "Government Mental Helath Hospital, Hubli",
            "Government Mental Helath Hospital, Mandya",
            "Government Mental Helath Hospital, Mysuru"]

#creating labels and entry widget

l1=tkinter.Label(window,text="Helper ID =").place(x=10,y=40)

e1=tkinter.Entry(window,textvariable=name_var1,font=('calibre',10,'normal')).place(x=120,y=40)

l2=tkinter.Label(window,text="Helper Name =").place(x=10,y=70)

e2=tkinter.Entry(window,textvariable=name_var2,font=('calibre',10,'normal')).place(x=120,y=70)

l3=tkinter.Label(window,text="Helper Phone =").place(x=10,y=100)

e3=tkinter.Entry(window,textvariable=name_var3,font=('calibre',10,'normal')).place(x=120,y=100)

l4=tkinter.Label(window,text="Hospital_Name =").place(x=10,y=130)

e4=ttk.Combobox(window,textvariable=name_var4, values= options, width=50).place(x=120,y=130)

def insert_q():
    print(name_var1.get())
    insert(name_var1.get(),name_var2.get()
           ,name_var3.get()
           ,name_var4.get())

button=Button(
    window,
    text="Enter",
    font=("Lucida sans", 10),
    fg="#00ff00",
    bg="black",
    activeforeground="#00ff00",
    activebackground="black",
    command=insert_q)
button.place(x=150,y=220)

window.config(bg="#efd9c1")
window.mainloop()
