# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 14:23:41 2021

@author: eilha
"""

import numpy as np
from PIL import Image
from feature_extractor import FeatureExtractor
from datetime import datetime
from flask import render_template, Flask, request
from pathlib import Path

app = Flask(__name__)

# Read img features
fe = FeatureExtractor()
features = []
img_path = []
for feature_path in Path("./static/feature").glob("*.npy"):
    features.append(np.load(feature_path))
    img_path.append(Path("./static/img") / (feature_path.stem + ".gif"))
    
features = np.array(features)
    

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["query_img"]
        
        # Saving the queried image
        img = Image.open(file.stream)
        uploaded_img_path = "static/uploaded/" +  datetime.now().isoformat().replace(":",".") + "_" + file.filename
        
        img.save(uploaded_img_path)
        
        
        
        ## Image retrieval / Search
        query = fe.extract(img)
        
       
        
        dists = np.linalg.norm(features - query, axis = 1)  #count distance between features and query image
        ids   = np.argsort(dists)[:20]
        scores= [(dists[id], img_path[id]) for id in ids]

        print(scores)
        
        
        ###########NEW SHIT########################################################
        
        #print("query image hehehehehehhe: ", file.filename)
         
        queryName = file.filename.__str__()
        
        print("queryName : ", queryName)
        
        for id in ids:
            
            retrievedName = img_path[id].__str__()
            
            print("Retrieved: ", retrievedName)
            
            if retrievedName.find(queryName) != -1:
                print("Similar!")
                
            else:
                print("Not similar")
            
            
        
        print("ini score hehe", scores)
        
         
        
        
        return render_template("index.html", query_path = uploaded_img_path, scores = scores)
        
    else:
        return render_template("index.html")
        


if __name__ == "__main__":
    app.run()