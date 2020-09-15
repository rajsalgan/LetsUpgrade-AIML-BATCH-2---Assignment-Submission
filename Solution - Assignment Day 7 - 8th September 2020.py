#!/usr/bin/env python
# coding: utf-8

# In[35]:


# Question 1:Write a program to copy the contents of one file to another using a for loop. 

import os
with open( r'C:\Users\rajeevs588\00.Work\AIML-master\AI-ML-Aug-2020\Day-7\SampleData.txt', 'r') as f:
#    print(f.readlines())
    with open(r'C:\Users\rajeevs588\00.Work\AIML-master\AI-ML-Aug-2020\Day-7\copy.txt',"w") as f1:
        for line in f:
            f1.write(line)
with open( r'C:\Users\rajeevs588\00.Work\AIML-master\AI-ML-Aug-2020\Day-7\copy.txt', 'r') as f2:
    print(f2.readlines())


# In[26]:


# Question 2: Write a Python program to find maximum and minimum values in the dictionary. Do not use built-in min
# and max functions.

d={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_d = dict(sorted(d.items(), reverse=False))
sorted_a = dict(sorted(d.items(), reverse=True))
print(sorted_d)
print(sorted_a)
print(sorted_d[0])
print(sorted_a[4])


# In[ ]:




