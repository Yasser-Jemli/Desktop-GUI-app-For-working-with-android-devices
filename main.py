from tkinter import *
import subprocess
import threading


root = Tk()
root.title("My android Controller")

scrcpy_process = None

# ************ Execute a Command *****************************************************************
def execute_command(command):
        try:
            result = subprocess.run(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            output = result.stdout + result.stderr
            return output
        except Exception as e :
            return f"Error: {str(e)}"

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

# ********************* append output of a command ************************************************
def append_output( text):
        output_text.insert(END, text)
# ************************************************************************************************    
# ************** CLear the output area ***********************************************************
# ************************************************************************************************
def clear_output():
        output_text.delete(1.0,END)
# ***********************************************************************************************

def run_scrcpy(frame):
    global scrcpy_process
    scrcpy_process = subprocess.Popen(["scrcpy"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Embed scrcpy window into the frame
    scrcpy_window = tk.Frame(frame)
    scrcpy_window.pack(fill=tk.BOTH, expand=True)
    scrcpy_process.wait()  # Wait for the process to finish

    return_code = scrcpy_process.returncode
    if return_code == 0:
        append_output(text='Loading ........\n')
        append_output(text='Scrcpy is launched \n')
    else:
        append_output(text='we encountered issues while trying to launch scrcpy\n')
    b8.config(state=NORMAL)
    b9.config(state=DISABLED)

def start_scrcpy():
    global scrcpy_process
    b8.config(state=DISABLED)
    b9.config(state=NORMAL)

    scrcpy_thread = threading.Thread(target=run_scrcpy, args=(scrcpy_frame,))
    scrcpy_thread.start()

def stop_scrcpy():
    global scrcpy_process
    if 'scrcpy_process' in globals() and scrcpy_process.poll() is None:
        scrcpy_process.terminate()
        b8.config(state=NORMAL)
        b9.config(state=DISABLED)


# Create buttons for controlling scrcpy 
b8 = Button(root, text="Start Scrcpy", command=start_scrcpy)
b8.grid(row=0,column=0,rowspan=1,columnspan=1)

b9 = Button(root, text="Stop Scrcpy", command=stop_scrcpy, state=DISABLED)
b9.grid(row=1,column=0,rowspan=1,columnspan=1)

# Create an output terminal for adb commands states 
output_text = Text(root, wrap=WORD, font=('Courier', 12))
output_text.grid(row=0,column=2,rowspan=2,columnspan=2,sticky='nsew')

# Create a frame to embed scrcpy
scrcpy_frame = Frame(root)
scrcpy_frame.grid(row=10,column=10,rowspan=10,columnspan=10)

# Button for Clear the terminal output 
# ***********************************************************************************************
b7=Button(root,text='Clear Terminal Output',command=clear_output)
b7.grid(row=0,column=1, rowspan=1,columnspan=1,sticky='nsew')

# B1 :  to show a adb devices >> list & state 
# ************************************ adb devices *********************************************
b1=Button(root,text='adb_devices',command=list_devices)
b1.grid(row=1,column=1,rowspan=1,columnspan=1,sticky='nsew')

#***********************************************************************************************
# Button forDisplay the profiles list availble in the connected android device 
# ***********************************************************************************************
b6=Button(root,text='profiles',command=list_profiles)
b6.grid(row=2,column=1, rowspan=1,columnspan=1,sticky='nsew')
# ***********************************************************************************************

# Run the Tkinter event loop
root.mainloop()
