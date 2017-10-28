#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

import matplotlib.pyplot as plot


__all__ = ['show_images']
 
def build_current_figure(ncols, nrows):
    width_in_inches = ncols * 3
    height_in_inches = nrows * 3
    current_figure = plot.gcf()
    current_figure.set_size_inches(width_in_inches, height_in_inches) 

def build_image(prediction_labels, labels, images, begin_index, size, nrows, ncols):
    for i in range(0, size):
        current_index = begin_index + i
        subplot = plot.subplot(nrows, ncols, 1 + i)
        title = str(labels[current_index]) + ":" + str(prediction_labels[current_index])
        subplot.set_title(title)
        subplot.imshow(images[current_index], cmap='binary')
        
def show_images(prediction_labels, labels, images, begin_index, size):
    ncols = 10
    nrows = math.ceil(size / ncols)
    build_current_figure(ncols, nrows)
    build_image(prediction_labels, labels, images, begin_index, size, nrows, ncols)
    plot.show()
