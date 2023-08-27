import customtkinter, tkinter
from tkinter import * 

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.title("By Me")

frame = customtkinter.CTkFrame(master=app,width=350,height=250,bg_color="green",fg_color="red",corner_radius=10)
frame.pack(padx=20,pady=20)

user_id_entry = customtkinter.CTkEntry(master=frame, placeholder_text="USER_ID",width=150,height=30,border_width=2,corner_radius=10)
user_id_entry.place(relx=0.5,rely=0.2, anchor = tkinter.CENTER)

password_entry = customtkinter.CTkEntry(master=frame , placeholder_text="PASSWORD",width=150,height=30,show="*",border_width=2,corner_radius=20)
password_entry.place(relx=0.5,rely=0.4,anchor=tkinter.CENTER)


app.mainloop()