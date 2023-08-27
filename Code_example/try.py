from tkinter import *
import subprocess
import threading

class ScrcpyController:
    def __init__(self, root):
        self.root = root
        self.root.title("My Android Controller")
        
        self.scrcpy_process = None
        
        self.create_buttons()
        self.create_output_terminal()
        
    def create_buttons(self):
        self.b8 = Button(self.root, text="Start Scrcpy", command=self.start_scrcpy)
        self.b8.grid(row=0, column=0, rowspan=1, columnspan=1)
        
        self.b9 = Button(self.root, text="Stop Scrcpy", command=self.stop_scrcpy, state=DISABLED)
        self.b9.grid(row=1, column=0, rowspan=1, columnspan=1)
        
        self.b7 = Button(self.root, text='Clear Terminal Output', command=self.clear_output)
        self.b7.grid(row=0, column=1, rowspan=1, columnspan=1)
        
        self.b1 = Button(self.root, text='adb_devices')
        self.b1.grid(row=1, column=1, rowspan=1, columnspan=1)
        
        self.b6 = Button(self.root, text='profiles')
        self.b6.grid(row=2, column=1, rowspan=1, columnspan=1)
        
    def create_output_terminal(self):
        self.output_text = Text(self.root, wrap=WORD, font=('Courier', 12))
        self.output_text.grid(row=0, column=2, rowspan=2, columnspan=2, sticky='nsew')
        
    def append_output(self, text):
        self.output_text.insert(END, text)
        
    def clear_output(self):
        self.output_text.delete(1.0, END)
        
    def run_scrcpy(self):
        self.scrcpy_process = subprocess.Popen(["scrcpy"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        self.scrcpy_process.wait()  # Wait for the process to finish

        return_code = self.scrcpy_process.returncode
        if return_code == 0:
            self.append_output('Closing scrcpy ........\n')
            
        else:
            self.append_output('we encountered issues while trying to launch scrcpy\n')
        self.b8.config(state=NORMAL)
        self.b9.config(state=DISABLED)

    def start_scrcpy(self):
        self.b8.config(state=DISABLED)
        self.b9.config(state=NORMAL)

        scrcpy_thread = threading.Thread(target=self.run_scrcpy)
        scrcpy_thread.start()
        self.append_output('Starting Scrcpy 99%.... \n')

    def stop_scrcpy(self):
        if self.scrcpy_process is not None and self.scrcpy_process.poll() is None:
            self.scrcpy_process.terminate()
            self.scrcpy_process.wait()  # Wait for the process to finish

        self.b8.config(state=NORMAL)
        self.b9.config(state=DISABLED)

if __name__ == "__main__":
    root = Tk()
    controller = ScrcpyController(root)
    root.mainloop()
