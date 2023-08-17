from tkinter import * 


window =Tk()

# Create a button

b1=Button(text='Hello')
b1.pack()
b1.grid(row=0,column=0)

# Note Grid and Pack and Place are three window Managers shouldn't be used in the same application 
# that's why in our projec we will use only grid   
# ... add more widgets and configurations to the adb_devices Frame

window.mainloop()