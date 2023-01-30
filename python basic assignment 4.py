#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1. What exactly is []?
1 ANS) The empty sqaure brackets [] represent a list.Just like how ' ' represents strings. 
        eg. l=['prasant',21,9*2,[rohit,45]]
    


# In[ ]:


2. In a list of values stored in a variable called spam, how would you assign the value 'hello' as the 
third value? (Assume [2, 4, 6, 8, 10] are in spam.)


# In[2]:


#2 ans)
spam = [2, 4, 6, 8, 10]
print(spam)
spam[2] = 'hello'
print(spam)


# In[ ]:


3. What is the value of spam[int(int('3' * 2) / 11)]?  (Lets pretend the spam includes the list ['a','b', 'c', 'd'] for the next three queries.)


# In[ ]:


#3 ans)

3'**2 will give '33'
int('33') will be 33
33/11 will be 3.0
int(3.0) will give 3
spam[3] will be value at index 3 that is 'd'


# In[8]:


#3 ans) example 
spam = ['a', 'b', 'c', 'd']


# In[9]:


spam[int(int('3'*2)/11)]


# In[ ]:


4. What is the value of spam[-1]? 

4 ans)spam[-1] = last value of list  'd'


# In[10]:


#4 ans)
spam[-1]


# In[ ]:


5. What is the value of spam[:2]?
5 ans)spam[:2] = 'a' and 'b'


# In[11]:


#5 ans
spam[:2]


# In[ ]:


#Let&#39;s pretend bacon has the list [3.14, 'cat', '11, 'cat', True] for the next three questions.


# In[ ]:


6. What is the value of bacon.index('cat')?
6 ans)index of first occurence of 'cat' value is 1 


# In[12]:


#6 ans 
bacon=[3.14,'cat','11','cat',True]


# In[13]:


bacon.index('cat')


# In[ ]:


get_ipython().set_next_input('7. How does bacon.append(99) change the look of the list value in bacon');get_ipython().run_line_magic('pinfo', 'bacon')
7 ans)It will append or add the value  99 at the end of list bacon


# In[28]:


#7 ans 
bacon.append(99)


# In[29]:


bacon


# In[ ]:


get_ipython().set_next_input("8. How does bacon.remove ('cat') change the look of the list in bacon");get_ipython().run_line_magic('pinfo', 'bacon')
8 ans)This will remove the first occured string named 'cat' from the list bacon 


# In[31]:


#8 ans
bacon.remove('cat')


# In[32]:


bacon


# In[ ]:


get_ipython().set_next_input('9. What are the list concatenation and list replication operators');get_ipython().run_line_magic('pinfo', 'operators')
9 ans)List concatenation operator is ‘+’ while list replication operator is ‘*’


# In[ ]:


10. What is difference between the list methods append() and insert()?
10 ans)Append method appends/includes/add the given object to the end of the list always.
       Insert method accepts two arguments, index at which the element needs to be inserted and the object to insert.


# In[ ]:


get_ipython().set_next_input('11. What are the two methods for removing items from a list');get_ipython().run_line_magic('pinfo', 'list')
11 ans)Two methods used for removing items from a list :

List.remove(object)  : Removes the first occurrence of the given object from the list
List.pop(index = -1) : Removes and returns item at the index (default is -1, the last element)


# In[ ]:


12. Describe how list values and string values are identical.
12 ans) list is a collection of values in Python, string is a collection of characters. Both list and strings are iterable in Python and for loop can be used around a list or string object to iterate through each element in the list/string.


# In[ ]:


get_ipython().set_next_input('13. Whats the difference between tuples and lists');get_ipython().run_line_magic('pinfo', 'lists')
13 ans)Tuples are immutable where as lists in Python are mutable. So once created, the items inside a tuple cannot be changed.


# In[ ]:


14. How do you type a tuple value that only contains the integer 42?
14 ans)


# In[33]:


#14 ans 
tup = tuple([32])
tup


# In[ ]:


get_ipython().set_next_input('15. How do you get a list values tuple form? How do you get a tuple values list form');get_ipython().run_line_magic('pinfo', 'form')
15 ans) 
          By using type casting

            b = tuple([42, 3, 5])
            type(b) # tuple
            c = list(b)
            type(c) # list


# In[34]:


#15 ans
b = tuple([42, 3, 5])
type(b)  # tuple
c = list(b)
type(c) # list


# In[ ]:


16. Variables that "contain" list values are not necessarily lists themselves. Instead, what do they
get_ipython().run_line_magic('pinfo', 'contain')
16 ans) They contain references to the list values


# In[ ]:


17. How do you distinguish between copy.copy() and copy.deepcopy()?
17 ans)

        -copy() returns a shallow copy of list and deepcopy() return a deep copy of list.
        -deepcopy: In case of deep copy, a copy of object is copied in other object. It means that any changes made to a copy of object do not reflect in the original object.
        -shallow copy: In case of shallow copy, a reference of object is copied in other object. It means that any changes made to a copy of object do reflect in the original object.
 


# In[ ]:





# In[ ]:




