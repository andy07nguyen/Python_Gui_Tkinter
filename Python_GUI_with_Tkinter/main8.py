from Tkinter import *

class AndysButtons:
    def __init__(self, master): # PASSING IN ROOT AS MASTER
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text="Print Message", command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Quit", command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print "Wow, this actually worked!"

root = Tk()
a = AndysButtons(root)
root.mainloop()
