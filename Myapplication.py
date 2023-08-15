from tkinter import *

window =Tk()

# ******* Create Terminal Output Area ********************************
def create_output_area(self):
        self.output_text = tk.Text(self.root, wrap=tk.WORD, font=('Courier', 12))
        self.output_text.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
#---------------------------------------------------------------------------------

def execute_command( command):
        try:
            result = subprocess.run(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            output = result.stdout + result.stderr
        except Exception as e:
            output = f"Error: {str(e)}"

def append_output( text):
        output_text.insert(tk.END, text)
    

def clear_output():
        output_text.delete(1.0, tk.END)

def list_devices():
        output = execute_command("adb devices")
        append_output(output)


# B1 :  to show a adb devices >> list & state 
#************************************ adb devices *********************************************
b1=Button(window,text='adb_devices',command=list_devices)
b1.grid(row=0,column=10,rowspan=1,columnspan=1,sticky='nsew')


#***********************************************************************************************
# B2 : Configuration CAN-0

b2=Button(window,text='CAN_Configuration : CAN-0')
b2.grid(row=0,column=0,rowspan=1,columnspan=1,sticky='nsew')

# B3 : Configuration CAN-1

b3=Button(window,text='CAN_Configuration : CAN-1')
b3.grid(row=1,column=0,rowspan=1,columnspan=1,sticky='nsew')

# Create Volume + : Works via adb commands 

b4=Button(window, text='volume plus 1 +')
b4.grid(row=6,column=0,rowspan=1,columnspan=1,sticky='nsew')

# Create Volume - : Works via adb commands

b5=Button(window,text='volume minus 1 -') 
b5.grid(row=7,column=0,rowspan=1,columnspan=1,sticky='nsew')



window.mainloop()