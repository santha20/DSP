#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
df=pd.read_csv("salaries.csv")
df


# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df.info()


# In[6]:


df["BasePay"].mean()


# In[7]:


df["OvertimePay"].max()


# In[8]:


df[df["EmployeeName"]=='JOSEPH DRISCOLL']


# In[9]:


df[df['EmployeeName']=='JOSEPH DRISCOLL']['TotalPayBenefits']


# In[10]:


df['TotalPayBenefits'].max()


# In[11]:


df[df['TotalPayBenefits']==df['TotalPayBenefits'].max()]


# In[12]:


df.loc[df['TotalPayBenefits'].idxmax()]


# In[13]:


df[df['TotalPayBenefits']==df['TotalPayBenefits'].min()]


# In[14]:


df.loc[df['TotalPayBenefits'].idxmin()]['EmployeeName']


# In[15]:


df.loc[df['TotalPayBenefits'].idxmin()]


# In[16]:


df.groupby('Year').mean()['BasePay']


# In[17]:


df['JobTitle'].value_counts().head(5)


# In[18]:


df[df['Year']==2013]['JobTitle'].value_counts()


# In[19]:


sum(df[df['Year']==2013]['JobTitle'].value_counts()==1)


# In[20]:


df['title_len']=df['JobTitle'].apply(len)


# In[21]:


df[['JobTitle','title_len']].head()


# In[ ]:


df[['title_len','TotalPayBenefits']].corr()

