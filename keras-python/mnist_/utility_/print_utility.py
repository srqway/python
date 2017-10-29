#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd


__all__ = ['print_confusion_matrix', 'print_error_prediction_table']

def print_confusion_matrix(prediction_labels, labels):
    df = pd.crosstab(prediction_labels, labels, rownames=["prediction"], colnames=["actual"])
    print(df)
    
def print_error_prediction_table(prediction_labels, labels, prediction_label, label):
    df = pd.DataFrame({"prediction_label":prediction_labels, "label" :labels})
    print(df[(df.prediction_label == prediction_label) & (df.label == label)])
