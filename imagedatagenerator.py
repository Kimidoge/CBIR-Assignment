# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 16:33:57 2021

@author: eilha
"""

from keras.preprocessing.image import ImageDataGenerator, img_to_array,  load_img

datagen = ImageDataGenerator(
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    rescale = 1./255,
    shear_range=0.2,
    zoom_range = 0.2,
    horizontal_flip=True,
    fill_mode='nearest')

img = load_img('datasetall/train/camel/camel-1.gif')
x = img_to_array(img)
x = x.reshape((1,)+ x.shape)

i = 0
for batch in datagen.flow(x, batch_size=1, save_to_dir='preview', save_prefix='camel', save_format='gif'):
    i+=1
    if i>20:
        break