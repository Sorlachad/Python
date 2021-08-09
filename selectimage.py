from logging import disable
from tkinter import *
import os
import tkinter
from PIL import ImageTk, Image
from numpy.core.fromnumeric import resize
from numpy.lib.arraypad import pad


def simage():
    def ok(value):
        print(value)
        global a
        a=value
        files2 = os.listdir('D:/รวม/testimage/cam/'+str(value))
        if(files2==[]):
            print("Hello")
            OPTION=([
                "None"])
        else:
            OPTION=files2
        #files[0],
        #"Feb",
        #"Mar"
            #]  
            variable2 = StringVar(simage)
            variable2.set("เลือกขวด")
            w2 = OptionMenu(simage, variable2, *OPTION,command=ok2)
            w2.grid(row=1,column=1)
    def ok2(ch):
        print(ch)
        print(a)
        global files3
        files3=[]
        files3=os.listdir('D:/รวม/testimage/cam/'+str(a)+"/"+str(ch))
        files3=max(files3)
        files3=['D:/รวม/testimage/cam/'+str(a)+"/"+str(ch)+"/"+files3]
        Button(simage,text="กดดูภาพ",bg="white",fg="gray",bd=1,command=showim,state=NORMAL,width=20,height=5).grid(row=2,column=1,pady=50,padx=10)
    def showim():
        showimage=Toplevel()
        showimage.geometry("1024x600")
        showimage.config(bg="#c6d6c5")
        showimage.option_add("*Font","consolas 20")
        img = Image.open(files3[0])
        img = ImageTk.PhotoImage(img.resize((600, 600), Image.ANTIALIAS))
        l = Label(showimage,image=img)
        l.grid(column=0,row=0,padx=50)
        b = Button(showimage,text="Back",command=showimage.destroy,width=20)
        b.grid(column=1,row=0)
        showimage.mainloop()
    files = os.listdir('D:/รวม/testimage/cam')
    if(files==[]):
        print("Hello")
        OPTIONS = [
            "None"
        ]
    else:
        OPTIONS = files
    #files[0],
    #"Feb",
    #"Mar"
    #]
    global b1
    simage=Toplevel()
    simage.geometry("1024x600")
    simage.config(bg="#c6d6c5")
    simage.option_add("*Font","consolas 20")
    Label(simage,text="เลือกวันที่",fg="white",bg="#a1b0a0",width=10).grid(row=0,column=0,pady=50,padx=200)
    Label(simage,text="เลือกขวด",fg="white",bg="#a1b0a0",width=10).grid(row=0,column=1,pady=50,padx=180)
    variable = StringVar(simage)
    variable.set("เลือกวัน") # default value
    w = OptionMenu(simage, variable,*OPTIONS,command=ok)
    w.config(width=5)
    w.grid(row=1,column=0)
    Button(simage,text="back",bg="white",fg="gray",bd=1,command=simage.destroy,width=20,height=5).grid(row=2,column=0,pady=100,padx=10)
    simage.mainloop()   
