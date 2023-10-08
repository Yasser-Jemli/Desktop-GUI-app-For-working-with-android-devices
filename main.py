#!/usr/bin/python3.8  
# Developed By Yasser JEMLi 2023 
# adding this line #!/usr/bin/python3.8 only to facilaite execution while coding process 

import tkinter as tk 
from tkinter  import ttk
import customtkinter
import subprocess
import threading
import time
import ttkbootstrap 
# Main Window 

root = tk.Tk()
style = ttk.Style(root)
root.tk.call("source","forest-light.tcl")
root.tk.call("source","forest-dark.tcl")
style.theme_use("forest-dark")
root.geometry('1024x800')
# menu
menu = tk.Menu(root)


# sub menu 
file_menu = tk.Menu(menu, tearoff = False)
file_menu.add_command(label = 'How To configure CAN _ bus', command = lambda: print('New file'))
file_menu.add_command(label = 'How To configure Multiple adb devices', command = lambda: print('Open file'))
file_menu.add_separator()
menu.add_cascade(label = 'How To Section ', menu = file_menu)

# another sub menu
help_menu = tk.Menu(menu, tearoff = False)
help_menu.add_command(label = 'Application Documentation', command = lambda: print(help_check_string.get()))
help_check_string = tk.StringVar()
help_menu.add_checkbutton(label = '', onvalue = 'on', offvalue = 'off', variable = help_check_string)
menu.add_cascade(label = 'Help', menu = help_menu)

# add another menu to the main menu, this one should have a sub menu
# try to read the website below and add a submenu
# docs: https://www.tutorialspoint.com/python/tk_menu.htm


# Display the menu
root.config(menu=menu)

frame = ttk.Frame(root)
frame.grid(row=0,column=0)

