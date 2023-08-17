import customtkinter # you should install pip3 install customtkinter
import subprocess
import threading

customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

root = customtkinter.CTk(fg_color="grey")  # create CTk window like you do with the Tk window
root.geometry("1024x1024")
class ScrcpyController:
    def __init__(self, root):
        self.root = root
        self.root.title("My Android Controller")
        
        self.scrcpy_process = None
        
        self.create_buttons()
        self.create_output_terminal()

    
    def create_buttons(self):
        self.b8 = customtkinter.CTkButton(master=self.root, text="Start Scrcpy", command=self.start_scrcpy,border_color="dark")
        self.b8.grid(row=0, column=0, rowspan=1, columnspan=1)
        
        self.b9 = customtkinter.CTkButton(master=self.root, text="Stop Scrcpy",fg_color='red', command=self.stop_scrcpy, state="disabled", border_color="dark")
        self.b9.grid(row=1, column=0, rowspan=1, columnspan=1)
        
        self.b7 = customtkinter.CTkButton(master=self.root, text='Clear Terminal Output', command=self.clear_output,border_color="dark")
        self.b7.grid(row=0, column=1, rowspan=1, columnspan=1)
        
        self.b1 = customtkinter.CTkButton(master=self.root, text='adb_devices',border_color="dark")
        self.b1.grid(row=1, column=1, rowspan=1, columnspan=1)
        
        self.b6 = customtkinter.CTkButton(self.root, text='profiles',border_color="dark")
        self.b6.grid(row=2, column=1, rowspan=1, columnspan=1)
        
    def create_output_terminal(self):
        self.output_text = customtkinter.CTkTextbox(master=self.root,font=('Courier', 12),border_color="dark")
        self.output_text.grid(row=0, column=2, rowspan=2, columnspan=2, sticky='nsew')
        
    def append_output(self, text):
        self.output_text.insert("end", text)
        
    def clear_output(self):
        self.output_text.delete(1.0, "end")
        
    def run_scrcpy(self):
        self.scrcpy_process = subprocess.Popen(["scrcpy"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        self.scrcpy_process.wait()  # Wait for the process to finish

        return_code = self.scrcpy_process.returncode
        if return_code == 0:
            self.append_output('Closing scrcpy ........\n')
            
        else:
            self.append_output('we encountered issues while trying to launch scrcpy\n')
        self.b8.configure(state="normal")
        self.b9.configure(state="disabled")

    def start_scrcpy(self):
        self.b8.configure(state="disabled")
        self.b9.configure(state="normal")

        scrcpy_thread = threading.Thread(target=self.run_scrcpy)
        scrcpy_thread.start()
        self.append_output('Starting Scrcpy 99%.... \n')

    def stop_scrcpy(self):
        if self.scrcpy_process is not None and self.scrcpy_process.poll() is None:
            self.scrcpy_process.terminate()
            self.scrcpy_process.wait()  # Wait for the process to finish

        self.b8.configure(state="normal")
        self.b9.configure(state="disabled")


if __name__ == "__main__":
    
    controller = ScrcpyController(root)
    root.mainloop()