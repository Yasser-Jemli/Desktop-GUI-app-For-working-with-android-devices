
import customtkinter # you should install customtkinter via :  pip3 install customtkinter & tkinter via : sudo apt install python3.8-tk
import subprocess
import threading
from PIL import Image

# customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
# customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
#
root = customtkinter.CTk(fg_color="#4C4646")  # create CTk window like you do with the Tk window
root.geometry("1024x592")


class ScrcpyController:
    def __init__(self, root):
        self.root = root
        self.root.title("My Android Controller")
        self.scrcpy_process = None
        self.create_frames()
        self.create_output_terminal()
        self.create_buttons()


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
            self.run_volume_pluss = subprocess.Popen(["adb", "shell", "input" , "keyevent", "KEYCODE_VOLUME_UP"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = self.run_volume_pluss.communicate()
            self.append_output(text=' Volume Key "+" is pressed \n')
            self.append_output(stdout)
            self.append_output(stderr)
            self.run_volume_pluss.wait()      
        except Exception as e:
            self.append_output(f"Error: {str(e)}\n")
            
    def volume_minus(self):
        volume_minus_thread = threading.Thread(target=self.run_volume_minus)
        volume_minus_thread.start()

    def run_volume_minus(self):
        try:
            self.run_volume_minuss = subprocess.Popen(["adb","shell","input","keyevent","KEYCODE_VOLUME_DOWN"], stdout=subprocess.PIPE, stderr=subprocess.PIPE , text=True)
            stdout, stderr = self.run_volume_minuss.communicate()
            self.append_output(text=' Volume Key "-" is pressed \n')
            self.append_output(stdout)
            self.append_output(stderr)
            self.run_volume_minuss.wait()
        except Exception as e:
            self.append_output(f"Error: {str(e)}\n")
    
    def mute(self):
        mute_thread = threading.Thread(target=self.run_mute)
        mute_thread.start()

    def run_mute(self):
        try:
            self.run_mutee = subprocess.Popen(["adb","shell","input","keyevent","KEYCODE_MUTE"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = self.run_mutee.communicate()
            self.append_output(text='You pressed The mute Button\n')
            self.append_output(stdout)
            self.append_output(stderr)
            self.run_mutee.wait()
        except Exception as e:
            self.append_output(f"Error: {str(e)}\n")

    def create_frames(self):
        # frame for the top zone of the app 
        self.f1 =customtkinter.CTkFrame(master=self.root,fg_color='#36454F',width=2000,height=50)
        self.f1.place(x=0,y=0)
        # frame for the buttons of adb commands 
        self.f2 = customtkinter.CTkFrame(master=self.root,width=150,height=960)
        self.f2.place(x=0,y=51)
        # frame of output terminal 
        self.f3 = customtkinter.CTkFrame(master=self.root,width=500,height=200)
        self.f3.place(x=151,y=51)

    def create_buttons(self):
        
        self.b8 = customtkinter.CTkButton(master=self.f2, text="Start Scrcpy", command=self.start_scrcpy,border_color="dark",width=140,height=50)
        self.b8.place(x=4,y=0)
        # self.b8.grid(row=3, column=0, rowspan=1, columnspan=1,sticky='we')

        self.b9 = customtkinter.CTkButton(master=self.f2, text="Stop Scrcpy",fg_color='red', command=self.stop_scrcpy, state="disabled", border_color="dark",width=140,height=50)
        self.b9.place(x=4,y=52)

        self.b7 = customtkinter.CTkButton(master=self.f2, text='Clear Terminal Output', command=self.clear_output,border_color="dark",width=140,height=50)
        self.b7.place(x=4,y=104)

        self.b1 = customtkinter.CTkButton(master=self.f2, text='adb_devices',command=self.list_devices, border_color="dark",width=140,height=50)
        self.b1.place(x=4,y=156)

        self.b2 = customtkinter.CTkButton(self.f2, text='profiles',command=self.list_profiles, border_color="dark",width=140,height=50)
        self.b2.place(x=4,y=208)

        self.b3 = customtkinter.CTkButton(master=self.f2, text='VOLUME_UP',command=self.volume_plus, border_color="dark",width=140,height=50)
        self.b3.place(x=4,y=260)

        self.b4 = customtkinter.CTkButton(master=self.f2, text='VLUME_DOWN', command=self.volume_minus, border_color="dark",width=140,height=50)
        self.b4.place(x=4,y=312)
        
        self.b5 = customtkinter.CTkButton(master=self.f2, text='Mute', command=self.mute, border_color="dark",width=140,height=50)
        self.b5.place(x=4,y=364)

        self.b3 = customtkinter.CTkButton(self.f2, text='volume_minus',command=self.volume_minus, border_color="dark",width=140,height=50)
        self.b3.place(x=4,y=416)


    def create_output_terminal(self):
        self.output_text = customtkinter.CTkTextbox(master=self.f3,text_color='#E2A76F',font=('arial', 16),fg_color='#757575',width=500,height=200)
        self.output_text.place(x=0,y=0)
        
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