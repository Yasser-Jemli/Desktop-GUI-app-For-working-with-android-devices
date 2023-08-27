import customtkinter, tkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()

frame = customtkinter.CTkFrame(master=app,width=200,height=200,corner_radius=10)
frame.pack(padx=20 , pady=20)

tk_textbox = tkinter.Text(frame, highlightthickness=0)
tk_textbox.grid(row=0 , column=0 , sticky="nsew")

ctk_textbox_scrollbar = customtkinter.CTkScrollbar(frame,command=tk_textbox.yview)
ctk_textbox_scrollbar.grid(row=0,column=1 , sticky="ns")
def button_event():
    print(tk_textbox.get("0.0","end"))

tk_textbox.configure(yscrollcommand=ctk_textbox_scrollbar.set)
button = customtkinter.CTkButton(master=frame, text="Button" , command=button_event)
button.grid(padx=20,pady=10)

label = customtkinter.CTkLabel(master=frame, text="LABEL",width=120,height=25,fg_color=("white","gray75"),corner_radius=8)
label.grid(padx=20,pady=10)
app.mainloop()
