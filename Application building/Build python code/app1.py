#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import numpy as np
import pandas as pd
import tensorflow as tf
from flask import Flask, request, render_template, redirect, url_for
import os
from werkzeug.utils import secure_filename
from tensorflow.python.keras.backend import set_session


# In[2]:


app = Flask(__name__)
veg_model=load_model(r"C:\Users\vijay\OneDrive\Desktop\ibm\models\vegetables.h5")
fruit_model=load_model(r"C:\Users\vijay\OneDrive\Desktop\ibm\models\fruit.h5")


# In[3]:


# home page
@app.route('/')
def home1():
    return render_template(r'C:\Users\vijay\OneDrive\Desktop\ibm\Application building\HTML pages\home.html')


# In[4]:


# about page
@app.route('/aboutus')
def about1():
    return render_template(r'C:\Users\vijay\OneDrive\Desktop\ibm\Application building\HTML pages\about.html')


# In[5]:


# prediction page
@app.route('/prediction')
def prediction1():
    return render_template(r'C:\Users\vijay\OneDrive\Desktop\ibm\Application building\HTML pages\predict.html')


# In[6]:



@app.route('/predict',methods=['POST'])
def predict2():
    if request.method == 'POST': 
        f= request.files['image']
        basepath = os.path.dirname(_file_)
        file_path = os.path.join(basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)
        img = image.load_img(filepath, target_size=(128, 128))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        plant = request.form['plant']
        print(plant)
        if(plant == "vegetables"):
            predictions = veg_model.predict_classes(x)
            print(predictions)
            df=pd.read_excel('precautions - veg.xlsx')
            print(df.iloc[predictions[0]]['caution'])
        else:
            predictions = fruit_model.predict_classes(x)
            df=pd.read_excel('precautions - fruits.xlsx')
            print(df.iloc[predictions[0]]['caution'])
        return df.iloc[predictions[0]]['caution']


# In[7]:


get_ipython().system('pip install Flask-Waitress')


# In[ ]:


if __name__ == "__main__":
    app.run(debug=False)


# In[ ]:




