from tkinter import *
import tkinter
import home

root = Tk()
root.geometry("1024x600")
root.option_add("*Font","consolas 20")
Lable_1 = Label(root, text='ยินดีต้อนรับ', fg='blue',bg='lightblue').grid(row=0,column=0,padx=350,pady=50)
Button(root,text="เข้าสู่ระบบ",command=home.home,width=20,height=4,bd=5).grid(row=1, column=0,padx=350,pady=50)

#root.wm_attributes('-fullscreen','true')
root.mainloop()