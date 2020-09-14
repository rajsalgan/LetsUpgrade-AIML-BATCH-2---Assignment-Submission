#!/usr/bin/env python
# coding: utf-8

# In[20]:


for i in range(1,100): 
    for j in range(2,i): 
        if(i % j==0) : 
            break
    else: 
        print(i, end=" ") 


# In[77]:


s="  this is my solution Assignment Day 4 6th September 2020- Rajeev Kumar Singh  "
t=" Solution is delayed due to office work"

#1 - changing all words to upper case 
print(s.upper())

#2 - changing all words to lower case 
print(s.lower())

#3 - extracting sepcific word from a index position 
print(s[1])

#4 - combining two string 
print(s+" "+ t)

#5 - Spliting the  string 
print(s.split(sep=" "), end=" ")


#6 - find a particular value in a string 
print(s.split(sep=" "), end=" ")

#7 - find length of string 
print(len(s))

#8 - replace a particlar value in string 
y=s.replace("t","n")
print(y)

#9 - Slice a String
print(s[1:5:2])


#10 - finding a value in Python 
z=s.find("Rajeev")
print(z)

#11 - finding no of occurances of a letter in a string 
c = 0
for i in s:
        if (i=="r"):
            count=count+1
        print( count, end=" ")
        
#12 - repeating string 
print( s*3)

#13 - removing spaces from string
print( "strip", s.strip())

#14 - removing trailing spaces from string
print( "strip", s.lstrip())

#15 - removing preceding spaces from string
print( "strip", s.rstrip())


# In[86]:


# Question 3: Write a Python program to check if the given string is a Palindrome or Anagram or None of them. Display
# the message accordingly to the user

s="malayalam"
if s== s[::-1]:
    print ( "s is a Palindrome")
else:
        print ( "s is not a Palindrome")


# In[125]:


#Question 4: Write a Python's user-defined function that removes all the additional characters from the string and
# convert it finally to lower case using built-in lower().

def remaddchar(s):
    bad_chars = [';', ':', '!', '*','"',',','!','@','#','$','%','^','&']
    txt = s
    for i in bad_chars :
        txt = txt.replace(i, '') 
    print (txt.lower())

remaddchar("Rajee#v$#.")


# In[ ]:




