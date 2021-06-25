import tkinter
import matplotlib

from patterns.visible_memory.button_options import button_options_pattern
from patterns.visible_memory.button_start import button_start, button_finish
from patterns.visible_memory.buttons_select import button_move_mouse, button_select
from patterns.visible_memory.pattern_options import set_default_options

matplotlib.use("TkAgg")

import matplotlib.pyplot as plt
import matplotlib.lines as mlines

from tkinter import ttk
from tkinter.ttk import *
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Main:

    def __init__(self):
        self.nWindow = tkinter.Tk()
        self.nWindow.title("I AM Q")
        self.nWindow.geometry('1900x1100+10+0')

        self.selectWindow = tkinter.Tk()
        self.selectWindow.overrideredirect(1)
        self.selectWindow.geometry('141x141+4000+0')
        self.selectWindow.attributes("-topmost", True)
        self.selectWindow.configure(background='black')
        self.selectWindow.wm_attributes('-alpha', 0.3)

        self.selectWindow.bind('<Button-1>', lambda e: button_select(e, self=self))

        """
            Поле для запоминания
        """
        self.start_memory_field = Notebook(self.nWindow, width=2600, height=200)
        self.start_memory_field.pack(expand=1, fill='both')
        self.start_memory_field.place(x=-370, y=0)

        self.frm_nat = Frame(self.start_memory_field)
        self.fig_nat = plt.figure(facecolor='white', figsize=(26, 2))
        self.ax_nat = self.fig_nat.add_subplot(111)
        self.canvasAgg_nat = FigureCanvasTkAgg(self.fig_nat, master=self.frm_nat)
        self.canvas_nat = self.canvasAgg_nat.get_tk_widget()
        self.xax_nat = self.ax_nat.xaxis
        self.ax_nat.get_xaxis().set_visible(False)
        self.ax_nat.get_yaxis().set_visible(False)
        self.ax_nat.cla()
        self.ax_nat.plot([0, 2600], [0, 200], '.', color='white')
        self.canvasAgg_nat.draw()

        """
            Поле для вспоминания
        """
        self.finish_memory_field = Notebook(self.nWindow, width=2600, height=200)
        self.finish_memory_field.pack(expand=1, fill='both')
        self.finish_memory_field.place(x=-370, y=200)

        self.frm_fin = Frame(self.finish_memory_field)
        self.fig_fin = plt.figure(facecolor='white', figsize=(26, 2))
        self.ax_fin = self.fig_fin.add_subplot(111)
        self.canvasAgg_fin = FigureCanvasTkAgg(self.fig_fin, master=self.frm_fin)
        self.canvas_fin = self.canvasAgg_fin.get_tk_widget()
        self.xax_fin = self.ax_fin.xaxis
        self.ax_fin.get_xaxis().set_visible(False)
        self.ax_fin.get_yaxis().set_visible(False)
        self.ax_fin.cla()
        self.ax_fin.plot([0, 2600], [0, 200], '.', color='white')
        self.canvasAgg_fin.draw()

        """
            Поле для выведения всех символов
        """
        self.figures_memory_field = Notebook(self.nWindow, width=2600, height=600)
        self.figures_memory_field.pack(expand=1, fill='both')
        self.figures_memory_field.place(x=-370, y=450)

        self.frm_figs = Frame(self.figures_memory_field)
        self.fig_figs = plt.figure(facecolor='white', figsize=(26, 6))
        self.ax_figs = self.fig_figs.add_subplot(111)
        self.canvasAgg_figs = FigureCanvasTkAgg(self.fig_figs, master=self.frm_figs)
        self.canvas_figs = self.canvasAgg_figs.get_tk_widget()
        self.xax_figs = self.ax_figs.xaxis
        self.ax_figs.get_xaxis().set_visible(False)
        self.ax_figs.get_yaxis().set_visible(False)
        self.ax_figs.cla()
        self.ax_figs.plot([0, 2600], [0, 600], '.', color='white')
        self.canvasAgg_figs.draw()

        self.canvas_figs.bind('<Motion>', lambda e: button_move_mouse(e, self=self))

        set_default_options(self=self)

        """
            Кнопки управления
        """
        button_start(self)
        button_finish(self)
        button_options_pattern(self)

        self.nWindow.mainloop()

Main()