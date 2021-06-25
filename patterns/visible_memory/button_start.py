from tkinter.ttk import *
from tkinter import *
import matplotlib.pyplot as plt
import numpy as np

def button_start(self):
    self.button_start = Button(self.nWindow, text='START')
    self.button_start.place(x=5, y=420, width=50, height=17)
    self.button_start.bind('<Button-1>', lambda e: click_start(self=self))

def button_finish(self):
    self.button_finish = Button(self.nWindow, text='FINISH')
    self.button_finish.place(x=55, y=420, width=50, height=17)
    self.button_finish.bind('<Button-1>', lambda e: click_finish(self=self))

def click_finish(self=None):

    self.key_selects = []

    self.ax_nat.cla()
    self.ax_nat.plot([0, 2600], [0, 200], '.', color='white')
    self.ax_fin.cla()
    self.ax_fin.plot([0, 2600], [0, 200], '.', color='white')
    self.canvasAgg_fin.draw()

    n_figures = []
    while len(n_figures) <= self.options['memory_figs']:
        n_fig = np.random.randint(self.options['n_figures'])
        if n_fig not in n_figures: n_figures.append(n_fig)

    for n_figure, key_figure in enumerate(n_figures):
        for xfill, yfill in zip(self.fillsx[key_figure], self.fillsy[key_figure]):
            for x, y, c in zip(xfill, yfill, self.colors_kit[key_figure]):

                if self.options['diff_angle'] == 0:ratio_angle = 1
                else: ratio_angle = np.random.randint(self.options['diff_angle']) + 1

                theta = np.deg2rad(360 / ratio_angle)  # поворот на n градусов
                xy_mean = (x.mean() + y.mean())/2
                xt = (x - xy_mean) * np.cos(theta) - (y - xy_mean) * np.sin(theta) + xy_mean
                yt = (x - xy_mean) * np.sin(theta) + (y - xy_mean) * np.cos(theta) + xy_mean
                self.ax_nat.fill(xt + n_figure * 200, yt, color=c, alpha=.5)
                self.ax_nat.plot(xt + n_figure * 200, yt, color='black', linewidth=.1)

    self.key_etalon = n_figures

    self.canvasAgg_nat.draw()
    self.canvas_nat = self.canvasAgg_nat.get_tk_widget()
    self.canvas_nat.pack(fill=BOTH, expand=1)
    self.frm_nat.pack(fill=BOTH, expand=1)

def click_start(self=None):
    self.ax_figs.cla()
    self.ax_figs.plot([0, 2600], [0, 600], '.', color='white')

    self.fillsx = {}
    self.fillsy = {}
    self.colors_kit = {}

    """
        вывод фигур для запоминания
    """
    colors = ['lightgreen', 'yellow', 'coral', 'aqua', 'gray', 'violet', 'orange', 'white']
    ratio_detals = 192 / self.options['difficult_detals']

    for figureq in np.arange(self.options['n_figures']):

        self.fillsx[figureq] = []
        self.fillsy[figureq] = []
        self.colors_kit[figureq] = []

        color_kit = []
        while len(color_kit) < self.options['n_colours']:
            col = colors[np.random.randint(len(colors))]
            if col not in color_kit: color_kit.append(col)

        fillsx = []
        fillsy = []
        colors_kit = []

        ny = int(figureq/13)
        nx = figureq-ny*13

        for color in color_kit:
            for n in np.arange(np.random.randint(self.options['rand_fig'])+1):

                size_fig = np.random.randint(self.options['difficult_fig_max']) + 2
                if size_fig < self.options['difficult_fig_min']: size_fig = self.options['difficult_fig_min']

                x = np.random.randint(self.options['difficult_detals'], size=size_fig)*ratio_detals
                y = np.random.randint(self.options['difficult_detals'], size=size_fig)*ratio_detals

                fillsx.append(x)
                fillsy.append(y)
                colors_kit.append(color)

                if self.options['diff_angle'] == 0: ratio_angle = 1
                else: ratio_angle = np.random.randint(self.options['diff_angle']) + 1

                theta = np.deg2rad(360 / ratio_angle)  # поворот на n градусов
                xy_mean = (x.mean() + y.mean())/2
                xt = (x - xy_mean) * np.cos(theta) - (y - xy_mean) * np.sin(theta) + xy_mean
                yt = (x - xy_mean) * np.sin(theta) + (y - xy_mean) * np.cos(theta) + xy_mean
                self.ax_figs.fill(xt + nx * 200, yt + ny * 200, color=color, alpha=.5)
                self.ax_figs.plot(xt + nx * 200, yt + ny * 200, color='black', linewidth=.1)


        self.canvasAgg_figs.draw()
        self.canvas_figs = self.canvasAgg_figs.get_tk_widget()
        self.canvas_figs.pack(fill=BOTH, expand=1)
        self.frm_figs.pack(fill=BOTH, expand=1)

        self.fillsx[figureq].append(fillsx)
        self.fillsy[figureq].append(fillsy)
        self.colors_kit[figureq] = colors_kit

