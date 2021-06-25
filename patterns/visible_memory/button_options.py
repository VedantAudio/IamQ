from tkinter import *

def button_options_pattern(self=None):
    self.button_options = Button(self.nWindow, text='options')
    self.button_options.place(x=150, y=420, width=50, height=17)
    self.button_options.bind('<Button-1>', lambda e: click_button_options(self=self))

def click_button_options(self=None):
    pass