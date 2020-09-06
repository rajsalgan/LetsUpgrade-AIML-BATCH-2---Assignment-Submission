#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Question 1:Write a program to subtract two complex numbers in Python.
a=2+3j
b=3+4j
c=a+b
print(c)


# In[9]:


#Question 2:Write a program to find the fourth root of a number.
a=81
b=a**(1/4)
print(b)


# In[18]:


# Question 3: Write a program to swap two numbers in Python with the help of a temporary variable.

a=1
b=2
c=b
b=a
a=c
print('new value of a is', a)
print('new value of b is', b)
print(c)


# In[21]:


# Question 4: Write a program to swap two numbers in Python without using a temporary variable.

a=1
b=4
print(a)
print(b)
a=a+b
b=a-b
a=a-b
print(a)
print(b)


# In[26]:


# Question 5: Write a program to convert Fahrenheit to kelvin and celsius both.
Fahrenheit=34
kelvin = (Fahrenheit-32) * 5/9 + 273.15
print(kelvin)


# In[32]:


# Question 6:Write a program to demonstrate all the available data types in Python. 
a=0.00002
print(type(a))


# In[ ]:




