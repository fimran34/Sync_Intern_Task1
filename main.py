#Importing all the necessary libraries to form the alarm clock:
from tkinter import *
import datetime
import time
import playsound

def al(set_timer):
    while True:
        time.sleep(1)
        currentime = datetime.datetime.now()
        now = currentime.strftime("%H:%M:%S")
        date = currentime.strftime("%d/%m/%Y")
        print("The date today is:",date)
        print(now)
        if now == set_timer:
            print("Time to Wake up")
            playsound.playsound('alarm.mp3')
            break

def actual_time():
    set_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    al(set_timer)

alarm = Tk()
alarm.title("Task 1: Alarm Clock")
alarm.configure(bg='#F3FDE8')
alarm.geometry("400x300")
time_form=Label(alarm, text= "Enter time in 24 hour format!", fg="#016A70",bg="#F3FDE8",font="Arial").place(x=100,y=120)
addtime = Label(alarm,text = "Hour  Min   Sec",font=200,bg="#F3FDE8",fg="#016A70").place(x = 130)

# The Variables we require to set the alarm(initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()

#Time required to set the alarm clock:
hourTime= Entry(alarm,textvariable = hour,bg = "#FFE5E5",width = 2).place(x=130,y=30)
minTime= Entry(alarm,textvariable = min,bg = "#FFE5E5",width = 2).place(x=165,y=30)
secTime = Entry(alarm,textvariable = sec,bg = "#FFE5E5",width = 2).place(x=200,y=30)

#To take the time input by user:
submit = Button(alarm,text = "Set Alarm",fg="#016A70",width = 8,padx=0,pady=0,command = actual_time).place(x =125,y=75)

alarm.mainloop()
#Execution of the window.