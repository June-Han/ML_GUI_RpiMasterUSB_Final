import tkinter as tk
from tkinter import *
from tkinter.font import families
import tkinter.font as font

'''
* Sterilisation completed
* Page 6 of the GUI
* @Author June Han
'''

class Page6(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        #Create a frame
        frame = LabelFrame(parent, padx=50, pady=50, bg="#FBF6F3")
        frame.pack(padx=10, pady=10)

        def Retrieve():
            controller.show_frame("Page1")
            parent.destroy()

        #Create a label for drying title
        SteriliseFont = font.Font(family = 'Kristen ITC', size=25, weight='bold')
        label1 = Label(frame, text = "Sterilisation Completed", bg="#FBF6F3")
        label1['font'] = SteriliseFont
        label1.pack(padx=50, pady=5, anchor=CENTER)


        # Create Exit Button
        ExitButtonFont = font.Font(family = 'Kristen ITC', size=25, weight='bold')
        ExitButton = Button(frame, text="RETRIEVE", padx = 100, pady = 10, fg="white", bg="#72C64B", command= lambda: Retrieve())
        ExitButton['font'] = ExitButtonFont
        ExitButton.pack(padx=50, pady=5, anchor=CENTER)

