#!/usr/bin/env python
# coding: utf-8

# In[1]:


sd = open('File_Handling')


# In[2]:


sd.read()


# In[3]:


sd = open('File_Handling','w')


# In[5]:


sd.read


# In[6]:


sd1=open('File_new','w')


# In[7]:


sd1.write("File Handling in Python")


# In[8]:


sd1.close()


# In[9]:


filename="example_file.txt"


# In[11]:


f=open('example_file.txt','a')
for i in range (0,5):
    name=input("enter a name: ")
    f.write(name)
f.close()


# In[12]:


filename="example1_file.txt"
f1=open('example1_file.txt','a')
for i in range (0,5):
    name=input("enter a name: ")
    f1.write(name+ "\n")
f1.close()


# In[13]:


import re


# In[15]:


if re.search("inform","we need to inform him"):
    print("there is inform")


# In[18]:


allinform = len(re.findall("inform","we need to inform him with the information"))
allinform


# In[21]:


allinform = (re.findall("inform","we need to inform him with the information"))
for i in allinform:
    print(i)


# In[24]:


target_string = "she has 12 balls.she lives in 44a baker street,she is 26.85 years old"
result = re.finditer(r"\d{2}",target_string)
for match_obj in result:
    print(match_obj)
    print(match_obj.group())


# In[25]:


word_list = re.split(r"\s",target_string)
print(word_list)


# In[ ]:




