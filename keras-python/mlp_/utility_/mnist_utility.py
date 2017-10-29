#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from keras.datasets import mnist

__all__ = ['load_data']

def load_data():
    (train_images, train_labels), (test_images, test_labels) = mnist.load_data()
    return (train_images, train_labels), (test_images, test_labels)

