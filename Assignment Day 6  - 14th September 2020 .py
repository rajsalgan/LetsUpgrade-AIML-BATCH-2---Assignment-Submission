#!/usr/bin/env python
# coding: utf-8

# In[16]:


# Question 1 :
# Assuming that we have some email addresses in the "username@companyname.com" format, please
# write a program to print the company name of a given email address. Both user names and company names are composed of letters only.

val = input("Enter your value: ")
print(val) 
y=val.find("@")
z=val.find(".",y)
company=val[(y+1):z]
print(y)
print(z)
print(company.upper())


# In[8]:


# Question 2 :Write a program that accepts a comma-separated sequence of words as input and prints the words in a
# comma-separated sequence after sorting them alphabetically.

val = input("Enter your value: ")
print(val) 
x= val.split(",")
x.sort()
for i in x:
   print(i)
print(x)

Set is a collection of unique items , the items in set are immutable .
Set is represented by {}
A Set will always have unique value
# In[9]:


# Creating a set 
x= {1,"hello", 3.12,(1,2,"raj")}
print(x)
type(x)


# In[10]:


# adding items to set
x.add(3)
print(x)


# In[11]:


# removing items
x.remove(3.12)
print(x)


# In[12]:


# Discarding items
x.discard(3.12)
print(x)


# In[13]:


# Discarding items
x.pop()
print(x)


# In[18]:


# Ckearing a set 
x.clear()
print(x)


# In[20]:


x={1,2,3,4}
y={3,4,5,6,7,8}

# Union of set
x.union(y)


# In[21]:


y.union(x)


# In[22]:


# Intersection
x.intersection(y)


# In[23]:


#p(X)
x.difference(y)


# In[24]:


#p(y)
y.difference(x)


# In[25]:


# P(x) + p(y)- P(xintersenction y)
x.symmetric_difference(y)


# In[30]:


# find in set
print("a" in x)
print(1 in x)


# In[39]:


# looping in set
for i in x:
    print(i, end=" ")


# In[62]:


#Question 4: Write a Python's user-defined function that removes all the additional characters from the string and
 # convert it finally to lower case using built-in lower().



def con(val):
    print(val)
    y= [';','!','@','#','$','%','^','&','*','(',')','-','_','+','=','"',':','/','?','<','>','/','|','`','~','`']
    for i in y:
        val = val.replace(i," ")
        z=val
        z=z.replace(" ","")
        k=z.lower()
        print(k)

con(val = input("Enter your value: "))    

