#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


df=pd.read_csv("Ecommerce Purchases.csv")


# In[5]:


df


# In[6]:


df.head()


# In[7]:


df.info()


# In[8]:


df["Purchase Price"].mean()


# In[9]:


df["Purchase Price"].max()


# In[10]:


df["Purchase Price"].min()


# In[11]:


df[df['Language']=='en'].count()


# In[12]:


df[df['Job']=='Lawyer'].info()


# In[13]:


df['AM or PM'].value_counts()


# In[14]:


df['Job'].value_counts().head(5)


# In[15]:


df[df['Lot']=='90 WT']['Purchase Price']


# In[16]:


df[df["Credit Card"]==4926535242672853]['Email']


# In[17]:


df[(df['CC Provider']=='Amarican Express')&(df['Purchase Price']>95)].count()


# In[ ]:





# In[ ]:





# In[ ]:




