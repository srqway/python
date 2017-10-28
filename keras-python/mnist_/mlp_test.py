#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from keras.utils import np_utils

import mnist_.utility_.image_utility as image_utility
import mnist_.utility_.mlp_utility as mlp_utility
import mnist_.utility_.mnist_utility as mnist_utility


class mlp_test(unittest.TestCase):
    """
    Multilayer perceptron
    """
    def test_run(self):
        (train_images, train_labels), (test_images, test_labels) = mnist_utility.load_data()
        (normalized_train_images, one_hot_encoding_train_labels) = mlp_utility.preprocess(train_images, train_labels)
        print(one_hot_encoding_train_labels[0])

if __name__ == '__main__':
    unittest.main()


