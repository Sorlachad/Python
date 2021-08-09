from tkinter import *

from numpy.core.fromnumeric import resize
import temp
import bottle
import humi
import selectimage
from PIL import ImageTk, Image
def home():
    root=Toplevel()
    root.geometry("1024x600")
    root.option_add("*Font","Times 20 bold")
    #home=Toplevel(root)
    #home.geometry("1024x600")
    root.config(bg="#c6d6c5")
    bot=PhotoImage(file='D:/โปรเจค/bottle.png')
    tem=PhotoImage(file='D:/โปรเจค/temp.png')
    hum=PhotoImage(file='D:/โปรเจค/Humi.png')
    img=PhotoImage(file='D:/โปรเจค/button2.png')
    Lable_1 = Label(root, text='ยินดีต้อนรับ', fg='white',bg="#c6d6c5").grid(row=0,column=1,pady=50)
    Button(root,text="bottle",fg='black',command=selectimage.simage,image=bot
    ,borderwidth=0,highlightthickness= 0,width=200,height=200,bg="#c6d6c5",activebackground="#c6d6c5").grid(row=1, column=0,padx=70)

    Button(root,text="temp",command=temp.temp,bd=5,image=tem
    ,borderwidth=0,highlightthickness= 0,width=200,height=200,bg="#c6d6c5",activebackground="#c6d6c5").grid(row=1, column=1,padx=70)

    Button(root,text="humi",fg="blue",command=humi.humi
    ,borderwidth=0,highlightthickness= 0,width=200,height=200,bg="#c6d6c5",image=hum,activebackground="#c6d6c5").grid(row=1, column=2,padx=70)

    Button(root,text="light",fg="blue"
    ,borderwidth=0,highlightthickness= 0,width=200,height=200,bg="#c6d6c5",image=img,activebackground="#c6d6c5").grid(row=2, column=0,padx=70,pady=10)

    Button(root,text="ozone",fg="blue" 
    ,borderwidth=0,highlightthickness= 0,width=200,height=200,bg="#c6d6c5",image=img,activebackground="#c6d6c5").grid(row=2, column=1,padx=70,pady=10)

    Button(root,text="camera",fg="blue"
    ,borderwidth=0,highlightthickness= 0,width=200,height=200,bg="#c6d6c5",image=img,activebackground="#c6d6c5").grid(row=2, column=2,padx=70,pady=10)

    root.mainloop()