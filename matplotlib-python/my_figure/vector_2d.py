#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from mpl_toolkits.axisartist.axislines import SubplotZero
import matplotlib.pyplot as plt
import numpy as np

def plot(arrows):
    fig = plt.figure("my_figure")
    ax = SubplotZero(fig, 1, 1, 1)
    fig.add_subplot(ax)
    for direction in ["left", "right", "bottom", "top"]:
        # hides borders
        ax.axis[direction].set_visible(False)
    for direction in ["xzero", "yzero"]:
        # adds arrows at the ends of each axis
        ax.axis[direction].set_axisline_style("-|>")
        # adds X and Y-axis from the origin
        ax.axis[direction].set_visible(True)
    xs = [point[0] for arrow in arrows for point in arrow]
    ys = [point[1] for arrow in arrows for point in arrow]
    x_max = max(xs)
    x_min = min(xs)
    x_step = (x_max - x_min) // 7 if (x_max - x_min) // 7 > 0 else 1
    plt.xticks(np.arange(x_min - x_step, x_max + 1 + x_step, x_step))
    y_max = max(ys)
    y_min = min(ys)
    y_step = (y_max - y_min) // 7 if (y_max - y_min) // 7 > 0 else 1
    plt.yticks(np.arange(y_min - y_step, y_max + 1 + y_step, y_step))
    for arrow in arrows:
        ax.arrow(*arrow[0],*(np.array(arrow[1]) - np.array(arrow[0])), length_includes_head = True, head_width = (x_step + y_step) / 8)
    plt.show()

if __name__ == '__main__':
    arrows = (\
          ([-1, 2], [3, 4]),\
          ([0, 0], [4, 2]),\
          ([2, -1], [6, 1]),\
         )
    plot(arrows)
    
    