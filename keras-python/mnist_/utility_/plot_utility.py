#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

import matplotlib.pyplot as plt


__all__ = ['plot_train_history', 'plot_train_history', 'plot_images']
 
def build_current_figure(ncols, nrows):
    width_in_inches = ncols * 3
    height_in_inches = nrows * 3
    current_figure = plt.gcf()
    current_figure.set_size_inches(width_in_inches, height_in_inches) 

def build_image(prediction_labels, labels, images, begin_index, size, nrows, ncols):
    for i in range(0, size):
        current_index = begin_index + i
        subplot = plt.subplot(nrows, ncols, 1 + i)
        title = None
        lable = labels[current_index]
        prediction_label = prediction_labels[current_index]
        if lable == prediction_label:
            title = str(lable)
        else:
            title = str(lable) + ":" + str(prediction_label)
        subplot.set_title(title)
        subplot.imshow(images[current_index], cmap='binary')
        
def plot_images(prediction_labels, labels, images, begin_index, size):
    ncols = 10
    nrows = math.ceil(size / ncols)
    build_current_figure(ncols, nrows)
    build_image(prediction_labels, labels, images, begin_index, size, nrows, ncols)
    plt.show()

def plot_sub_train_history(train_history, train_result_type, validation_result_type):
    history = train_history.history
    plt.plot(history[train_result_type])
    plt.plot(history[validation_result_type])
    plt.title('Train History')
    plt.ylabel(train_result_type)
    plt.xlabel('epoch')
    plt.legend(['train', 'validation'], loc='upper left')
    plt.show()

def plot_train_history(train_history):
    train_result_type = 'acc'
    validation_result_type = 'val_acc'
    plot_sub_train_history(train_history, train_result_type, validation_result_type)
    train_result_type = 'loss'
    validation_result_type = 'val_loss'
    plot_sub_train_history(train_history, train_result_type, validation_result_type)

