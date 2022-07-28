#!/usr/bin/env python
# coding: utf-8

# ## Import Libraries

# In[1]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


import os
os.getcwd()


# In[6]:


os.chdir(r'E:\R1j1s5k1r1n\Udemy\Python\Practice')


# ## Import dataset

# In[7]:


df = pd.read_csv('heart_failure_clinical_records_dataset.csv')
df


# In[8]:


df.head()


# In[10]:


## Checking for missing values


# In[9]:


df.isnull().any() 


# In[11]:


df.columns


# In[12]:


# Renaming certain columns for better readability


# In[13]:


df = df.rename(columns={'creatinine_phosphokinase': 'creatinine',
                        'ejection_fraction': 'ejection',
                        'DEATH_EVENT': 'death'})


# In[14]:


df.shape


# In[16]:


# Checking the data type of each column


# In[17]:


df.dtypes


# In[19]:


## Comparing death(1) and survival(0) rate


# In[22]:


death_rate = df.death.value_counts()/299
death_rate


# Around 68% survived, compared to 32% who died from heart failure

# In[26]:


corr = df.corr()
corr = (corr)
corr


# In[28]:


sns.heatmap(corr)
plt.title('Heatmap of Correlation Matrix')


# Death has a positive correlation with age and serum creatinine; death has a negative correlation with ejection fraction, serum sodium, and time. Weak correlation with other factors.

# ## Anaemia vs Death

# In[31]:


plt.subplots(figsize=(10, 5))
sns.countplot(x="anaemia", hue='death', data=df).set_title('Anaemia Death Distribution')


# ## Age vs Death

# In[32]:


fig = plt.figure(figsize=(15,4),)
ax=sns.kdeplot(df.loc[(df['death'] == 0),'age'] , color='b',shade=True,label='survived')
ax=sns.kdeplot(df.loc[(df['death'] == 1),'age'] , color='r',shade=True, label='died')
plt.title('Age Distribution - Death V.S. Survival')


# Greater rate of survival for patients in the 40-60 age range, as compared to 60-100.

# ## Ejection Fraction vs Death

# In[33]:


fig = plt.figure(figsize=(15,4),)
ax=sns.kdeplot(df.loc[(df['death'] == 0),'ejection'] , color='b',shade=True,label='survived')
ax=sns.kdeplot(df.loc[(df['death'] == 1),'ejection'] , color='r',shade=True, label='died')
plt.title('Ejection Distribution - Death V.S. Survival')


# ## Serum Creatinine vs Death

# In[47]:


fig = plt.figure(figsize=(15,4),)
ax=sns.kdeplot(df.loc[(df['death'] == 0),'serum_creatinine'] , color='b',shade=True,label='survived')
ax=sns.kdeplot(df.loc[(df['death'] == 1),'serum_creatinine'] , color='r',shade=True, label='died')
plt.title('Serum Creatinine Distribution - Death V.S. Survival')


# ## Serum Sodium vs Death

# In[49]:


fig = plt.figure(figsize=(15,4),)
ax=sns.kdeplot(df.loc[(df['death'] == 0),'serum_sodium'] , color='b',shade=True,label='survived')
ax=sns.kdeplot(df.loc[(df['death'] == 1),'serum_sodium'] , color='r',shade=True, label='died')
plt.title('Serum Sodium Distribution - Death V.S. Survival')


# ## Time vs Death

# In[51]:


fig = plt.figure(figsize=(15,4),)
ax=sns.kdeplot(df.loc[(df['death'] == 0),'time'] , color='b',shade=True,label='survived')
ax=sns.kdeplot(df.loc[(df['death'] == 1),'time'] , color='r',shade=True, label='died')
plt.title('Time Distribution - Death V.S. Survival')


# Patients with a shorter follow-up period were more prone to death.

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




