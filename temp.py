from posixpath import split
from tkinter import *
from PIL import ImageTk, Image
from matplotlib.pyplot import colorbar
from numpy.core.fromnumeric import resize
import hTemp
import os
from os import walk
files = os.listdir('D:/โปรเจค/testfirebase')
sp=[]
back2=Image
def temp():
    if(files==[]):
        print("Hello")
        OPTIONS = [
            "None"
        ]
        st=DISABLED
    else:
        OPTIONS = files
        #files[0],
        #"Feb",
        #"Mar"
        #]
        st=ACTIVE
    def ok(value):
        print("value is:"+value)
        hTemp.temps=[]
        hTemp.hours=[]
        with open("D:/โปรเจค/testfirebase/"+str(value)+"/"+"temp.txt") as f:
            for line in f:
                sp=line.split("|")
                a=float(sp[0].split(",")[0])
                b=(sp[2].split("\n")[0])
                hTemp.temps.append(a)
                hTemp.hours.append(b)
        # Or: file_path = os.path.join(absolute_path, 'folder', 'my_file.py')
        #Label(temp,text=value,fg="white",bg="#a1b0a0",width=10,height=5).grid(row=1,column=2,pady=50)
    temp=Toplevel()
    temp.geometry("1024x600")
    temp.option_add("*Font","Times 20")
    temp.config(bg="#c6d6c5")
    frame=Frame(temp,bg="#8CA76D")
    frame.place(x=600,y=0,bordermode='ignore',width=424,height=600)
    back2=PhotoImage(file='D:/โปรเจค/button4.png')

    Label(temp,text="อุณหภูมิ",fg="white",bg="#a1b0a0",width=10).grid(row=0,column=0,pady=50,padx=50)
    Label(temp,text="24",fg="white",bg="#a1b0a0",width=20,height=5).grid(row=1,column=0,pady=50,padx=50)
    Button(temp,text="back",bg="#c6d6c5"
    ,borderwidth=0,fg="black",width=400,height=200,image=back2,activebackground="#c6d6c5",command=temp.destroy).grid(row=2,column=0,padx=50) 

    Button(frame,text="history",bg="#FFFFFF",fg="black",activebackground="#FFFFFF",command=hTemp.htemp,state=st,width=15,height=5).grid(row=2,column=0,pady=20,padx=100)
    Label(frame,text="เลือกวัน",fg="white",bg="#a1b0a0",width=10).grid(row=0,column=0,pady=50,padx=100)
    variable = StringVar(temp)
    variable.set("เลือก") # default value
    w = OptionMenu(frame, variable, *OPTIONS,command=ok)
    w.config(width=20,height=5,bg="#D4E3C3",activebackground="#D4E3C3",fg="white",font=('Times',15))
    w["menu"].config(bg="white")
    w.grid(row=1,column=0,pady=50,padx=100)
    temp.mainloop()