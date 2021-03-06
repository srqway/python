#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from keras.layers import Dense
from keras.layers import Dropout
from keras.models import Sequential
from keras.utils import np_utils


__all__ = ['preprocess', 'train', 'evaluate', 'prediction']
        
def preprocess(train_images, train_labels):
    (size, width, height) = train_images.shape
    normalized_train_images = train_images.reshape(size, width * height).astype('float32') / 255
    one_hot_encoding_train_labels = np_utils.to_categorical(train_labels)
    return (normalized_train_images, one_hot_encoding_train_labels)

def build_model(input_layer_dimension, hidden_layer_dimensions, output_layer_dimension):
    model = Sequential()
    for (i, hidden_layer_dimension) in enumerate(hidden_layer_dimensions):
        if i == 0:
            model.add(Dense(input_dim=input_layer_dimension, units=hidden_layer_dimension, kernel_initializer='normal', activation='relu'))
        else:
            model.add(Dense(units=hidden_layer_dimension, kernel_initializer='normal', activation='relu'))
        model.add(Dropout(0.5))
    model.add(Dense(units=output_layer_dimension, kernel_initializer='normal', activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    print(model.summary())
    return model

def train(normalized_train_images, one_hot_encoding_train_labels, input_layer_dimension, hidden_layer_dimensions, output_layer_dimension):
    model = build_model(input_layer_dimension, hidden_layer_dimensions, output_layer_dimension)
    train_history = model.fit(x=normalized_train_images, y=one_hot_encoding_train_labels, validation_split=0.2, epochs=10, batch_size=200, verbose=2)
    return (model, train_history)

def evaluate(model, normalized_test_images, one_hot_encoding_test_labels):
    scores = model.evaluate(normalized_test_images, one_hot_encoding_test_labels)
    return scores

def prediction(model, normalized_images):
    prediction = model.predict_classes(normalized_images)
    return prediction
    
    
    
    
    
    
    
