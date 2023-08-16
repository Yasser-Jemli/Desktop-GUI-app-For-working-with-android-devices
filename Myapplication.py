from tkinter import *
import subprocess
import threading

window =Tk()
# ************************** Application Layout & Widget ****************************************
c=Canvas(window,bg='grey',height=150,width=150)
c.grid(row=0,column=0,rowspan=10,columnspan=1,sticky='nsew')
# ************************************************************************************************
# ******* Create Terminal Output Area ************************************************************
output_text = Text(window, wrap=WORD, font=('Courier', 12))
output_text.grid(row=0,column=2,rowspan=2,columnspan=2,sticky='nsew')
#---------------------------------------------------------------------------------
# ************ Execute a Command *****************************************************************
def execute_command( command):
        try:
            result = subprocess.run(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            output = result.stdout + result.stderr
            return output
        except Exception as e :
            return f"Error: {str(e)}"
# *************************************************************************************************
# ********************* append output of a command ************************************************
def append_output( text):
        output_text.insert(END, text)
# ************************************************************************************************    
# ************** CLear the output area ***********************************************************
# ************************************************************************************************
def clear_output():
        output_text.delete(1.0,END)
# ***********************************************************************************************
#  list the adb devices & states function 
# ***********************************************************************************************
def list_devices():
        output = execute_command("adb devices")
        append_output(output)
# **********************************************************************************************
# list the availble profiles in the android device & thier states function 
# **********************************************************************************************
def list_profiles():
        output = execute_command("adb shell pm list users")
        append_output(output)
# **********************************************************************************************
# start scrcpy function
# **********************************************************************************************
def start_scrcpy():
        scrcpy_process = subprocess.Popen(["scrcpy"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        b8.config(state=DISABLED)
        b9.config(state=NORMAL)
        scrcpy_process.communicate()  # Wait for the process to finish
        return_code = scrcpy_process.returncode
        if return_code == 0:
            append_output(text='scrcpy is launched \n')  # Successful launch
            b8.config(state=DISABLED)
            b9.config(state=NORMAL)
        else:
            append_output(text='we are encounterd issues while try to launch scrcpy \n')  # Error encountered
        b8.config(state=NORMAL)
        b9.config(state=DISABLED)
# **********************************************************************************************
# Stop Scrcpy Function 
# **********************************************************************************************
def stop_scrcpy():
        if hasattr( "scrcpy_process") and scrcpy_process.poll() is None:
            scrcpy_process.terminate()
            b8.config(state=NORMAL)
            b9.config(state=DISABLED)
# *********************************************************************************************
# B1 :  to show a adb devices >> list & state 
# ************************************ adb devices *********************************************
b1=Button(window,text='adb_devices',command=list_devices)
b1.grid(row=1,column=1,rowspan=1,columnspan=1,sticky='nsew')

#***********************************************************************************************
# Button B2 : Configuration CAN-0
# **********************************************************************************************

b2=Button(window,text='CAN_Configuration : CAN-0')
b2.grid(row=0,column=0,rowspan=1,columnspan=1,sticky='nsew') 
# ***********************************************************************************************
# Button B3 : Configuration CAN-1
# ***********************************************************************************************
b3=Button(window,text='CAN_Configuration : CAN-1')
b3.grid(row=1,column=0,rowspan=1,columnspan=1,sticky='nsew')
# ***********************************************************************************************
# Button for Create Volume + : Works via adb commands 
# ***********************************************************************************************
b4=Button(window, text='volume plus 1 +')
b4.grid(row=2,column=0,rowspan=1,columnspan=1,sticky='nsew')
# ***********************************************************************************************
# Button for Create Volume - : Works via adb commands
# ***********************************************************************************************
b5=Button(window,text='volume minus 1 -') 
b5.grid(row=3,column=0,rowspan=1,columnspan=1,sticky='nsew')
# ***********************************************************************************************
# Button forDisplay the profiles list availble in the connected android device 
# ***********************************************************************************************
b6=Button(window,text='profiles',command=list_profiles)
b6.grid(row=2,column=1, rowspan=1,columnspan=1,sticky='nsew')
# ***********************************************************************************************
# Button for Create mute : works via adb commands
# ***********************************************************************************************
b6=Button(window,text='Mute')
b6.grid(row=4,column=0, rowspan=1,columnspan=1,sticky='nsew')
# ***********************************************************************************************
# Button for Clear the terminal output 
# ***********************************************************************************************
b7=Button(window,text='Clear Terminal Output',command=clear_output)
b7.grid(row=0,column=1, rowspan=1,columnspan=1,sticky='nsew')
# ***********************************************************************************************
# Button for Starting Scrcpy
# ***********************************************************************************************
b8=Button(window,text='Start Scrcpy',command=start_scrcpy)
b8.grid(row=3,column=1, rowspan=1,columnspan=1,sticky='nsew')
#************************************************************************************************
# Button for stop Scrcpy 
# ***********************************************************************************************
b9=Button(window,text='Stop Scrcpy',command=start_scrcpy)
b9.grid(row=4,column=1, rowspan=1,columnspan=1,sticky='nsew')
b9.config(state=DISABLED)
# ************************************************************************************************
# Button for Clear the terminal output 
# ***********************************************************************************************
b10=Button(window,text='restart Scrcpy every 2s')
b10.grid(row=5,column=1, rowspan=1,columnspan=1,sticky='nsew')
# ***********************************************************************************************

window.mainloop()