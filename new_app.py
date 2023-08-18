
import customtkinter # you should install pip3 install customtkinter
import subprocess
import threading

customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

root = customtkinter.CTk(fg_color="grey")  # create CTk window like you do with the Tk window
root.geometry("1024x592")


class ScrcpyController:
    def __init__(self, root):
        self.root = root
        self.root.title("My Android Controller")

        self.scrcpy_process = None

        self.create_buttons()
        self.create_output_terminal()

    def list_profiles(self):
        list_profiles_thread = threading.Thread(target=self.run_list_profiles)
        list_profiles_thread.start()

    def run_list_profiles(self):
        try:
            self.run_profiles = subprocess.Popen(["adb" , "shell", "pm", "list", "users"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr =self.run_profiles.communicate()
            self.append_output(stdout)
            self.append_output(stderr)
            self.run_profiles.wait() 
        except Exception as e:
            self.append.output(f"Error: {str(e)}\n")

    def list_devices(self):
        list_devices_thread = threading.Thread(target=self.run_list_devices)
        list_devices_thread.start()

    def run_list_devices(self):
        try:
            adb_path="/usr/bin/adb" # check the Path with which adb command 
            self.run_devices = subprocess.Popen([adb_path,"devices"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = self.run_devices.communicate()
            self.append_output(stdout)
            self.append_output(stderr)

            self.run_devices.wait()
        except Exception as e:
            self.append_output(f"Error: {str(e)}\n")

    def volume_plus(self):
        volume_plus_thread = threading.Thread(target=self.run_volume_plus)
        volume_plus_thread.start()

    def run_volume_plus(self):
        try:
            subprocess.Popen(["adb", "shell", "input" , "keyevent", "KEYCODE_VOLUME_UP"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            self.append_output(text=' Volume is increased with one step \n')
          
        except Exception as e:
            self.append_output(f"Error: {str(e)}\n")
            
    def volume_minus(self):
        volume_minus_thread = threading.Thread(target=self.run_volume_minus)
        volume_minus_thread.start()

    def run_volume_minus(self):
        try:
            subprocess.Popen(["adb","shell","input","keyevent","KEYCODE_VOLUME_DOWN"], stdout=subprocess.PIPE, stderr=subprocess.PIPE , text=True)
            self.append_output(text=' Volume is decresed with one step \n')
        except Exception as e:
            self.append_output(f"Error: {str(e)}\n")
        
    def mute_unmute():
        output = execute_command('adb shell .................')
        append_output(output)

    def create_buttons(self):
        self.b8 = customtkinter.CTkButton(master=self.root, text="Start Scrcpy", command=self.start_scrcpy,border_color="dark")
        self.b8.grid(row=3, column=0, rowspan=1, columnspan=1,sticky='nsew')

        self.b9 = customtkinter.CTkButton(master=self.root, text="Stop Scrcpy",fg_color='red', command=self.stop_scrcpy, state="disabled", border_color="dark")
        self.b9.grid(row=4, column=0, rowspan=1, columnspan=1,sticky='nsew')

        self.b7 = customtkinter.CTkButton(master=self.root, text='Clear Terminal Output', command=self.clear_output,border_color="dark")
        self.b7.grid(row=0, column=0, rowspan=1, columnspan=1,sticky='nsew')

        self.b1 = customtkinter.CTkButton(master=self.root, text='adb_devices',command=self.list_devices, border_color="dark")
        self.b1.grid(row=1, column=0, rowspan=1, columnspan=1,sticky='nsew')

        self.b2 = customtkinter.CTkButton(self.root, text='profiles',command=self.list_profiles, border_color="dark")
        self.b2.grid(row=2, column=0, rowspan=1, columnspan=1,sticky='nsew')

        self.b3 = customtkinter.CTkButton(master=self.root, text='VOLUME_UP',command=self.volume_plus, border_color="dark")
        self.b3.grid(row=5, column=0, rowspan=1, columnspan=1,sticky='nsew')

        self.b4 = customtkinter.CTkButton(master=self.root, text='VLUME_DOWN', command=self.volume_minus, border_color="dark")
        self.b4.grid(row=6 , column=0, rowspan=1, columnspan=1 , sticky='nsew')

        # self.b3 = customtkinter.CTkButton(self.root, text='volume_minus',command=volume_minus, border_color="dark")
        # self.b3.grid(row=3, column=1, rowspan=1, columnspan=1,sticky='nsew')


    def create_output_terminal(self):
        self.output_text = customtkinter.CTkTextbox(master=self.root,font=('Courier', 12),border_color="dark")
        self.output_text.grid(row=0, column=2, rowspan=8, columnspan=8, sticky='nsew')

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