#!/usr/bin/env python
# coding: utf-8

# In[ ]:


list_of_num = [2,5,4,8]
def sqaure(num):
    return num**2
x = list(map(sqaure, list_of_num))
print(x) 

