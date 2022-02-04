from tkinter import *
from tkinter import messagebox
from tkinter import *
#import mysql.connector
import os

#New Patient window
def patOption():
    def upPat():
        filename = "patient.py"
        os.system(filename)

    def viewPat():
        filename="showp.py"
        os.system(filename)


    patOption = Tk()
    patOption.geometry("600x500")
    patOption.title("Patient")
    patOption.config(background="#efd9c1")

    #icon = PhotoImage(file="Patient_Care_Cartoon.svg.png")
    label= Label(patOption,bg="#dc7c71",width=20,height=6,text="Patient Information",font=("consolas",30)).pack()

    upPat = Button(
        patOption,
        text="Update Patient Information",
        command=upPat,
        font=("Lucida sans", 10),
        fg="#00ff00",
        bg="black",
        activeforeground="#00ff00",
        activebackground="black"
    )
    upPat.place(x=50,y=350)

    viewPat = Button(
        patOption,
        text="View Patient Information",
        command=viewPat,
        font=("Lucida sans", 10),
        fg="#00ff00",
        bg="black",
        activeforeground="#00ff00",
        activebackground="black"
    )
    viewPat.place(x=380, y=350)

    window.destroy()

    patOption.mainloop()

#New Doctor window
def docOption():

    def addDoc():
        os.system("Doctor.py")

    def viewDoc():
        os.system("showd.py")

    docOption = Tk()
    docOption.geometry("600x500")
    docOption.title("Doctor")
    docOption.config(background="#efd9c1")

    label2 = Label(docOption, bg="#dc7c71", width=20, height=6, text="Doctor Information", font=("consolas", 30)).pack()

    addDoc = Button(
        docOption,
        text="Add Doctor Information",
        font=("Lucida sans", 10),
        fg="#00ff00",
        bg="black",
        activeforeground="#00ff00",
        activebackground="black",
        command=addDoc
    )
    addDoc.place(x=50, y=350)

    viewDoc = Button(
        docOption,
        text="View Doctor Information",
        font=("Lucida sans", 10),
        fg="#00ff00",
        bg="black",
        activeforeground="#00ff00",
        activebackground="black",
        command=viewDoc
    )
    viewDoc.place(x=380, y=350)

    window.destroy()
    docOption.mainloop()

#New Helper Window
def helpOption():

    def addHelp():
        os.system("Helper.py")

    def viewHelp():
        os.system("showh.py")

    helpOption = Tk()
    helpOption.geometry("600x500")
    helpOption.title("Query Helper")
    helpOption.config(background="#efd9c1")

    label2 = Label(helpOption, bg="#dc7c71", width=20, height=6, text="Helper Information", font=("consolas", 30)).pack()

    addHelp = Button(
        helpOption,
        text="Add Helper Information",
        font=("Lucida sans", 10),
        fg="#00ff00",
        bg="black",
        activeforeground="#00ff00",
        activebackground="black",
        command=addHelp
    )
    addHelp.place(x=50, y=350)

    viewHelp = Button(
        helpOption,
        text="View Helper Information",
        font=("Lucida sans", 10),
        fg="#00ff00",
        bg="black",
        activeforeground="#00ff00",
        activebackground="black",
        command=viewHelp
    )
    viewHelp.place(x=380, y=350)

    window.destroy()
    helpOption.mainloop()


#creating main window
window=Tk()
window.title("Query Window")
window.geometry('600x500')

#creating Heading
icon = PhotoImage(file="final image.png")
label=Label(
    window,
    text="MENTAL HEALTH HOSPITAL MANAGEMENT",
    font =("consolas",14,'bold'),
    bg="black",
    fg="white",
    image=icon,
    compound="bottom",
    width=440,
    height=320
)
label.place(x=70,y=35)

queryPatient = Button(
    window,
    text="Patient Info",
    command=patOption,
    font=("Lucida sans", 10),
    fg="#00ff00",
    bg="black",
    activeforeground="#00ff00",
    activebackground="black"
)
queryPatient.place(x=60,y=400)

queryDoctor = Button(
    window,
    text="Doctor Info",
    command=docOption,
    font=("Lucida sans", 10),
    fg="#00ff00",
    bg="black",
    activeforeground="#00ff00",
    activebackground="black"
)
queryDoctor.place(x=265,y=400)

queryHelper = Button(
    window,
    text="Helper Info",
    command=helpOption,
    font=("Lucida sans",10),
    fg="#00ff00",
    bg="black",
    activeforeground="#00ff00",
    activebackground="black"
)
queryHelper.place(x=460,y=400)

window.config(bg="#efd9c1")
window.mainloop()