# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 14:05:17 2021

@author: eilha
"""

from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.models import Model
import numpy as np


class FeatureExtractor:
    def __init__(self):
        base_model = VGG16(weights = "imagenet")
        self.model = Model(inputs = base_model.inputs , 
                           outputs = base_model.get_layer("fc1").output)
        
        
      
    def extract(self, img):
        img = img.resize((224, 224)).convert("RGB")
        x = image.img_to_array(img)  ##converting to np.array
        x = np.expand_dims(x, axis = 0)
        x = preprocess_input(x)
        feature = self.model.predict(x)[0]  #(1, 4096)
        
        print(feature)
        
        return feature / np.linalg.norm(feature)
    
        
