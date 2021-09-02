from tflite_runtime.interpreter import Interpreter 
import numpy as np
import time
from tkinter import ttk
import tkinter as tk
from tkinter import *
from tkinter.font import families
import tkinter.font as font
from PIL import ImageTk, Image
from Page1 import Page1
from Page2 import Page2
from Page3 import Page3
from Page4 import Page4
from Page5 import Page5
from Page6 import Page6

class SyringeApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Syringe Washer UI")
        #self.iconbitmap("./syringe.ico")

        self.title_font = font.Font(family='Kristen ITC', weight="bold")

        #The container is a window where we'll change the frames
        self.container = tk.Frame(self)
        self.geometry("650x500")
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        #Create a canvas for the main frame
        self.canvas = Canvas(self.container)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=1)

        #Position in frame but attached to the canvas
        vertical_scrollbar = ttk.Scrollbar(self.container, orient = VERTICAL, command = self.canvas.yview)
        vertical_scrollbar.pack(side=RIGHT, fill=Y)

        #Configure the canvas
        self.canvas.configure(yscrollcommand=vertical_scrollbar.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion = self.canvas.bbox("all")))
        
        self.frames = {}
        #Create a mapping from string Page_Name: Page
        for F in (Page1, Page2, Page3, Page4, Page5, Page6):
            page_name = F.__name__
            self.frames[page_name] = F
        
        self.show_frame("Page1")

    def show_frame(self, page_name):
        # create the new frame to put labelframes in
        second_frame =  Frame(self.canvas, width="700", height="500")
        second_frame.grid(row=0, column=0, sticky="nsew")
        second_frame.pack(side="top", fill="both", expand=True)
        second_frame.grid_rowconfigure(0, weight=1)
        second_frame.grid_columnconfigure(0, weight=1)
        self.canvas.create_window((0,0), window = second_frame, anchor="nw")
        requested_frame = self.frames[page_name]
        requested_frame(second_frame, controller=self)

        


if __name__ == "__main__":
    app = SyringeApp()
    app.mainloop()