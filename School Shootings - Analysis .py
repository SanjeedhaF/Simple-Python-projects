#!/usr/bin/env python
# coding: utf-8

# In[29]:


#Animation in a dataset using plotly

#Dataset taken from Kaggle - School shootings

# Analysis of the school shootings trends over the past year

import pandas as pd
import numpy as np


#load the file

df=pd.read_csv('Shooting dataset.csv')
df


# In[30]:


#DATA CLEANING

# drop empty rows

df.dropna(axis=0,inplace=True)
df


# In[31]:


data=df.head(50)
data


# In[49]:


#!pip install plotly


get_ipython().system('pip install plotly --upgrade')
import plotly.express as px


# In[50]:


data_sorted = data.sort_values('victims', ascending=False)
data_sorted


# In[57]:


fig = px.bar(data_sorted, 
             x ="school", 
             y ="victims",
             color ='city',
             animation_frame ='year',
             hover_name ='state', 
             range_y =[0, 10])
           


fig.show()


# In[ ]:





# In[ ]:


# Conclusion

In 2012, Sandy hook elementery school had a great tragedy of losing 28 children which is very heartbreaking till now.


