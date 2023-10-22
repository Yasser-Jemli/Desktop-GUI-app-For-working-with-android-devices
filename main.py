#!/usr/bin/python3.8  
# Developed By Yasser JEMLi 2023 
# adding this line #!/usr/bin/python3.8 only to make execution of spec feature easy    

import tkinter as tk 
from tkinter  import ttk
import customtkinter
import subprocess
import threading
import time
import ttkbootstrap as ttk
from tkinter import messagebox
import os 

# Main Window 
root = ttk.Window()
style = ttk.Style

root.title("My Android Helper ")
# add a fix for changing screen resolution 
# we shall control the changes of the screen resolution from pc to another to fix this 

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
print(width,height)
configuration = f'{width}x{height}'
print(configuration)

# i add this fix but i should test it with different screen size to confirm if it's working or not 
root.geometry(configuration) # this workaround didn't fix the issue : we shall fix it soon 

# to fix this with variable Path 
image_var= 'Untitled.png' 
absolute_path =  os.path.join(os.getcwd(),image_var)
print(f'this is the path : {absolute_path}') # debug statement that the Path is correctly selected
root.iconphoto(True, tk.PhotoImage(file=absolute_path))

root.tk.call('tk','scaling',2.0)

# menu
menu = tk.Menu(root)

# Create a notebook to switch between pages
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# Main frame
frame = ttk.Frame(notebook)
notebook.add(frame)

def missing_feature():
    # help_frame
    help_frame = ttk.Frame(notebook)
    notebook.add(help_frame)
    notebook.select(help_frame)
    back_button = ttk.Button(help_frame, text="Back", command=show_main)
    back_button.pack(pady=20)
    messagebox.showinfo("Missing Manuel","This Feature is not availble yet !")

def show_main():
        # Switch back to the main page
        notebook.select(frame)
        
# sub menu 
file_menu = tk.Menu(menu, tearoff = False)
file_menu.add_command(label = 'How To configure CAN _ bus',background='green', command =missing_feature)
file_menu.add_separator()
file_menu.add_command(label = 'How To configure Multiple adb devices',background='green', command = missing_feature)
file_menu.add_separator()
file_menu.add_command(label = 'Scrcpy issues & Fixes',background='green',command = missing_feature)

menu.add_cascade(label = 'How To Section ', menu = file_menu)

# another sub menu
help_menu = tk.Menu(menu, tearoff = False)
help_menu.add_command(label = 'Application Documentation', command =missing_feature)
help_check_string = tk.StringVar()
help_menu.add_checkbutton(label = '', onvalue = 'on', offvalue = 'off', variable = help_check_string)
menu.add_cascade(label = 'Help', menu = help_menu)

# add another menu to the main menu, this one should have a sub menu
# try to read the website below and add a submenu
# docs: https://www.tutorialspoint.com/python/tk_menu.htm

# Display the menu
root.config(menu=menu)

# initial adb device Value ( Serial Number)
selected_device = None

# intial Process var as None which is the Process THat Handels the Performance Command
process = None  # Initialize process as None

def get_connected_adb_devices():
    try:
        # Run the adb devices command and capture the output
        result = subprocess.run(["adb", "devices"], capture_output=True, text=True, check=True)

        # Split the output into lines
        lines = result.stdout.strip().split("\n")

        # Initialize a list to store the serial numbers of connected devices
        connected_devices = []

        # Start from the second line (skipping the header "List of devices attached")
        for line in lines[1:]:
            parts = line.split()
            if len(parts) == 2 and parts[1] == "device":
                # If the line has two parts and the second part is "device," it's a connected device
                connected_devices.append(parts[0])

        # Return the list of connected device serial numbers
        return connected_devices

    except subprocess.CalledProcessError as e:
        print("Error running adb devices:", e)
        return []

# Callback function to update the selected device
def update_selected_device():
    global selected_device
    selected_device = adb_spinbox.get()
    if selected_device == 'Select Your adb device' :
        selected_device = None 
        messagebox.showerror("Error","No adb device is Selected \n please Insert & Select and Adb device")
    else : 
    # debug state to display if we correctly select the target adb devices
        print("The Selected Device is :",selected_device)
        append_output(text=f'The Selected Device is : {selected_device}\n')

