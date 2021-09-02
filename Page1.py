import tkinter as tk
from tkinter import *
from tkinter.font import families
import tkinter.font as font

'''
* Welcome Page
* Page 1 of the GUI
* @Author June Han
'''

class Page1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
		
        #Function to Exit the program
        def ExitApp():
            self.quit()

        def NextPage():
            controller.show_frame("Page2")
            parent.destroy()

        #Create a frame
        frame = LabelFrame(parent, padx=50, pady=50, bg="#FBF6F3")
        frame.pack(padx=10, pady=10)

        #Create a label
        welcomeFont = font.Font(family = 'Kristen ITC', size=50, weight='bold')
        label1 = Label(frame, text = "Welcome", bg="#FBF6F3")
        label1['font'] = welcomeFont
        label1.pack(padx=50, pady=5, anchor=CENTER)

        #Create Start Button
        StartButtonFont = font.Font(family = 'Kristen ITC', size=25, weight='bold')
        StartButton = Button(frame, text="START WASH", padx = 60, pady = 10, fg="white", bg="#72C64B", command=lambda: NextPage())
        StartButton['font'] = StartButtonFont
        StartButton.pack(padx=50, pady=5, anchor=CENTER)

        # Create Exit Button
        ExitButtonFont = font.Font(family = 'Kristen ITC', size=25, weight='bold')
        ExitButton = Button(frame, text="EXIT", padx = 142, pady = 10, fg="white", bg="red",command=lambda: ExitApp())
        ExitButton['font'] = ExitButtonFont
        ExitButton.pack(padx=50, pady=5, anchor=CENTER)
