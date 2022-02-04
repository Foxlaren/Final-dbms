import tkinter
from tkinter import ttk,messagebox
from tkinter import *
# import mysql.connector

#creating main window

window=tkinter.Tk()
window.title("Patient Registering")
window.geometry('600x500')

#add command

# def insert(p_id,p_name,p_ph, doc_id, help_id, dis_name,hos_name,pres,sui,sec,time):
#     if(p_id=='' or p_name==''or p_ph==''or doc_id==''or help_id==''  or dis_name==''or hos_name=='' or pres=="" or sui=='' or sec=='' or time==''):
#         messagebox.showinfo("Insert status","Error-all fields required")
#     else:
#         connection = mysql.connector.connect(host = 'localhost',database = 'mhms',user='root',password='sam13102001')
#         mySql_insert_query = "INSERT INTO patient VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
#         cursor = connection.cursor()
#         record = (p_id,p_name,p_ph, doc_id, help_id, dis_name,hos_name,pres,sui,sec,time)
#         cursor.execute(mySql_insert_query,record)
#         messagebox.showinfo("Insert status","Successfully Inserted")
#         connection.commit()


#delete command

def delete(pid):
    mysqldb = mysql.connector.connect(host='localhost', database='mhms', user='root', password='sam13102001')
    mycursor = mysqldb.cursor()

    try:
        sql = f"DELETE FROM patient WHERE Patient_id='{pid}'"
        val = (pid)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Record Deleteeeee successfully...")

    except Exception as e:

        print(e)
        mysqldb.rollback()
        mysqldb.close()

#creating Heading

label=tkinter.Label(
    window,
    text="Patient Record Register",
    font =("consolas",14,'bold'),
    bg="black",
    fg="white"
    )
label.pack()


#declaring string variables

name_var1=tkinter.StringVar()
name_var2=tkinter.StringVar()
name_var3=tkinter.StringVar()
name_var4=tkinter.StringVar()
name_var5=tkinter.StringVar()
name_var6=tkinter.StringVar()
name_var7=tkinter.StringVar()
name_var8=tkinter.StringVar()
name_var9=tkinter.StringVar()
name_var10=tkinter.StringVar()
name_var11=tkinter.StringVar()

options1 = ["Government Mental Helath Hospital, Belagaum",
            "Government Mental Helath Hospital, Bengaluru",
            "Government Mental Helath Hospital, Hubli",
            "Government Mental Helath Hospital, Mandya",
            "Government Mental Helath Hospital, Mysuru"]

disorder = ["Addiction & Substance Abuse","Anxiety",
            "ADHD","Insomnia",
            "Bipolar Disorder","Schizophrenia",
            "PTSD","Eating Disorders",
            "Depression","Borderline Personality"]

options2 = ["Yes","No"]


#creating labels and entry widget

l1 = tkinter.Label(window,text="Patient ID ").place(x=10,y=40)
l2 = tkinter.Label(window,text="Patient Name ").place(x=10,y=70)
l3 = tkinter.Label(window,text="Patient PH ").place(x=10,y=100)
l4 = tkinter.Label(window,text="Doctor ID ").place(x=10,y=130)
l5 = tkinter.Label(window,text="Helper ID ").place(x=10,y=160)
l6 = tkinter.Label(window,text="Disorder Name ").place(x=10,y=190)
l7 = tkinter.Label(window,text="Hospital Name ").place(x=10,y=220)
l8 = tkinter.Label(window,text="Prescription ").place(x=10,y=250)
l9 = tkinter.Label(window,text="Suicidal ").place(x=10,y=310)
l10= tkinter.Label(window,text="Sectioned ").place(x=10,y=340)
l11= tkinter.Label(window,text="Time to Cure ").place(x=10,y=370)


#Radio button
buttons = ["Yes","No"]

Patient_ID = tkinter.Entry(window,textvariable=name_var1,font=('calibre',10,'normal')).place(x=120,y=40)

Name = tkinter.Entry(window,textvariable=name_var2,font=('calibre',10,'normal')).place(x=120,y=70)

PH = tkinter.Entry(window,textvariable=name_var3,font=('calibre',10,'normal')).place(x=120,y=100)

Doc_ID = tkinter.Entry(window,textvariable=name_var4,font=('calibre',10,'normal')).place(x=120,y=130)

Helper_ID = tkinter.Entry(window,textvariable=name_var5,font=('calibre',10,'normal')).place(x=120,y=160)

Dis_Name = ttk.Combobox(window,textvariable=name_var6, values= disorder, width=50).place(x=120,y=190)

Hos_Name = ttk.Combobox(window,textvariable=name_var7, values= options1, width=50).place(x=120,y=220)

Prescription = tkinter.Entry(window,textvariable=name_var8,font=('calibre',10,'normal'),width=45).place(x=120,y=250)

Suicidal = ttk.Combobox(window,textvariable=name_var9,value=options2,font=('calibre',10,'normal')).place(x=120,y=310)

Sectioned = ttk.Combobox(window,textvariable=name_var10,value=options2,font=('calibre',10,'normal')).place(x=120,y=340)

Time = tkinter.Entry(window,textvariable=name_var11,font=('calibre',10,'normal')).place(x=120,y=370)



def insert_q():
    insert(name_var1.get()
           ,name_var2.get()
           ,name_var3.get()
           ,name_var4.get()
           ,name_var5.get()
           ,name_var6.get()
           ,name_var7.get()
           ,name_var8.get()
           ,name_var9.get()
           ,name_var10.get()
           ,name_var11.get())


def delete_q():
    delete(name_var1.get())

button=Button(
    window,
    text="Add",
    font=("Lucida sans", 10),
    fg="#00ff00",
    bg="black",
    activeforeground="#00ff00",
    activebackground="black",
    command=insert_q)
button.place(x=150,y=420)

button=Button(
    window,
    text="Delete",
    font=("Lucida sans", 10),
    fg="#00ff00",
    bg="black",
    activeforeground="#00ff00",
    activebackground="black",
    command=delete_q
)
button.place(x=200,y=420)


window.config(bg="#efd9c1")
window.mainloop()

