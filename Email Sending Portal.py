from tkinter import *
import tkinter as tk
import  smtplib


# Screen

master = Tk()
master.title(" Email App ")

#Functons
def Send():
   try:
      username=temp_username.get()
      password = temp_password.get()
      to =temp_receiver.get()
      subject=temp_subject.get()
      body=temp_body.get()
      if username=="" or password=="" or to=="" or subject=="" or body=="":
         notif.config(text="All Fields Are Required !",fg="red")
         return

      else:
         finalMessage='Subject:{}\n\n{}'.format(subject,body)
         server=smtplib.SMTP('smtp.gmail.com',587)
         server.starttls()
         server.login(username,password)
         server.sendmail(username,to,finalMessage)
         notif.config(text='Email Has Been Sent',fg='green')

   except:
      notif.config(text="Error Sending Email", fg="red")

def Reset():
   print("Reset")
   usernameEntry.delete(0,'end')
   passwordEntry.delete(0, 'end')
   receiverEntry.delete(0, 'end')
   subjectEntry.delete(0, 'end')
   subjectBody.delete(0, 'end')

#Graphics
Label(master , text=" Email App", font=('Calibri',15)).grid(row=0, sticky=N)
Label(master, text="Use the below to send an email",font=('Calibri',12)).grid(row=1, sticky=W, padx=5)
Label(master, text="Enter Email:-",font=('Calibri',12)).grid(row=2, sticky=W, padx=5)
Label(master, text="Enter Password:-",font=('Calibri',12)).grid(row=3, sticky=W, padx=5)
Label(master, text="Sent To:-",font=('Calibri',12)).grid(row=4, sticky=W, padx=5)
Label(master, text="Enter Subject:-",font=('Calibri',12,)).grid(row=5, sticky=W)
Label(master, text="Enter Body:-",font=('Calibri',12)).grid(row=6, sticky=W, padx=5)
notif=Label(master, text=" ",font=('Calibri',12))
notif.grid(row=7, sticky=S, padx=5)

#Storage
temp_username=StringVar()
temp_password=StringVar()
temp_receiver=StringVar()
temp_subject=StringVar()
temp_body=StringVar()

#Entries
usernameEntry= Entry(master,textvariable=temp_username)
usernameEntry.grid(row=2,column=0, padx= 110, pady= 12)

passwordEntry= Entry(master,show='*',textvariable=temp_password)
passwordEntry.grid(row=3,column=0,pady= 12)

receiverEntry= Entry(master,textvariable=temp_receiver)
receiverEntry.grid(row=4,column=0,pady= 12)

subjectEntry= Entry(master,textvariable=temp_subject)
subjectEntry.grid(row=5,column=0,pady= 12)

subjectBody= Entry(master,textvariable=temp_body,width=25)
subjectBody.grid(row=6,column=0,pady= 12)

#Buttons
Button(master, text="Send",command= Send).grid(row=7,sticky=W,pady=15,padx=5)
Button(master, text="Reset",command= Reset).grid(row=7,sticky=W,pady=45,padx=45)

tk.mainloop()
master.mainloop()