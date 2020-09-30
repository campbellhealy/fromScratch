# alarm_clock.py using Windows10

'''
This time I was struggling to figure this out. I have not used tkinter before.
Then from tkinter import * has been replaced with the actual methods,
this will make sure the coder know what is actually in the code.

Colour is changing, as work thorugh thism as is the size and layout of the items.
The basic sound.wav is replaced with one of the Alarm wav files, there are four that
I am aware, easy to guess the file names. The actual file location is in the code now.
'''

from tkinter import Tk, Label, StringVar, Entry, Button
import datetime
import time
from winsound import PlaySound, SND_ASYNC



def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        print(now)
        if now == set_alarm_timer:
            print("Time to Wake up")
            x = 0
            for x in range(5):
                x+=1
                PlaySound("C:\Windows\Media\Alarm01.wav",SND_ASYNC)
                time.sleep(5) # The above file plays for 5 seconds
                print(x)
            break

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)



clock = Tk()
clock.configure(bg='black')
clock.title("Alarm Clock")
clock.geometry("320x200")
label = Label(text="When to wake you up",fg="white",bg="black").place(x = 85, y=20)
addTime = Label(clock,text = "Hour  Min   Sec",fg="white",bg="black",font=60).place(x = 90)
time_format=Label(clock, text= "24 hour Time Format!", fg="white",bg="black",font="Arial").place(x= 80,y=120)


hour = StringVar()
min = StringVar()
sec = StringVar()

#Time required to set the alarm clock:
hourTime= Entry(clock,textvariable = hour,bg = "yellow").place(x=80,y=45)
minTime= Entry(clock,textvariable = min,bg = "yellow").place(x=100,y=45)
secTime = Entry(clock,textvariable = sec,bg = "red").place(x=120,y=45)

submit = Button(clock,text = "Set Alarm",fg="white",bg = "green",width = 10,command = actual_time).place(x =110,y=85)

clock.mainloop()

