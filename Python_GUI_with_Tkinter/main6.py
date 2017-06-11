from Tkinter import *

root = Tk()

def printName(event):
    print "Hello World!"

# button_1 = Button(root, text="Print My Name", command=printName)
button_1 = Button(root, text="Print My Name")
button_1.bind("<Button-1>", printName)
button_1.pack()


root.mainloop()
