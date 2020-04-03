#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Classificação de Coronavírus Binário.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/164fuZk7Oe8AUFxoDQL7fEmH2Mmw-HH9z

Código baseado no post de Adrian Yijie Xu disponível em: https://towardsdatascience.com/detecting-covid-19-induced-pneumonia-from-chest-x-rays-with-transfer-learning-an-implementation-311484e6afc1
"""

# código simples que contem o comandos de carregar o modelo a partir de um arquivo. 

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os

os.environ['KMP_DUPLICATE_LIB_OK']='True'

# load model
model = load_model("model.h5")

# summarize model.
model.summary()

print("Model loaded from disk")

print("Testing model...")

test_dir = '/Users/adalbertocajueiro/Downloads/two/test'
img_size = (150, 150)
test_datagen = ImageDataGenerator(rescale=1. / 255)
test_generator = test_datagen.flow_from_directory(
 test_dir,
 target_size=img_size,
 batch_size=1,
 shuffle=False,
 class_mode='binary')

x = model.evaluate_generator(
 test_generator,
 steps = test_generator.n,
 verbose = 1
 )
print('Test loss:', x[0])
print('Test accuracy:',x[1])

from keras.preprocessing import image
import numpy as np

image_path = '/Users/adalbertocajueiro/Downloads/normal-image.jpeg'
print('Loading image ', image_path)

img = image.load_img(image_path, target_size=(150, 150))
x = image.img_to_array(img)/255.0
x = np.expand_dims(x, axis=0)
images = np.vstack([x])
classes = model.predict(images)
print(classes[0])
if classes[0]>0.5:
  print("Normal")
else:
  print("COVID19")

