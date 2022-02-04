import tkinter as tk
from tkinter import ttk, messagebox
#import mysql.connector
from tkinter import *

# def show():
#     did = e1.get()
#
#     mysqldb = mysql.connector.connect(host='localhost', database='mhms', user='root', password='sam13102001')
#     mycursor = mysqldb.cursor()
#
#     sql = f"SELECT * FROM DOCTOR WHERE Doctor_Name='{did}'"
#     mycursor.execute(sql)
#     records = mycursor.fetchall()
#     print(records)
#
#     for i, (Doctor_id, Doctor_Name, Doc_Qualification, Doc_Phone, Doc_email, Hospital_Name) in enumerate(records, start=1):
#         listBox.insert("", "end", values=(Doctor_id, Doctor_Name, Doc_Qualification, Doc_Phone, Doc_email, Hospital_Name))
#         mysqldb.close()

root = Tk()
root.geometry("950x500")
global e1


tk.Label(
    root,
    text="DOCTOR",
    font=("consolas", 14, 'bold'),
    bg="black",
    fg="white"
    ).place(x=400,y=10)

tk.Label(root, text="DOCTOR Name").place(x=10, y=80)

e1 = Entry(root)
e1.place(x=140, y=80)

cols=('Doctor_id', 'Doctor_Name', 'Doc_Qualification', 'Doc_Phone', 'Doc_email', 'Hospital_Name')

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

Button(root,
       text="Enter",
       height=1,
       width=5,
       font=("Lucida sans", 10),
       fg="#00ff00",
       bg="black",
       activeforeground="#00ff00",
       activebackground="black",
       ).place(x=180, y=120)
#Button(root, text="Enter", command=show, height=1, width=5).place(x=180, y=80)

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=10, y=200)
    listBox.column("#1", anchor=CENTER, width= 100)
    listBox.column("#2", anchor=CENTER, width= 100)
    listBox.column("#3", anchor=CENTER, width= 120)
    listBox.column("#4", anchor=CENTER, width= 100)
    listBox.column("#5", anchor=CENTER, width= 100)
    listBox.column("#6", anchor=CENTER, width= 400)


# show()

root.title("View Patient")
root.config(bg="#efd9c1")
root.mainloop()