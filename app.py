import tkinter as tk
import subprocess
import threading
from PIL import Image, ImageTk

class SplashScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Loading...")
        
        self.show_logo()
        
    def show_logo(self):
        self.logo_image = Image.open("/home/yasser/Desktop-GUI-app-For-working-with-android-devices/logo.png")  # Replace with the path to your logo image
        self.logo_image = self.logo_image.resize((400, 400))  
        self.logo_photo = ImageTk.PhotoImage(self.logo_image)
        
        self.logo_label = tk.Label(self.root, image=self.logo_photo)
        self.logo_label.pack()

        self.root.after(2000, self.close_splash)

    def close_splash(self):
        self.root.destroy()

class AdbApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ADB Command Executor")
        
        self.create_ui()
        self.performance_thread = None
    def create_ui(self):
        self.create_buttons()
        self.create_output_area()
        self.create_scrcpy_area()
        self.create_performance_area()
        
    def create_buttons(self):
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(padx=10, pady=10)

        self.devices_button = tk.Button(self.buttons_frame, text="List Devices", command=self.list_devices)
        self.devices_button.pack(fill=tk.X, pady=5)

        self.users_button = tk.Button(self.buttons_frame, text="List Users", command=self.list_users)
        self.users_button.pack(fill=tk.X, pady=5)

        self.clear_button = tk.Button(self.buttons_frame, text="Clear", command=self.clear_output)
        self.clear_button.pack(fill=tk.X, pady=5)

        self.start_scrcpy_button = tk.Button(self.buttons_frame, text="Start Scrcpy", command=self.start_scrcpy)
        self.start_scrcpy_button.pack(fill=tk.X, pady=5)

        self.stop_scrcpy_button = tk.Button(self.buttons_frame, text="Stop Scrcpy", command=self.stop_scrcpy, state=tk.DISABLED)
        self.stop_scrcpy_button.pack(fill=tk.X, pady=5)

        self.performance_button = tk.Button(self.buttons_frame, text="Show Performance", command=self.start_performance)
        self.performance_button.pack(fill=tk.X, pady=5)

        
    def create_performance_area(self):
        self.performance_frame = tk.Frame(self.root)
        self.performance_frame.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
        
        self.performance_text = tk.Text(self.performance_frame, wrap=tk.WORD, font=('Courier', 12))
        self.performance_text.pack(fill=tk.BOTH, expand=True)
    
    def start_performance(self):tkinter
        if self.performance_thread is None or not self.performance_thread.is_alive():
            self.performance_thread = threading.Thread(target=self.monitor_performance)
            self.performance_thread.start()
        else:
            print("Performance monitoring is already running.")
    
    def monitor_performance(self):
        try:
            process = subprocess.Popen(["adb", "shell", "top", "-H"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            self.read_performance_output(process)
        except Exception as e:
            print("Error monitoring performance:", str(e))
    
    def read_performance_output(self, process):
        line = process.stdout.readline()
        if line:
            self.update_performance_output(line.strip())
            self.root.after(100, self.read_performance_output, process)
        else:
            process.terminate()
    
    def update_performance_output(self, line):
        self.performance_text.insert(tk.END, line + "\n")
        self.performance_text.see(tk.END)

    def create_output_area(self):
        self.output_text = tk.Text(self.root, wrap=tk.WORD, font=('Courier', 12))
        self.output_text.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
        
    def create_scrcpy_area(self):
        self.scrcpy_frame = tk.Frame(self.root)
        self.scrcpy_frame.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
        
        self.scrcpy_label = tk.Label(self.scrcpy_frame, text="Scrcpy screen will appear here")
        self.scrcpy_label.pack()
        
    def list_devices(self):
        output = self.execute_command("adb devices")
        self.append_output(output)
    
    def list_users(self):
        output = self.execute_command("adb shell pm list users")
        self.append_output(output)
    
    def execute_command(self, command):
        try:
            result = subprocess.run(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            output = result.stdout + result.stderr
        except Exception as e:
            output = f"Error: {str(e)}"
        
        return output
    
    def append_output(self, text):
        self.output_text.insert(tk.END, text)
    
    def clear_output(self):
        self.output_text.delete(1.0, tk.END)
    
    def start_scrcpy(self):
        self.scrcpy_process = subprocess.Popen(["scrcpy"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        self.start_scrcpy_button.config(state=tk.DISABLED)
        self.stop_scrcpy_button.config(state=tk.NORMAL)
    
    def stop_scrcpy(self):
        if hasattr(self, "scrcpy_process") and self.scrcpy_process.poll() is None:
            self.scrcpy_process.terminate()
            self.start_scrcpy_button.config(state=tk.NORMAL)
            self.stop_scrcpy_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    splash_root = tk.Toplevel(root)
    splash_app = SplashScreen(splash_root)
    splash_root.withdraw()  # Hide the splash window temporarily
    root.withdraw()  # Hide the root window temporarily
    
    def show_main_app():
        root.deiconify()  # Show the root window
        root.title("ADB Command Executor")  # Set title again
        app = AdbApp(root)
        
        
    root.after(2000, show_main_app)  # Delay to show the main app
    
    root.mainloop()