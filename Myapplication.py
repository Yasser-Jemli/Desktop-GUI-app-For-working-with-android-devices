from tkinter import *
from tkinter.font import Font 


window=Tk()
window.title("my android monitor")
window.geometry("960x960")
#color declaration 


# labels declaration 
main_label = Label(window,text='welcome to our application',bg='green').pack()

# button declaration 

adb_devices=Button(window, text='adb devices',width=10,pady= 5 ,padx =5,font=Font(family='tahome', size =10, weight='bold')).pack()


window.mainloop()