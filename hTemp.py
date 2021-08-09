from tkinter import *
import temp
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import matplotlib.dates as md
temps=[]
hours=[]
def htemp():
    htemp=Tk()
    htemp.geometry("1024x600")
    htemp.option_add("*Font","consolas 20")
    htemp.config(bg="#c6d6c5")
    df = pd.DataFrame({'toronto_time': hours,
                    'description': temps})
    df2 = pd.DataFrame({'toronto_time': ['2018-09-08 00:00:00',
                                    '2018-09-08 01:01:55',
                                    '2018-09-08 05:02:18',
                                    '2018-09-08 07:05:24',
                                    '2018-09-08 16:05:34',
                                    '2018-09-08 23:59:59'], 
                    'description': [1, 2, 3, 4, 5, 6]})
    a=(df['toronto_time'].min())
    a2=(df['toronto_time'].max())
    b=a.split(":")
    b2=a2.split(":")
    df['toronto_time'] = pd.to_datetime(df['toronto_time'], format='%H:%M:%S')
    print(b)
    fig, ax = plt.subplots(figsize=(8,6))
    plt.plot('toronto_time', 'description', data=df)
    ax.set_xlim(df['toronto_time'].min()-pd.Timedelta(int(b[0]),'h'),
            df['toronto_time'].max()+pd.Timedelta(24-int(b2[0]),'h'))
    ax.xaxis.set_major_locator(md.HourLocator(interval = 2))
    ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M'))
    ax.set_ylim([15,40])
    ax.grid(which='minor', alpha=1)
    ax.grid(which='major', alpha=2)
    fig.autofmt_xdate()
    canvas = FigureCanvasTkAgg(fig,htemp)
    canvas.get_tk_widget().grid(column=0,row=0)
    canvas.draw()
    Button(htemp,text="back",bg="white",fg="gray",bd=1,command=htemp.destroy,width=10,height=2).grid(column=1,row=0,padx=20)
    htemp.mainloop()