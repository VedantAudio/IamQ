from tkinter.ttk import *
from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
import tkinter


def button_select(event, self=None):
    x0 = self.nWindow.winfo_pointerx() - self.nWindow.winfo_rootx() - 40
    y0 = self.nWindow.winfo_pointery() - self.nWindow.winfo_rooty() - 550
    if x0 >= 0 and y0 >= 0 and len(self.key_selects) < 13 and len(self.key_etalon) > len(self.key_selects):
        sss = 141

        x = int(x0/sss)
        y = int(y0/sss)

        key_fig_select = x+(2-y)*13
        if key_fig_select < self.options['n_figures']:
            self.key_selects.append(key_fig_select)

            """
                Построение выбранной фигуры
            """
            n_figure = len(self.key_selects) - 1
            for xfill, yfill in zip(self.fillsx[key_fig_select], self.fillsy[key_fig_select]):
                for x, y, c in zip(xfill, yfill, self.colors_kit[key_fig_select]):

                    if self.options['diff_angle'] == 0: ratio_angle = 1
                    else: ratio_angle = np.random.randint(self.options['diff_angle']) + 1

                    theta = np.deg2rad(360 / ratio_angle) #поворот на n градусов
                    xy_mean = (x.mean() + y.mean()) / 2
                    xt = (x - xy_mean) * np.cos(theta) - (y - xy_mean) * np.sin(theta) + xy_mean
                    yt = (x - xy_mean) * np.sin(theta) + (y - xy_mean) * np.cos(theta) + xy_mean
                    self.ax_fin.fill(xt + n_figure*200, yt, color=c, alpha=.5)
                    self.ax_fin.plot(xt + n_figure*200, yt, color='black', linewidth=.1)

            self.canvasAgg_fin.draw()
            self.canvas_fin = self.canvasAgg_fin.get_tk_widget()
            self.canvas_fin.pack(fill=BOTH, expand=1)
            self.frm_fin.pack(fill=BOTH, expand=1)

            if len(self.key_etalon) == len(self.key_selects):
                print()


def button_move_mouse(event, self=None):
    x0 = self.nWindow.winfo_pointerx() - self.nWindow.winfo_rootx() - 40
    y0 = self.nWindow.winfo_pointery() - self.nWindow.winfo_rooty() - 550

    if x0 >= 0 and y0 >= 0:
        sss = 141
        x = int(x0/sss)
        y = int(y0/sss)

        if x < 13 and y < 3:
            self.selectWindow.geometry('+{}+{}'.format(x*sss + self.nWindow.winfo_rootx()+40,
                                                       y*sss + self.nWindow.winfo_rooty()+550))
        else: self.selectWindow.geometry('+{}+{}'.format(4000,4000))
    else: self.selectWindow.geometry('+{}+{}'.format(4000,4000))