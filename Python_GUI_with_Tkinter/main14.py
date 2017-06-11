from Tkinter import *

root = Tk()

photo = PhotoImage(file="img/WahNEDdlGjRZ.gif") # The PhotoImage class can read GIF and PGM/PPM images from files (PYTHON 2.7 ONLY)
label = Label(root, image=photo)
label.pack()

root.mainloop()
