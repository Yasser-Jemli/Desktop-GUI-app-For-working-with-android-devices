import tkinter as tk
import subprocess
import threading
import time

def run_adb_top():
    try:
        # Run the adb shell top -m 5 command and capture the output
        adb_command = ["adb", "shell", "top", "-m", "5"]
        process = subprocess.Popen(adb_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

        # Create a separate thread to continuously read and display the output
        def display_output():
            while True:
                output_line = process.stdout.readline()
                if not output_line:
                    break
                update_output_text(output_line)

        output_thread = threading.Thread(target=display_output)
        output_thread.start()
    except subprocess.CalledProcessError as e:
        # Handle errors, for example, if adb is not found
        update_output_text(f"Error: {e}")

def update_output_text(output_line):
    output_text.config(state=tk.NORMAL)
    output_text.insert(tk.END, output_line)
    output_text.config(state=tk.DISABLED)
    output_text.see(tk.END)  # Scroll to the end of the text

# Create the main window
root = tk.Tk()
root.title("ADB Shell top -m 5 Output")

# Create a Text widget to display the output
output_text = tk.Text(root, wrap=tk.WORD, height=20, width=80)
output_text.pack(padx=10, pady=10)
output_text.config(state=tk.DISABLED)  # Disable text widget for editing

# Create a button to run the adb command
run_button = tk.Button(root, text="Run adb shell top -m 5", command=run_adb_top)
run_button.pack(pady=10)

# Start the Tkinter main loop
root.mainloop()
