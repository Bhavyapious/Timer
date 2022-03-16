import time
from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry("500x450")
root.title("Timer")
root.config(bg='#345')
root.resizable(False,False)

hour=StringVar()
minute=StringVar()
second=StringVar()

hour_box=Entry(root,width=3,font="Arial",textvariable=hour)
hour_box.place(x=80,y=20)
hour.set(' 00 ')

mint_box=Entry(root,width=3,font="Arial",textvariable=minute)
mint_box.place(x=120,y=20)
minute.set(' 00 ')

sec_box=Entry(width=3,font="Arial",textvariable=second)
sec_box.place(x=160,y=20)
second.set(' 00 ')

def countdowntimer():
    try:
        user_input=int(hour.get())*3600 + int(minute.get())*60 +int(second.get())
    except:
        messagebox.showwarning("Invalid input !!")
    while(user_input>-1):
        mins=user_input//60
        secs=user_input%60
        hr=0
        if mins>60:
            hr=mins//60
            mins=mins%60

        hour.set("{0:2d}".format(hr))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))

        root.update()
        time.sleep(1)

        if user_input==0:
            messagebox.showinfo("Timer countdown","Time over")
        user_input-=1

btn=Button(text="Set Time Countdown",command=countdowntimer)
btn.place(x=120,y=60)
root.mainloop()
