#!/usr/bin/python3.8
# Developed By Yasser JEMLI 
# Date : 27 May 2024 

# *************** Import Section **************************
import tkinter as tk
from tkinter import ttk
import subprocess

class TerminalFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.text = tk.Text(self, wrap='word', height=10)
        self.text.pack(fill=tk.BOTH, expand=True)

        self.entry = tk.Entry(self)
        self.entry.pack(fill=tk.X, pady=5)
        self.entry.bind("<Return>", self.execute_command)

    def execute_command(self, event):
        command = self.entry.get()
        self.entry.delete(0, tk.END)
        
        stdout, stderr = execute_adb_command(command)
        if stdout:
            self.text.insert(tk.END, f"$ {command}\n{stdout}\n")
        if stderr:
            self.text.insert(tk.END, f"$ {command}\n{stderr}\n")
            
def execute_adb_command(command):
    try:
        result = subprocess.run(['adb'] + command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8'), result.stderr.decode('utf-8')
    except Exception as e:
        return None, str(e)

class ADBUtils:
    @staticmethod
    def check_device_connected():
        stdout, stderr = execute_adb_command('devices')
        if 'device' in stdout:
            return True
        else:
            return False, stderr
        
class AnimationFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.label = tk.Label(self, text="Animation will be shown here", font=("Helvetica", 16))
        self.label.pack(pady=20)

    def start_animation(self):
        # Logic to start animation
        self.label.config(text="Animation Started")

class CustomWidgetFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.label = tk.Label(self, text="Custom Widget", font=("Helvetica", 16))
        self.label.pack(pady=20)

        # Example widget
        self.button = tk.Button(self, text="Press me", command=self.on_button_press)
        self.button.pack(pady=20)

    def on_button_press(self):
        # Logic for button press
        print("Button Pressed")

class DebugApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Android Debugging Tool")
        self.geometry("800x600")
        
        # Initialize Widgets
        self.create_widgets()

    def create_widgets(self):
        self.animation_frame = AnimationFrame(self)
        self.animation_frame.pack(fill=tk.BOTH, expand=True)

        self.widget_frame = CustomWidgetFrame(self)
        self.widget_frame.pack(fill=tk.BOTH, expand=True)

        self.terminal_frame = TerminalFrame(self)
        self.terminal_frame.pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    app = DebugApp()
    app.mainloop()
