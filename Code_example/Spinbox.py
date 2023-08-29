import tkinter as tk
from tkinter import ttk

def update_spinbox_values():
    age_spinbox['values'] = ('Power On', 'Power Off')

root = tk.Tk()
root.title("Background Photo Example")

# Load the background image
background_image = tk.PhotoImage(file="images.png")  # Replace with your image file

# Create a label to display the background image
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)  # Cover the entire window

script_frame_label = ttk.Frame(root)
script_frame_label.place(relx=0.5, rely=0.5, anchor="center")

age_spinbox = ttk.Spinbox(script_frame_label, values=('Power On', 'Power Off'))
age_spinbox.set('Power On')
age_spinbox.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

update_button = ttk.Button(root, text="Update Values", command=update_spinbox_values)
update_button.place(relx=0.5, rely=0.9, anchor="center")

root.mainloop()

