from tkinter.ttk import *
from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
import tkinter


def button_select(event, self=None):
    print(0000000)

def button_move_mouse(event, self=None):
    x0 = self.nWindow.winfo_pointerx() - self.nWindow.winfo_rootx() - 40
    y0 = self.nWindow.winfo_pointery() - self.nWindow.winfo_rooty() - 542

    if x0 >= 0 and y0 >= 0:
        sss = 141

        x = int(x0/sss)
        y = int(y0/sss)

        if x < 13 and y < 3:

            self.selectWindow.geometry('+{}+{}'.format(x*sss + self.nWindow.winfo_rootx()+40,
                                                       y*sss + self.nWindow.winfo_rooty()+542))

        else: self.selectWindow.geometry('+{}+{}'.format(4000,4000))
    else: self.selectWindow.geometry('+{}+{}'.format(4000,4000))