import customtkinter
import tkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("400x240")

textbox = customtkinter.CTkTextbox(app)
textbox.grid(row= 0 , column = 0)
text = """
        welcome to my github 
"""
textbox.insert("0.0",text)
textbox.configure(state="normal")

button = customtkinter.CTkButton(master=app , text="CTkButton")
button.place(relx=0.7, rely=0.3 , anchor = tkinter.CENTER)


app.mainloop()
