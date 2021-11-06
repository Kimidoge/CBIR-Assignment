# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 13:57:23 2021

@author: eilha

offline.py is to read images and extract the features
"""

from PIL import Image
from pathlib import Path
import numpy as np

from feature_extractor import FeatureExtractor

if __name__ == "__main__":
    fe = FeatureExtractor()
    
    
    for img_path in sorted(Path("./static/img").glob("*.gif")):
        print(img_path)
        
        ## Extract the features (Feature Extractor)
        feature = fe.extract(img  = Image.open(img_path))
        print(type(feature), feature.shape)
        
        
        feature_path = Path("./static/feature") / (img_path.stem + ".npy")
        print(feature_path)
        
        ## Saving Features
        np.save(feature_path, feature)