import tkinter as tk
from tkinter import ttk
import subprocess
import pexpect

# Global variable to store the previous activity
previous_activity = ""

def check_adb_connection():
    try:
        # Check if the device is connected and authorized using ADB
        adb_check = subprocess.Popen(["adb", "devices"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        adb_out, adb_err = adb_check.communicate()
        
        if "List of devices attached" in adb_out.decode():
            return True
        else:
            return False
    except Exception as e:
        return False

def get_current_activity():
    global previous_activity
    try:
        # Run the adb shell command to get the current activity
        adb_shell = pexpect.spawn("adb shell dumpsys activity activities | grep mFocusedActivity")
        adb_shell.expect(pexpect.EOF)
        current_activity = adb_shell.before.decode("utf-8").strip()

        # Display the current activity in the tkinter text widget
        activity_text.config(state=tk.NORMAL)
        activity_text.delete(1.0, tk.END)
        activity_text.insert(tk.END, current_activity)
        activity_text.config(state=tk.DISABLED)
        
        # Check if the activity has changed
        if current_activity != previous_activity:
            previous_activity = current_activity
    except Exception as e:
        activity_text.config(state=tk.NORMAL)
        activity_text.delete(1.0, tk.END)
        activity_text.insert(tk.END, "Error: " + str(e))
        activity_text.config(state=tk.DISABLED)

def start_gui():
    # Create the tkinter window
    global root
    root = tk.Tk()
    root.title("Android Activity Tracker")

    # Create a text widget to display the current activity
    global activity_text
    activity_text = tk.Text(root, height=10, width=50)
    activity_text.pack(padx=10, pady=10)
    activity_text.config(state=tk.DISABLED)

    # Create a button to trigger the get_current_activity function
    get_activity_button = ttk.Button(root, text="Get Activity", command=get_current_activity)
    get_activity_button.pack(padx=10, pady=10)

    # Check ADB connection and display error message label if not connected
    if not check_adb_connection():
        adb_error_label = ttk.Label(root, text="ADB Error: Please connect and authorize your Android device using ADB.")
        adb_error_label.pack(padx=10, pady=10)

    root.mainloop()

# Start the GUI
start_gui()
