from posixpath import split
from tkinter import *
import hHumi
import os
from os import walk
files = os.listdir('D:/โปรเจค/testfirebase')
sp=[]
def humi():
    if(files==[]):
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
        hHumi.humi=[]
        hHumi.hours=[]
        with open("D:/โปรเจค/testfirebase/"+str(value)+"/"+"temp.txt") as f:
            for line in f:
                sp=line.split("|")
                a=float(sp[0].split(",")[1])
                b=(sp[2].split("\n")[0])
                hHumi.humi.append(a)
                hHumi.hours.append(b)
        # Or: file_path = os.path.join(absolute_path, 'folder', 'my_file.py')
        #Label(humi,text=value,fg="white",bg="#a1b0a0",width=10,height=5).grid(row=1,column=2,pady=50)
    humi=Toplevel()
    humi.geometry("1024x600")
    humi.option_add("*Font","consolas 20")
    humi.config(bg="#c6d6c5")
    Label(humi,text="ความชื้น",fg="white",bg="#a1b0a0",width=10).grid(row=0,column=0,pady=50,padx=50)
    Label(humi,text="24",fg="white",width=20,height=5,bg="#a1b0a0").grid(row=1,column=0,pady=50,padx=50)
    Button(humi,text="back",bg="white",fg="gray",bd=1,command=humi.destroy,width=15,height=5).grid(row=2,column=0,padx=50)
    Button(humi,text="history",bg="white",fg="gray",bd=1,command=hHumi.hHumi,state=st,width=15,height=5).grid(row=2,column=1,pady=30)
    Label(humi,text="เลือกวัน",fg="white",bg="#a1b0a0",width=10).grid(row=0,column=1,pady=50,padx=100)
    variable = StringVar(humi)
    variable.set("เลือก") # default value
    w = OptionMenu(humi, variable, *OPTIONS,command=ok)
    w.config(width=20,height=5,font=('consolas',15))
    w.grid(row=1,column=1,pady=50,padx=200)
    humi.mainloop()