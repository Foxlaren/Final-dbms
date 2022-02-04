import tkinter as tk
from tkinter import ttk, messagebox
#import mysql.connector
from tkinter import *

def show():
    pid = e1.get()

    mysqldb = mysql.connector.connect(host='localhost', database='mhms', user='root', password='sam13102001')
    mycursor = mysqldb.cursor()

    sql = f"SELECT * FROM PATIENT WHERE Patient_id='{pid}'"
    # val = (pid)
    mycursor.execute(sql)
    records = mycursor.fetchall()
    print(records)

    for i, (Patient_id,Patient_name, Patient_Phone, Doc_id,Helper_id,Disorder_Name, Hospital_Name,Prescription,Suicidal,Sectionied,Time_to_Cure) in enumerate(records, start=1):
        listBox.insert("", "end", values=(Patient_id,Patient_name, Patient_Phone, Doc_id,Helper_id,Disorder_Name, Hospital_Name,Prescription,Suicidal,Sectionied,Time_to_Cure))
        mysqldb.close()

root = Tk()
root.geometry("1240x500")
global e1


tk.Label(
    root,
    text="PATIENT",
    font=("consolas", 14, 'bold'),
    bg="black",
    fg="white"
    ).place(x=550,y=10)

tk.Label(root, text="PATIENT ID").place(x=10, y=60)

e1 = Entry(root)
e1.place(x=140, y=60)

cols=('Patient_id','Patient_name', 'Patient_Phone', 'Doc_id','Helper_id','Disorder_Name', 'Hospital_Name','Prescription','Suicidal','Sectionied','Time_to_Cure')
listBox = ttk.Treeview(root, columns=cols, show='headings')

# Button(root, text="Enter", command=show, height=1, width=5).place(x=180, y=80)
Button(
    root,
    text="Enter",
    height=1,
    width=5,
    font=("Lucida sans", 10),
    fg="#00ff00",
    bg="black",
    activeforeground="#00ff00",
    activebackground="black",
    ).place(x=180, y=100)


#Styling treee view

style = ttk.Style()
style.configure("Treeview",
                background="silver",
                foreground="black",
                fieldbackground="silver")
#Change selected color
style.map("Treeview",
          background=[('selected',"#00ff00")])

listBox = ttk.Treeview(root,
                       columns=cols,
                       show='headings',style="Treeview")

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=10, y=200)
    listBox.column("#1", anchor=CENTER, width= 100)
    listBox.column("#2", anchor=CENTER, width= 100)
    listBox.column("#3", anchor=CENTER, width= 120)
    listBox.column("#4", anchor=CENTER, width= 100)
    listBox.column("#5", anchor=CENTER, width= 100)
    listBox.column("#6", anchor=CENTER, width= 100)
    listBox.column("#7", anchor=CENTER, width= 300)
    listBox.column("#8", anchor=CENTER, width= 100)
    listBox.column("#9", anchor=CENTER, width= 50)
    listBox.column("#10", anchor=CENTER, width= 65)
    listBox.column("#11", anchor=CENTER, width= 80)



# show()

root.title("View Patient")
root.config(bg="#efd9c1")
root.mainloop()