# Start The Performance Check Process if we have an adb device selected 
# if not we throw a messagbox Error That No adb device was Selected
def run_adb_top():
    global process
    if selected_device is not None:
        try:
            # Run the adb shell top -m 5 command and capture the output
            adb_command = ["adb", "-s", selected_device, "shell", "top", "-m", "5"]
            process = subprocess.Popen(adb_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
            
            # Create a separate thread to continuously read and display the output
            def display_output():
                while True:
                    output_line = process.stdout.readline()
                    if not output_line:
                        break
                    root.after(10, update_perfo_text, output_line)  # Schedule GUI update

            output_thread = threading.Thread(target=display_output)
            output_thread.start()
        except subprocess.CalledProcessError as e:
            # Handle errors, for example, if adb is not found
            update_perfo_text(f"Error: {e}")
            
    else : 
        messagebox.showerror("Error !","No Adb device was Selected !")
        
# Function For Update The Performance State Of device in the Performance Box 
def update_perfo_text(output_line):
    output_perfo.configure(state=tk.NORMAL)
    output_perfo.insert(tk.END, output_line)
    output_perfo.configure(state=tk.DISABLED)
    output_perfo.see(tk.END)
# Add function to clear the Performance text zone   
def clear_output_perfo():
        output_perfo.delete(1.0, "end")
# scrcpy function to launch a sperate Thread of the Selected Device 
def run_scrcpy():
        # Now Its working even if we have Multiple Adb devices connected 
        global selected_device
        if selected_device is not None:
            append_output(f'Launching Scrcpy On {selected_device}\n')
            scrcpy_process = subprocess.Popen(["scrcpy","-s",selected_device], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            scrcpy_process.wait()  # Wait for the process to finish

            return_code = scrcpy_process.returncode
            print(return_code)
            if return_code == 0:
                closing_message = f'Closing scrcpy of {selected_device}\n'
                append_output(closing_message)
                b3.configure(state="normal")
            else : 
                append_output('we encountered issues while trying to launch scrcpy\n')
                b3.configure(state="normal")

        else :
            # This is a fix Of No adb device was selected  
            append_output('No Adb device was Selected\n')
            messagebox.showerror("Error !","No Adb device was Selected")
            b3.configure(state="normal")

# Call the Scrcpy Function with Disabling the Button State For a while Untill 
# We check if we have an adb device connected or not and decide 
def start_scrcpy():
        b3.configure(state="disabled")
        scrcpy_thread = threading.Thread(target=run_scrcpy)
        scrcpy_thread.start()
        

def list_profiles():
        list_profiles_thread = threading.Thread(target=run_list_profiles)
        list_profiles_thread.start()

def run_list_profiles():
        global selected_device
        if selected_device is not None:
            try:
                run_profiles = subprocess.Popen(["adb" ,"-s",selected_device,"shell", "pm", "list", "users"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                stdout, stderr =run_profiles.communicate()
                append_output(stdout)
                append_output(stderr)
                run_profiles.wait() 
            except Exception as e:
                append_output(f"Error: {str(e)}\n")
        else:
            print("No ADB device selected.")
            messagebox.showerror("Error !","No Adb device was Selected !")
            
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
        global selected_device
        if selected_device is not None:
            try:
                run_volume_pluss = subprocess.Popen(["adb", "-s",selected_device,"shell", "input" , "keyevent", "KEYCODE_VOLUME_UP"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                stdout, stderr = run_volume_pluss.communicate()
                append_output(text=' Volume Key "+" is pressed \n')
                append_output(stdout)
                append_output(stderr)
                run_volume_pluss.wait()      
            except Exception as e:
                append_output(f"Error: {str(e)}\n")
        else:
            print("No ADB device selected.")
            messagebox.showerror("Error !","No Adb device was Selected !")

def volume_minus():
        volume_minus_thread = threading.Thread(target=run_volume_minus)
        volume_minus_thread.start()

def run_volume_minus():
        global selected_device
        if selected_device is not None:
            try:
                run_volume_minuss = subprocess.Popen(["adb","-s",selected_device,"shell","input","keyevent","KEYCODE_VOLUME_DOWN"], stdout=subprocess.PIPE, stderr=subprocess.PIPE , text=True)
                stdout, stderr = run_volume_minuss.communicate()
                append_output(text='Volume Key "-" is pressed on \n')
                append_output(stdout)
                append_output(stderr)
                run_volume_minuss.wait()
            except Exception as e:
                append_output(f"Error: {str(e)}\n")
        else:
            print("No ADB device selected.")
            messagebox.showerror("Error !","No Adb device was Selected !")

def mute():
        mute_thread = threading.Thread(target=run_mute)
        mute_thread.start()

def run_mute():
        global selected_device
        if selected_device is not None:
            try:
                run_mutee = subprocess.Popen(["adb","-s",selected_device,"shell","input","keyevent","KEYCODE_MUTE"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                stdout, stderr = run_mutee.communicate()
                append_output(text='You pressed The mute Button\n')
                append_output(stdout)
                append_output(stderr)
                run_mutee.wait()
            except Exception as e:
                append_output(f"Error: {str(e)}\n")
        else:
            print("No ADB device selected.")
            messagebox.showerror("Error !","No Adb device was Selected !")

def run_bugreport(output_file="bugreport.txt"):
    global selected_device
    if selected_device is not None:
    # Showing Information To the User about Bugreport Generation Process
    # If the Target Device Selected has an old Android Version it will Generate A txt File as Bugreport
    # If The Target Device has a New Android version it will Generate a zip file as bugreport 
        messagebox.showinfo("Info","If you're Using older android version you will have a txt file as a bugreport , if not You will find a Zip File As a bug report ")
        try:
            append_output("Bugreport Generation In Progress .... 10% ... \n")
            append_output("Please Don't Do anything untill finshing Bugreport Generation...   \n")
        # Start the adb bugreport command
            run_bugreport_thread = subprocess.Popen(["adb","-s",selected_device, "bugreport"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
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
    else:
            print("No ADB device selected.")
            messagebox.showerror("Error !","No Adb device was Selected !")

# Function TO start the Bugreport_Greneration Thread 
def bugreport_generate():
    # Start the bugreport process in a separate thread
    bugreport_thread = threading.Thread(target=run_bugreport)
    bugreport_thread.start()

# Function to start the Adb_reboot_Process Thread 
def adb_reboot():
    adb_reboot_thread = threading.Thread(target=run_reboot)
    adb_reboot_thread.start()

# Callback function to check if we have a selected device to make the reboot or not  
def run_reboot():
        global selected_device
        if selected_device is not None: 
            try:
                run_adb_reboot = subprocess.Popen(["adb","reboot"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                stdout,stderr = run_adb_reboot.communicate()
                append_output(text='Reboot In Progress .. 20% .. \n')
                append_output(stdout)
                append_output(stderr)
                run_adb_reboot.wait()
                append_output(text='Reboot Is done')
            except Exception as e:
                append_output(f"Error: {str(e)}\n")
        else:
            messagebox.showerror("Error ! " , "No Adb device was selected !")
             
def execute_spinbox_values():
    messagebox.showinfo("Feature Not AVailble","This Feature is not yet availble")
    selected_power = power_spinbox.get()
    if selected_power == 'ShutDown':
        append_output("Rebooting the Device \n")
        append_output("Feature Is Not availble Yet..\n")
    elif selected_power == 'Suspend To Ram':
        append_output("Suspend To Ram .. 10 % \n")
        append_output("Feature Is Not availble Yet..\n")
    elif selected_power == "Suspend To Disk":
         append_output("Suspend To Disk ... 10% ... \n")
         append_output("Feature Is Not availble Yet..\n")
    
def execute_spec_android_tool():
     messagebox.showinfo("Feature Not Availble","This Feature is not yet availble")
                            
# Label for frames are definied Here 

power_frame_label = ttk.LabelFrame(frame,text="My Power Transistions",width=200,height=200)
power_frame_label.grid(row=0, column=0,padx=1,pady=1)

app_control = ttk.LabelFrame(frame, text="Settings",width=200,height=200)
app_control.grid(row=1,column=0,pady=1,padx=1)

button_frame_label = ttk.LabelFrame(frame,text="My ADB Commands",width=200,height=200)
button_frame_label.grid(row=2, column=0,padx=1,pady=1)

terminal_frame = ttk.LabelFrame(frame, text="My terminal", width=200,height=200)
terminal_frame.grid(row=0,column=1,padx=1,pady=1)

performance_frame = ttk.LabelFrame(frame, text="Android Device Performance",width=200,height=200)
performance_frame.grid(row=1,column=1,padx=1,pady=1)

Activity_controle_frame = ttk.LabelFrame(frame, text="Device Activity",width=200,height=200)
Activity_controle_frame.grid(row=2,column=1,pady=1,padx=1)

# My terminal function 
output_text = customtkinter.CTkTextbox(terminal_frame,fg_color='white',text_color='black', width=350 ,height=150)
output_text.grid(row=0, column=0,pady=1,padx=1,sticky='nsew')

output_perfo = customtkinter.CTkTextbox(performance_frame,fg_color='white',text_color='black',width=350, height=150)
output_perfo.grid(row=0,column=0,pady=1,padx=1,sticky='nsew')

output_activity = customtkinter.CTkTextbox(Activity_controle_frame, width= 350 ,fg_color='white',text_color='black', height=150)
output_activity.grid(row=0,column=0,pady=1,padx=1,sticky='nsew')
        
def append_output(text):
        output_text.insert("end", text)

def clear_output():
        output_text.delete(1.0, "end")

# Switch mode  Dark/Light Function 
# still to be fixed with bootstrap theme
# For the Moment we display an info message of feature Not availble

def toggel_mode(): 
    if mode_switch.instate(["selected"]):
        style.theme_use(themename='darkly')
        # messagebox.showinfo("Feature Not AVailble","This Feature is not yet availble")
    else:
        style.theme_use(themename='sandstone')
        # messagebox.showinfo("Feature Not AVailble","This Feature is not yet availble")

def update_perfo_toggel():
    if performance_switch.instate(["selected"]):
        run_adb_top()
    else:
        # check if the Process Thread is running and terminate the process with a Message
        if process:
            process.terminate()  # Terminate the running process
            obj = f'Checking Performance is Stopped on device : {selected_device}\n'           
            update_perfo_text(obj) 
        else:
            if selected_device is not None : 
                messagebox.showinfo("Info","No Checking Performance Thread Is running For the Moment")  
                update_perfo_text("There's No Checking Performance Process is running")
            else : 
                 messagebox.showerror("Error ! " , "No Adb device Was Selected")
# Settings Button ..

mode_switch = ttk.Checkbutton(app_control, text="Mode : Dark/Light ", style="Switch",command=toggel_mode)
mode_switch.grid(row=0,column=0 , sticky="ew",pady=1,padx=1)

# performance Check Button 

performance_switch = ttk.Checkbutton(app_control,text="Check Your Device Performance",style="Switch",command=update_perfo_toggel)
performance_switch.grid(row=4,column=0,sticky="ew",pady=1,padx=1)

# clear the Performance Check text Box 
# bug here => the button is not clearing the performance screen 
clear_button = ttk.Button(app_control,text="Clear Performance Terminal",command=clear_output_perfo)
clear_button.grid(row=5,column=0,sticky='ew',pady=1,padx=1)

# Here we have a bug , the refresh is not happend for the adb devices 
# Need to Be fixed Soon 
connected_devices = get_connected_adb_devices()
adb_spinbox = ttk.Spinbox(app_control, values=connected_devices)
adb_spinbox.set('Select Your adb device')  # Set an initial value
adb_spinbox.grid(row=1, column=0, sticky="nsew",pady=1,padx=1)

# Bind the Spinbox widget to the callback function
adb_spinbox.bind("<<SpinboxSelected>>", update_selected_device)

update_button = ttk.Button(app_control, text="Select Your Target Adb from the List ", command=update_selected_device)
update_button.grid(row=2,column=0, sticky="nsew ",pady=1,padx=1)
# Switch the Clear button Here in the settings menu for the moment
b7 = ttk.Button(app_control, text="Clear Terminal",command=clear_output)
b7.grid(row=3 , column=0 , sticky="ew",pady=1,padx=1)
# button for the button_frame_label are definied Here 

b1 = ttk.Button(button_frame_label, text="        list _ adb _devices + states     ", command=list_devices)
b1.grid(row=1 , column=0 , sticky="ew",pady=1,padx=1)
b2 = ttk.Button(button_frame_label , text=" list _ profiles ", command=list_profiles)
b2.grid(row=2 , column=0 , sticky="ew",pady=1, padx=1)
b3 = ttk.Button(button_frame_label, text=" Start Scrcpy ",command=start_scrcpy)
b3.grid(row=3 , column=0 , sticky="ew",padx=1,pady=1)
b5 = ttk.Button(button_frame_label, text=" Volume Up ",command=run_volume_plus)
b5.grid(row=4 , column=0 , sticky="ew",padx=1,pady=1)
b6 = ttk.Button(button_frame_label , text=" Volume Down ",command=run_volume_minus)
b6.grid(row=5 , column=0 , sticky="ew",pady=1,padx=1)
b8 = ttk.Button(button_frame_label,text=" Bugreport", command=bugreport_generate)
b8.grid(row=7, column=0 ,sticky="ew",pady=1,padx=1)
b4 = ttk.Button(button_frame_label, text="adb_reboot",command=adb_reboot)
b4.grid(row=8,column=0,sticky="ew",pady=1,padx=1)

# button for script_frame_label are definied Here 

power_spinbox = ttk.Spinbox(power_frame_label, values=('Suspend To Ram', 'Suspend To Disk','ShutDown'))
power_spinbox.set("select you power trasistion")  # Set an initial value
power_spinbox.grid(row=1, column=0, sticky="ew",pady=1,padx=1)

update_button = ttk.Button(power_frame_label, text="Make your Selected Power Transition", command=execute_spinbox_values)
update_button.grid(row=2,column=0, sticky="nsew ",pady=1,padx=1)

Spec_android_tools = ttk.Spinbox(power_frame_label,values=('Volume_up','Volume_down','specifique_reboot'))
Spec_android_tools.set("Select your action")
Spec_android_tools.grid(row=3,column=0,sticky="ew",pady=1,padx=1)
# to add spec function to handle the Soec_android_tools actions
update_button2 = ttk.Button(power_frame_label,text="Select Your action",command=execute_spec_android_tool)
update_button2.grid(row=4,column=0,sticky='nsew',pady=1,padx=1)
# Window Loop 
root.mainloop()