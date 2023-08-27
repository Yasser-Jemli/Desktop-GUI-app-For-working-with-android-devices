import tkinter as tk 
from tkinter  import ttk
import customtkinter
import subprocess
import threading

# Main Window 

root = tk.Tk()
style = ttk.Style(root)
root.tk.call("source","forest-light.tcl")
root.tk.call("source","forest-dark.tcl")
style.theme_use("forest-dark")


# Frame are defined Here ............... 



frame = ttk.Frame(root)
frame.pack()

# scrcpy functions 

def run_scrcpy():
        scrcpy_process = subprocess.Popen(["scrcpy"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        scrcpy_process.wait()  # Wait for the process to finish

        return_code = scrcpy_process.returncode
        if return_code == 0:
            append_output('Closing scrcpy ........\n')

        else:
            append_output('we encountered issues while trying to launch scrcpy\n')
        b3.configure(state="normal")
        b4.configure(state="disabled")

def start_scrcpy():
        b3.configure(state="disabled")
        b4.configure(state="normal")

        scrcpy_thread = threading.Thread(target=run_scrcpy)
        scrcpy_thread.start()
        append_output('Starting Scrcpy 99%.... \n')

# our button functions -- adb commands 


def list_profiles():
        list_profiles_thread = threading.Thread(target=run_list_profiles)
        list_profiles_thread.start()

def run_list_profiles():
        try:
            run_profiles = subprocess.Popen(["adb" , "shell", "pm", "list", "users"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr =run_profiles.communicate()
            append_output(stdout)
            append_output(stderr)
            run_profiles.wait() 
        except Exception as e:
            append.output(f"Error: {str(e)}\n")

def list_devices():
        list_devices_thread = threading.Thread(target=run_list_devices)
        list_devices_thread.start()

def run_list_devices():
        try:
            adb_path="/usr/bin/adb" # check the Path with which adb command 
            run_devices = subprocess.Popen([adb_path,"devices"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = run_devices.communicate()
            append_output(stdout)
            append_output(stderr)
            run_devices.wait()
        except Exception as e:
            append_output(f"Error: {str(e)}\n")

def volume_plus():
        volume_plus_thread = threading.Thread(target=run_volume_plus)
        volume_plus_thread.start()

def run_volume_plus():
        try:
            run_volume_pluss = subprocess.Popen(["adb", "shell", "input" , "keyevent", "KEYCODE_VOLUME_UP"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = run_volume_pluss.communicate()
            append_output(text=' Volume Key "+" is pressed \n')
            append_output(stdout)
            append_output(stderr)
            run_volume_pluss.wait()      
        except Exception as e:
            append_output(f"Error: {str(e)}\n")
            
def volume_minus():
        volume_minus_thread = threading.Thread(target=run_volume_minus)
        volume_minus_thread.start()

def run_volume_minus():
        try:
            run_volume_minuss = subprocess.Popen(["adb","shell","input","keyevent","KEYCODE_VOLUME_DOWN"], stdout=subprocess.PIPE, stderr=subprocess.PIPE , text=True)
            stdout, stderr = run_volume_minuss.communicate()
            append_output(text=' Volume Key "-" is pressed \n')
            append_output(stdout)
            append_output(stderr)
            run_volume_minuss.wait()
        except Exception as e:
            append_output(f"Error: {str(e)}\n")
    
def mute():
        mute_thread = threading.Thread(target=run_mute)
        mute_thread.start()

def run_mute():
        try:
            run_mutee = subprocess.Popen(["adb","shell","input","keyevent","KEYCODE_MUTE"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = run_mutee.communicate()
            append_output(text='You pressed The mute Button\n')
            append_output(stdout)
            append_output(stderr)
            run_mutee.wait()
        except Exception as e:
            append_output(f"Error: {str(e)}\n")

# Label for frames are definied Here 

button_frame_label = ttk.LabelFrame(frame,text="My ADB Commands")
button_frame_label.grid(row=0, column=0, padx=20 , pady=10)

terminal_frame = ttk.LabelFrame(frame, text="My terminal")
terminal_frame.grid(row=0,column=1, padx=20 , pady=20)


# My terminal function 


output_text = customtkinter.CTkTextbox(terminal_frame, width=600 ,height=200)
output_text.grid(row=0, column=0 , sticky="nsew")

# output_text.grid(row=1 , column=0 , sticky="nsew")
        
def append_output(text):
        output_text.insert("end", text)

def clear_output():
        output_text.delete(1.0, "end")

# button for the button_frame_label are definied Here 

b1 = ttk.Button(button_frame_label, text=" list _ adb _devices + states ", command=list_devices)
b1.grid(row=1 , column=0 ,padx=5, pady=5, sticky="nsew")
b2 = ttk.Button(button_frame_label , text=" list _ profiles ", command=list_profiles)
b2.grid(row=2 , column=0 ,padx=5, pady=5, sticky="nsew")
b3 = ttk.Button(button_frame_label, text=" Start Scrcpy ",command=start_scrcpy)
b3.grid(row=3 , column=0 ,padx=5, pady=5, sticky="nsew")
b4 = ttk.Button(button_frame_label , text=" Stop Scrcpy ")
b4.grid(row=4 , column=0 ,padx=5, pady=5, sticky="nsew")
b5 = ttk.Button(button_frame_label, text=" Volume Up ",command=run_volume_plus)
b5.grid(row=5 , column=0 ,padx=5, pady=5, sticky="nsew")
b6 = ttk.Button(button_frame_label , text=" Volume Down ",command=run_volume_minus)
b6.grid(row=6 , column=0 ,padx=5, pady=5, sticky="nsew")
b7 = ttk.Button(button_frame_label, text="Clear Terminal",command=clear_output)
b7.grid(row=7 , column=0 ,padx=5, pady=5, sticky="nsew")

# Window Loop 
root.mainloop()