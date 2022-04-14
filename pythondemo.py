#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd


# In[6]:


pip install pandas


# In[7]:


import pandas as pd


# In[8]:


df = pd.read_csv(r"C:\Users\atrdas\Downloads\cs2m.csv")


# In[9]:


df


# In[12]:


pip install matplotlib


# In[13]:


pip install numpy


# In[14]:


import matplotlib.pyplot as plt


# In[15]:


import numpy as np


# In[16]:


plt.plot('BP',data=df)


# In[17]:


plt.plot('Age',data=df,color="red")


# In[18]:


plt.bar("BP","Age",data=df)


# In[19]:


plt.hist("BP",data=df)


# In[21]:


plt.hist("Chlstrl",data=df,color="Red")
plt.title("Chlstrl Distribution")
plt.legend("Chlstrl")
plt.show()


# In[22]:


plt.bar("BP","Age",data=df,color='yellow')
plt.title("BP according to Age")
plt.legend("bp")
plt.xlabel("BP")
plt.ylabel("Age")
plt.show()


# In[27]:


cars = ['AUDI', 'BMW', 'FORD', 'TESLA', 'JAGUAR', 'MERCEDES']
data = [23, 17, 35, 29, 12, 41]
fig = plt.figure(figsize = (5,5))
plt.pie(data, labels = cars)
plt.show()


# In[30]:


explode = (0.1, 0.0, 0.2, 0.3, 0.0, 0.0)
colors = ("orange", "cyan", "brown", "grey", "indigo", "beige")
wp = { 'linewidth' : 1, 'edgecolor' : "green"}
def func(pct, allvalues):
    absolute = int(pct/100.*np.sum(allvalues))
    return "{:.1f}%\n({:d} g)" .format(pct,absolute)
fig, ax = plt.subplots(figsize = (10,7)) 
wedges,texts,autotexts = ax.pie(data,
                               autopct = lambda pct: func(pct, data),
                               explode = explode,
                               labels = cars,
                               shadow = True,
                               colors = colors,
                               startangle = 90,
                               wedgeprops = wp,
                               textprops = dict(color = "magenta"))
ax.legend(wedges, cars,
         title = "Cars",
         loc ="center left",
         bbox_to_anchor = (1,0,0.5,1))
plt.setp(autotexts, size = 8,weight ="bold")
ax.set_title("Customizing pie chart")
plt.show()


# In[ ]:




