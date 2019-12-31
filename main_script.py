#__________import

from tkinter import*


#__________basic_functions_&_launching_code

#_____files_gestion

def open_existant_project():#review
    print("to do")

#_____animations

def dd_animation():
    print("to do")

def ddd_animation():
    print ("to do")

#_____games

def new_file_dd_platform():#review
    print("to do")

def new_file_ddd_fps():
    print("to do")

root = Tk()
root.geometry("700x500")
root.config(bg="grey")

menu_bar = Menu(root)

open_project = Menu(menu_bar, tearoff = 0)
new_project = Menu(menu_bar, tearoff = 0)

open_project.add_command(label="select...", command = open_existant_project)

new_project.add_command(label="2D animation", command = dd_animation)
new_project.add_command(label="3D animation", command = ddd_animation)
new_project.add_separator()
new_project.add_command(label="2D platform game", command = new_file_dd_platform)
new_project.add_separator()
new_project.add_command(label="3D fps game", command = new_file_ddd_fps)

menu_bar.add_cascade(label="open", menu = open_project)
menu_bar.add_cascade(label="new", menu = new_project)

root.config(menu = menu_bar)

root.mainloop()

#__________main_code# tea_engine
# tea_engine
