#!/usr/bin/env python
# coding: utf-8
# Author: AYUSH TIWARI

# In[6]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[7]:


data=pd.read_csv('world-happiness-report-2021.csv')


# In[8]:


data


# In[9]:


data.columns


# In[11]:


data1=data[['Country name','Regional indicator','Ladder score','Logged GDP per capita',
         'Social support','Healthy life expectancy','Freedom to make life choices','Generosity','Perceptions of corruption',
         'Ladder score in Dystopia']]


# In[12]:


data1.shape


# In[13]:


data1.isnull().sum()


# In[14]:


plt.figure(figsize=(30,10))
sns.barplot(data=data1,x='Country name',y='Ladder score')
plt.xticks(rotation=90)


# In[15]:


data1.corr()[['Ladder score']].sort_values(by='Ladder score',ascending=False)


# In[16]:


plt.figure(figsize=(30,10))
sns.barplot(data=data1,x='Country name',y='Logged GDP per capita')
plt.xticks(rotation=120)


# In[17]:


data1.corr()[['Logged GDP per capita']].sort_values(by='Logged GDP per capita',ascending=False)


# In[18]:


top_10_happiest=data1.sort_values(by='Ladder score',ascending=False).head(10)
top_15_unhappiest=data1.sort_values(by='Ladder score',ascending=False).tail(15)


# In[19]:


plt.figure(figsize=(20,6))
sns.barplot(data=data1,x=top_10_happiest['Country name'],y=top_10_happiest['Ladder score'])


# In[20]:


plt.figure(figsize=(20,6))
sns.barplot(data=data1,x=top_15_unhappiest['Country name'],y=top_15_unhappiest['Ladder score'])


# In[22]:


plt.figure(figsize=(30,10))
sns.barplot(data=data1,x='Country name',y='Healthy life expectancy')
plt.xticks(rotation=90)


# In[23]:


data1.corr()[['Healthy life expectancy']].sort_values(by='Healthy life expectancy',ascending=False)


# In[ ]:





# In[ ]:




