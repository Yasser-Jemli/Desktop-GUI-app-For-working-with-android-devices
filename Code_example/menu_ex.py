import tkinter as tk

def menu_command():
    # Command to be executed when a menu item is clicked
    pass

root = tk.Tk()
root.title("My Application")

# Create a style for the menu
menu_style = tk.Menu(root)
root.config(menu=menu_style)

# Create the File menu
file_menu = tk.Menu(menu_style, tearoff=0)
menu_style.add_cascade(label="File", menu=file_menu)

# Add menu items to the File menu
file_menu.add_command(label="Open", command=menu_command)
file_menu.add_command(label="Save", command=menu_command)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Create the Edit menu
edit_menu = tk.Menu(menu_style, tearoff=0)
menu_style.add_cascade(label="Edit", menu=edit_menu)

# Add menu items to the Edit menu
edit_menu.add_command(label="Cut", command=menu_command)
edit_menu.add_command(label="Copy", command=menu_command)
edit_menu.add_command(label="Paste", command=menu_command)

# Add more menus and items as needed

# Start the application loop
root.mainloop()
