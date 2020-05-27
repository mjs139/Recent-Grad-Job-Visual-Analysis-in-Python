#!/usr/bin/env python
# coding: utf-8

# # Data Visualization in Python
# 
# For this project, I will be using Python to visualize FiveThirtyEight [data](https://github.com/fivethirtyeight/data/tree/master/college-majors) regarding the job outcomes of students who graduated from college between 2010 and 2012. 

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[3]:


recent_grads = pd.read_csv('recent-grads.csv')
recent_grads.iloc[0]


# In[6]:


recent_grads.head()


# In[7]:


recent_grads.tail()


# In[8]:


recent_grads.describe()


# I will now drop rows with missing data

# In[4]:


raw_data_count = recent_grads.shape[0]
raw_data_count


# In[5]:


recent_grads = recent_grads.dropna()
cleaned_data_count = recent_grads.shape[0]
cleaned_data_count


# Only one row with missing data was dropped. In this data set, we have 172 rows. 

# ### Plots
# 
# I will now produce numerous scatter plots of the data

# In[15]:


recent_grads.plot(x='Sample_size', y='Median', 
                  kind='scatter', 
                  title='Median vs. Sample_size')


# It does not seem like students in more popular majors make more money. 

# In[16]:


recent_grads.plot(x='Sample_size', 
                  y='Unemployment_rate', 
                  kind='scatter',
                 title='Unemployment_rate vs. Sample_size')


# In[21]:


recent_grads.plot(x='Full_time', y='Median', 
                  kind='scatter',
                 title='Median vs. Full_time')


# In[22]:


recent_grads.plot(x='ShareWomen', y='Unemployment_rate', 
                  kind='scatter',
                 title='Unemployment Rate vs. ShareWomen')


# In[23]:


recent_grads.plot(x='Men', y='Median', kind='scatter',
                 title='Median vs. Men')


# In[25]:


recent_grads.plot(x='Women', y='Median', kind='scatter',
                 title='Median vs. Women')


# It seems like students majored in subjects that were majority female made less money

# ### Histograms
# 
# I will now make histograms of the data using Pandas. 

# In[15]:


fig, ax = plt.subplots()
ax.hist(recent_grads['Sample_size'], bins = 10)
ax.set_title("Sample Size")
ax.set_xlabel("Sample Size")
ax.set_ylabel("Counts")
plt.show()


# In[16]:


fig, ax = plt.subplots()
ax.hist(recent_grads['Median'], bins = 10)
ax.set_title("Median")
ax.set_xlabel("Median")
ax.set_ylabel("Counts")
plt.show()


# The most common median salary range is between $30000-50000. 

# In[17]:


fig, ax = plt.subplots()
ax.hist(recent_grads['Employed'], bins = 10)
ax.set_title("Employed")
ax.set_xlabel("Employed")
ax.set_ylabel("Counts")
plt.show()


# In[46]:


cols = ["Full_time", "ShareWomen", "Unemployment_rate", "Men", "Women"]

fig = plt.figure(figsize=(5,30))

for i in range(0,len(cols)):
    ax = fig.add_subplot(5, 1, i+1)
    ax.hist(recent_grads[cols[i]], bins=10)
    ax.set_xlabel(cols[i])
    ax.set_ylabel("Counts")
    if cols[i] == "Men":
        plt.xticks(rotation=45)
    #plt.show()


# ### Scatterplot Matrix
# 
# I will now use a scatterplot matrix to view the data

# In[48]:


from pandas.plotting import scatter_matrix


# In[50]:


scatter_matrix(recent_grads[['Sample_size', 'Median']], figsize=(8,8))


# In[52]:


scatter_matrix(recent_grads[['Sample_size', 'Median', 'Unemployment_rate']], figsize=(9,9))


# ### Bar Plots
# 
# I will now create bar plots to visualize the data
# 
# First, I will create a bar plot for the first ten and last ten rows or the "ShareWomen" column. 

# In[54]:


recent_grads[:10].plot.bar(x='Major', y='ShareWomen', legend=False)
recent_grads[163:].plot.bar(x='Major', y='ShareWomen', legend=False)


# Now, I will do the same thing for unemployment

# In[55]:



recent_grads[:10].plot.bar(x='Major', y='Unemployment_rate', legend=False)
recent_grads[163:].plot.bar(x='Major', y='Unemployment_rate', legend=False)

