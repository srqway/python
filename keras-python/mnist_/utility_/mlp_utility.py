#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from keras.utils import np_utils


__all__ = ['preprocess']
        
def preprocess(train_images, train_labels):
    (size, width, height) = train_images.shape
    normalized_train_images = train_images.reshape(size, width * height).astype('float32') / 255
    one_hot_encoding_train_labels = np_utils.to_categorical(train_labels)
    return (normalized_train_images, one_hot_encoding_train_labels)
