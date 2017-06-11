from Tkinter import *

def donothing():
    print "ok ok I won't..."

root = Tk()

# ***** Main Menu *****

menu = Menu(root)
root.config(menu=menu)

# FILE - Menu
subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New Project...", command=donothing)
subMenu.add_command(label="New", command=donothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=donothing)

# EDIT - Menu
editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=donothing)


# ***** Toolbar *****

toolbar = Frame(root, bg="blue")

insertButt = Button(toolbar, text="Insert Image", command=donothing)
insertButt.pack(side=LEFT, padx=2, pady=2)
printButt = Button(toolbar, text="Print", command=donothing)
printButt.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

root.mainloop()
