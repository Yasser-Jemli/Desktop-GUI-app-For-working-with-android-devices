import tkinter as tk
import subprocess
import re


app = tk.Tk()
app.title("Android Control App")

output_text = tk.Text(app, height=10, width=50)
output_text.pack()

cpu_label = tk.Label(app, text="CPU Usage:")
cpu_label.pack()

ram_label = tk.Label(app, text="RAM Usage:")
ram_label.pack()

# Function to update the UI with CPU and RAM usage
def update_ui():
    # Run 'top -n 1' command and capture its output
    top_output = subprocess.check_output(["adb", "shell", "top", "-n", "1"]).decode("utf-8")
    
    # Extract CPU and RAM usage percentages using regular expressions
    cpu_match = re.search(r"%Cpu\(s\):.*?([\d\.]+)%", top_output)
    ram_match = re.search(r"KiB Mem :.*?([\d\.]+) used,", top_output)

    if cpu_match:
        cpu_usage = cpu_match.group(1)
    else:
        cpu_usage = "N/A"

    if ram_match:
        ram_usage = ram_match.group(1)
    else:
        ram_usage = "N/A"

    # Update labels
    cpu_label.config(text=f"CPU Usage: {cpu_usage}%")
    ram_label.config(text=f"RAM Usage: {ram_usage.strip()} KiB")
    
    # Update text widget with the entire 'top' command output
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, top_output)
    
    # Schedule the function to run again after 1 second
    app.after(1000, update_ui)

# Start the updating process
update_ui()

app.mainloop()
