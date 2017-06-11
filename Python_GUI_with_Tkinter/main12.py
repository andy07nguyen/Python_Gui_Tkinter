from Tkinter import *
import Tkinter
import tkMessageBox

root = Tk()

tkMessageBox.showinfo("Window Title", "Monkey can live up to 300 years.")

answer = tkMessageBox.askquestion("Question 1", "Do you like silly faces?")

if answer == "yes":
    print " 8==D~ "
    

root.mainloop()
