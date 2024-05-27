#!/usr/bin/python3.8
# Developed By Yasser JEMLI 
# Date : 27 May 2024 

# *************** Import Section **************************
import tkinter as tk
from tkinter import ttk
import subprocess
from PIL import Image, ImageTk

# Function to execute ADB commands
def execute_adb_command(command):
    try:
        result = subprocess.run(['adb'] + command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8'), result.stderr.decode('utf-8')
    except Exception as e:
        return None, str(e)

# Frame for launching animations
class AnimationFrame(tk.Frame):
    def __init__(self, master, gif_path):
        super().__init__(master, borderwidth=0, highlightthickness=0)
        self.gif_path = gif_path
        self.label = tk.Label(self, borderwidth=0, highlightthickness=0)
        self.label.pack(fill=tk.BOTH, expand=True)
        self.frames = self.load_gif()
        self.current_frame = 0
        self.animate()

    def load_gif(self):
        image = Image.open(self.gif_path)
        frames = []
        try:
            while True:
                frame = ImageTk.PhotoImage(image.copy())
                frames.append(frame)
                image.seek(len(frames))  # Move to the next frame
        except EOFError:
            pass
        return frames

    def animate(self):
        frame = self.frames[self.current_frame]
        self.label.config(image=frame)
        self.current_frame = (self.current_frame + 1) % len(self.frames)
        self.after(100, self.animate)  # Adjust the delay as necessary for your GIF

# Frame for custom widgets
class CustomWidgetFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.label = tk.Label(self, text="Custom Widget", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.button = tk.Button(self, text="Press me", command=self.on_button_press)
        self.button.pack(pady=20)

    def on_button_press(self):
        # Logic for button press
        print("Button Pressed")

# Frame for ADB terminal
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

# Main application class
class DebugApp(tk.Tk):
    def __init__(self, gif_path):
        super().__init__()
        self.title("Android Debugging Tool")
        self.geometry("800x600")
        self.create_widgets(gif_path)

    def create_widgets(self, gif_path):
        self.notebook = ttk.Notebook(self)
        
        self.animation_frame = AnimationFrame(self.notebook, gif_path)
        self.notebook.add(self.animation_frame, text='Animation')
        
        self.widget_frame = CustomWidgetFrame(self.notebook)
        self.notebook.add(self.widget_frame, text='Custom Widget')
        
        self.terminal_frame = TerminalFrame(self.notebook)
        self.notebook.add(self.terminal_frame, text='Terminal')

        self.notebook.pack(fill=tk.BOTH, expand=True)

# Splash screen class
class SplashScreen(tk.Toplevel):
    def __init__(self, master, gif_path, duration):
        super().__init__(master)
        self.overrideredirect(True)  # Remove window borders
        self.geometry("600x600")  # Set size to your GIF dimensions
        self.center_window()
        self.animation_frame = AnimationFrame(self, gif_path)
        self.animation_frame.pack(fill=tk.BOTH, expand=True)
        self.after(duration, self.destroy_splash)

    def center_window(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

    def destroy_splash(self):
        self.destroy()
        self.master.deiconify()

if __name__ == "__main__":
    gif_path = "src/animation/start_animation.gif"  # Replace with the path to your GIF
    
    # Create the main application but keep it hidden initially
    app = DebugApp(gif_path)
    app.withdraw()

    # Create and display the splash screen
    splash = SplashScreen(app, gif_path, 4000)  # Duration in milliseconds
    splash.mainloop()

    # Start the main application
    app.mainloop()