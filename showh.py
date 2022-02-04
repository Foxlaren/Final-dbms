import tkinter as tk
from tkinter import ttk, messagebox
#import mysql.connector
from tkinter import *

# def show():
#     hid = e1.get()
#
#     mysqldb = mysql.connector.connect(host='localhost', database='mhms', user='root', password='sam13102001')
#     mycursor = mysqldb.cursor()
#
#     sql = f"SELECT * FROM HELPER WHERE Helper_id='{hid}'"
#     mycursor.execute(sql)
#     records = mycursor.fetchall()
#     print(records)
#
#     for i, (Helper_id, Helper_Name, Helper_Phone, Hospital_Name) in enumerate(records, start=1):
#         listBox.insert("", "end", values=(Helper_id, Helper_Name, Helper_Phone, Hospital_Name))
#         mysqldb.close()

root = Tk()
root.geometry("750x500")
global e1


tk.Label(root,
         text="HELPER",
         font=("consolas", 14, 'bold'),
         bg="black",
         fg="white"
         ).place(x=330,y=10)

tk.Label(root, text="DOCTOR ID").place(x=10, y=60)

e1 = Entry(root)
e1.place(x=140, y=60)

cols=('Helper_id', 'Helper_Name', 'Helper_Phone', 'Hospital_Name')
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
    activebackground="black"
    ).place(x=180, y=100)


for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=10, y=200)
    listBox.column("#1", anchor=CENTER, width= 100)
    listBox.column("#2", anchor=CENTER, width= 100)
    listBox.column("#3", anchor=CENTER, width= 120)
    listBox.column("#4", anchor=CENTER, width= 400)


# show()

root.config(bg="#efd9c1")
root.mainloop()