import customtkinter as ctk
from PIL import Image
from os import walk 

class AnimatedButton(ctk.CTkButton):
    def __init__(self, parent, light_path, dark_path):
        self.import_folders(light_path,dark_path)

        super().__init__(master = parent, text = 'A animated button')
        self.pack(expand = True)

    def import_folders(self, light_path, dark_path):
        for path in (light_path, dark_path):
            for _, __, image_data in walk(path):
                print(image_data[1].split('.')[0][-5:])
                sorted_data = sorted(image_data, 
                                     key = lambda item: int(item.split('.')[0][-5:]))
                
                full_path_data = [path +'/' + item for item in sorted_data]
                print(full_path_data)

       

window = ctk.CTk()
window.title('Animations')
window.geometry('300x200')

AnimatedButton(window, 'black' , 'yellow')

window.mainloop()