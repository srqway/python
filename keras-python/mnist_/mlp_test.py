#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from keras.utils import np_utils

from mnist_.utility_ import print_utility, mlp_utility, mnist_utility, \
    plot_utility
import numpy as np


np.random.seed(0)

class mlp_test(unittest.TestCase):
    """
    Multilayer perceptron
    """
    def test_run(self):
        (train_images, train_labels), (test_images, test_labels) = mnist_utility.load_data()
        (normalized_train_images, one_hot_encoding_train_labels) = mlp_utility.preprocess(train_images, train_labels)
        input_layer_dimension = 28 * 28
        hidden_layer_dimensions = [256, 256]
        output_layer_dimension = 10
        (model, train_history) = mlp_utility.train(normalized_train_images, one_hot_encoding_train_labels, input_layer_dimension, hidden_layer_dimensions, output_layer_dimension)
        plot_utility.plot_train_history(train_history)
        (normalized_test_images, one_hot_encoding_test_labels) = mlp_utility.preprocess(test_images, test_labels)
        scores = mlp_utility.evaluate(model, normalized_test_images, one_hot_encoding_test_labels)
        normalized_images = normalized_test_images
        prediction_labels = mlp_utility.prediction(model, normalized_images)
        labels = test_labels
        images = test_images
        begin_index = 0
        size = 100
        plot_utility.plot_images(prediction_labels, labels, images, begin_index, size)
        print_utility.print_confusion_matrix(prediction_labels, labels)
        prediction_label = 6
        label = 5
        print_utility.print_error_prediction_table(prediction_labels, labels, prediction_label, label)
    
if __name__ == '__main__':

    unittest.main()


