import customtkinter
import tkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("400x200")

tabview = customtkinter.CTkTabview(app)
tabview.pack(padx=20,pady=20)

tabview.add("tab1")
tabview.add("tab2")
tabview.add("tab3")

tabview.set("tab2") # set tab as default window when app started 
button1 = customtkinter.CTkButton(tabview.tab("tab1"), text="button 1 ")
button1.pack(padx=20,pady=20)


app.mainloop()