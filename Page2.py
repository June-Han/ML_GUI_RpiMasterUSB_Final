import tkinter as tk
from tkinter import *
from tkinter.font import families
import tkinter.font as font

'''
* Washing Countdown Timing before drying
* Page 2 of the GUI
* @Author June Han
'''
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        #Create a frame
        frame = LabelFrame(parent, padx=50, pady=50, bg="#FBF6F3")
        frame.pack(padx=10, pady=10)

        #Create a function for countdown
        def countdown(seconds):
            hours, remainder = divmod(seconds, 3600)
            mins, secs = divmod(remainder, 60)
            timeformat = "{:02d}:{:02d}:{:02d}".format(hours, mins, secs)
            timeLabel.config(text=timeformat)
            seconds -=1
            #When second is 0, it will be -1.
            if (seconds == -1):
                controller.show_frame("Page3")
                parent.destroy()
            else:
                # call function again after 1000ms (1s)
                frame.after(1000,lambda: countdown(seconds))
        
        def StopWashing():
            controller.show_frame("Page1")
            parent.destroy()

        #Create a label for washing title
        washingFont = font.Font(family = 'Kristen ITC', size=25, weight='bold')
        label1 = Label(frame, text = "Washing...", bg="#FBF6F3")
        label1['font'] = washingFont
        label1.pack(padx=50, pady=5, anchor=W)

        #Countdown Label
        countdownFont = font.Font(family = 'Kristen ITC', size=20, weight='bold')
        timeLabel = Label(frame, text=0, padx = 140, pady = 10, bg="#FBF6F3", relief=SUNKEN)
        timeLabel['font'] = countdownFont
        timeLabel.pack(padx=50, pady=5, anchor=CENTER)
        countdown(5)


        # Create Exit Button
        ExitButtonFont = font.Font(family = 'Kristen ITC', size=25, weight='bold')
        ExitButton = Button(frame, text="STOP", padx = 140, pady = 10, fg="white", bg="red", command= lambda: StopWashing())
        ExitButton['font'] = ExitButtonFont
        ExitButton.pack(padx=50, pady=5, anchor=CENTER)