# scrcpy functions 
def run_adb_top():
    try:
        # Run the adb shell top -m 5 command and capture the output
        adb_command = ["adb", "shell", "top", "-m", "5"]
        process = subprocess.Popen(adb_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        stderr = process.communicate()
        append_output(stderr)
        # Create a separate thread to continuously read and display the output
        def display_output():
            while True:
                output_line = process.stdout.readline()
                if not output_line:
                    break
                update_perfo_text(output_line)

        output_thread = threading.Thread(target=display_output)
        output_thread.start()
    except subprocess.CalledProcessError as e:
        # Handle errors, for example, if adb is not found
        update_perfo_text(f"Error: {e}")

def update_perfo_text(output_line):
    output_perfo.configure(state=tk.NORMAL)
    output_perfo.insert(tk.END, output_line)
    output_perfo.configure(state=tk.DISABLED)
    output_perfo.see(tk.END)  # Scroll to the end of the text

def run_scrcpy():
        scrcpy_process = subprocess.Popen(["scrcpy"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        scrcpy_process.wait()  # Wait for the process to finish

        return_code = scrcpy_process.returncode
        if return_code == 0:
            append_output('Closing scrcpy ........\n')

        else:
            append_output('Starting Scrcpy 60% .... \n')
            append_output('we encountered issues while trying to launch scrcpy\n')
        b3.configure(state="normal")

def start_scrcpy():
        b3.configure(state="disabled")

        scrcpy_thread = threading.Thread(target=run_scrcpy)
        scrcpy_thread.start()
       
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
            append_output(f"Error: {str(e)}\n")

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

def run_bugreport(output_file="bugreport.txt"):
    try:
        # Start the adb bugreport command
        run_bugreport_thread = subprocess.Popen(["adb", "bugreport"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        # stdout , stderr = run_bugreport_thread.communicate()
        # append_output(stderr)
        # append_output(stdout)
        # Open the output file for writing
        with open(output_file, "w", encoding="utf-8") as output_file_obj:
            while True:
                output_line = run_bugreport_thread.stdout.readline()
                if not output_line:
                    break
                output_file_obj.write(output_line)
                output_file_obj.flush()
                append_output(output_line)

        # Wait for the adb bugreport command to complete
        run_bugreport_thread.wait()
        append_output('Bugreport Generation Completed.\n')

    except Exception as e:
        append_output(f"Error: {str(e)}\n")

# Your button click event handler function
def bugreport_generate():
    append_output("Bugreport Generation In Progress .... 10% ... \n")
    # Start the bugreport process in a separate thread
    append_output("Please Don't Do anything untill finshing Bugreport Generation...   \n")
    bugreport_thread = threading.Thread(target=run_bugreport)
    bugreport_thread.start()

# function for Scripts Button 
def adb_reboot():
    adb_reboot_thread = threading.Thread(target=run_reboot)
    adb_reboot_thread.start()

def run_reboot():
        try:
            run_adb_reboot = subprocess.Popen(["adb","reboot"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout,stderr = run_adb_reboot.communicate()
            append_output(text='Reboot In Progress .. 20% .. \n')
            append_output(stdout)
            append_output(stderr)
            run_adb_reboot.wait()
        except Exception as e:
             append_output(f"Error: {str(e)}\n")
         
def execute_spinbox_values():
    selected_power = power_spinbox.get()
    if selected_power == 'Adb Reboot':
        append_output("Rebooting the Device \n")
        adb_reboot()
    elif selected_power == 'Suspend To Ram':
        append_output("Suspend To Ram .. 10 % \n")
    elif selected_power == "Suspend To Disk":
         append_output("Suspend To Disk ... 10% ... \n")
    
# Switch mode  Dark/Light Function 

def toggel_mode(): 
    if mode_switch.instate(["selected"]):
        style.theme_use("forest-light")    
    else:
        style.theme_use("forest-dark")

# Label for frames are definied Here 

button_frame_label = ttk.LabelFrame(frame,text="My ADB Commands",width=200,height=200)
button_frame_label.grid(row=2, column=0,padx=1,pady=1)

power_frame_label = ttk.LabelFrame(frame,text="My Power Transistions",width=200,height=200)
power_frame_label.grid(row=0, column=0,padx=1,pady=1)

app_control = ttk.LabelFrame(frame, text="Settings",width=200,height=200)
app_control.grid(row=1,column=0,pady=1,padx=1)

terminal_frame = ttk.LabelFrame(frame, text="My terminal", width=200,height=200)
terminal_frame.grid(row=0,column=1,padx=1,pady=1)

performance_frame = ttk.LabelFrame(frame, text="Android Device Performance",width=200,height=200)
performance_frame.grid(row=1,column=1,padx=1,pady=1)

Activity_controle_frame = ttk.LabelFrame(frame, text="Device Activity",width=200,height=200)
Activity_controle_frame.grid(row=2,column=1,pady=1,padx=1)

# My terminal function 
output_text = customtkinter.CTkTextbox(terminal_frame, width=250 ,height=150)
output_text.grid(row=0, column=0,pady=1,padx=1,sticky='nsew')

output_perfo = customtkinter.CTkTextbox(performance_frame, width=250, height=150)
output_perfo.grid(row=0,column=0,pady=1,padx=1,sticky='nsew')

output_activity = customtkinter.CTkTextbox(Activity_controle_frame, width= 250 , height=150)
output_activity.grid(row=0,column=0,pady=1,padx=1,sticky='nsew')
        
def append_output(text):
        output_text.insert("end", text)

def clear_output():
        output_text.delete(1.0, "end")


# Settings Button 

mode_switch = ttk.Checkbutton(app_control, text="Mode : Dark/Light ", style="Switch",command=toggel_mode)
mode_switch.grid(row=1,column=0 , sticky="nsew")

power_spinbox = ttk.Spinbox(app_control, values=('Adb device N°1', 'Adb device N°2','Adb device N°3'))
power_spinbox.set('Select Your adb device')  # Set an initial value
power_spinbox.grid(row=2, column=0, sticky="nsew",pady=5,padx=5)

update_button = ttk.Button(app_control,text="Select Your Adb device", command=execute_spinbox_values)
update_button.grid(row=3,column=0, sticky="nsew ",pady=5,padx=5)

# button for the button_frame_label are definied Here 

b1 = ttk.Button(button_frame_label, text=" list _ adb _devices + states ", command=list_devices)
b1.grid(row=1 , column=0 , sticky="ew",pady=1,padx=1)
b2 = ttk.Button(button_frame_label , text=" list _ profiles ", command=list_profiles)
b2.grid(row=2 , column=0 , sticky="ew",pady=1, padx=1)
b3 = ttk.Button(button_frame_label, text=" Start Scrcpy ",command=start_scrcpy)
b3.grid(row=3 , column=0 , sticky="ew",padx=1,pady=1)
b5 = ttk.Button(button_frame_label, text=" Volume Up ",command=run_volume_plus)
b5.grid(row=4 , column=0 , sticky="ew",padx=1,pady=1)
b6 = ttk.Button(button_frame_label , text=" Volume Down ",command=run_volume_minus)
b6.grid(row=5 , column=0 , sticky="ew",pady=1,padx=1)
b7 = ttk.Button(button_frame_label, text="Clear Terminal",command=clear_output)
b7.grid(row=6 , column=0 , sticky="ew",pady=1,padx=1)
b8 = ttk.Button(button_frame_label,text=" Bugreport", command=bugreport_generate)
b8.grid(row=7, column=0 ,sticky="ew",pady=1,padx=1)
b9 = ttk.Button(button_frame_label, text="Check My device Performance" , command=run_adb_top)
b9.grid(row=8,column=0,sticky="ew",pady=1,padx=1)

# button for script_frame_label are definied Here 

power_spinbox = ttk.Spinbox(power_frame_label, values=('Suspend To Ram', 'Suspend To Disk','Adb Reboot'))
power_spinbox.set('Select Your Power Transition')  # Set an initial value
power_spinbox.grid(row=1, column=0, sticky="ew",pady=1,padx=1)

update_button = ttk.Button(power_frame_label, text="Make your Selected Power Transition", command=execute_spinbox_values)
update_button.grid(row=2,column=0, sticky="nsew ",pady=1,padx=1)


# Window Loop 
root.mainloop()