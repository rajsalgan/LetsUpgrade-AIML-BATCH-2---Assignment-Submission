#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Question 1 : Research on whether addition, subtraction, multiplication, division, floor division, and modulo operations 
# be performed on complex numbers. Based on your study, implement a Python program to demonstrate
# these operations.


a=3+4j
b=5+6j
c=a+b
print(c)
d=a-b
print(d)
e=a*b
print(e)
f=a/b
print(f)
 # Floor division (a//b), and modulo operations(a%b) cannot be performed on complex numbers



# # Question 2 : Research on range() functions and its parameters. Create a markdown cell and write in your own words (no copy-paste from google please) what you understand about it. Implement a small program of your choice on the same.
# 
# ##  Range is a function which creates a sequence of numbers; the functions has three parameters
# 
#     ### Range( Start, stop, steps) 
#         #### start is the number from which the number squence starts and this is included in the series.
#          #### stop is the number from which the number squence ends and it is not included in the series.
#           #### step is the increment by which the number diffrs frok its preceding number
#              

# In[20]:


x=range(0,-10,-2)
for i in x:
    print(i,end=" ")


# In[25]:


# Question 3: Consider two numbers. Perform their subtraction and if the result of subtraction is greater than 25, print
# their multiplication result else print their division result.

a=50
b=5
c=a-b
if c>25:
    d=a*b
else:
    d=a/b
print(c)
print(d)


# In[64]:


# Question 4: Consider a list of 10 elements of integer values. If the number in the list is divisible by 2, print the result as
# "square of that number minus 2".

a=[1,2,3,4,5,6,7,8,9,10]
for i in a:
    if i%2==0:
        d=(i*i)-2
        print(' the Number is', i,'and the square of that number minus 2   ' ,d)
    


# In[66]:


# Question 5: Consider a list of 10 elements. Print all the elements in the list which are greater than 7 when that number 
# is divided 2.

a=[1,2,3,4,5,6,7,8,9,10]
for k in a:
    if i%2==0:
        for i in a:
            if i>=7:
                print(i)       


# In[ ]:




