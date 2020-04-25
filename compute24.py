#!/usr/bin/env python
# coding: utf-8

# In[27]:


import random
from itertools import permutations 
from math import sqrt

#
#input is two tuple items
#first item in tuple is existing operation string
#second item in tumple is the number need operation
#
def oprNum(a,b,op):
    if op =="+":
        rval = a[1]+b[1]
        rstr = "(" + a[0] + "+" + b[0] +  ")"
    elif op =='-':
        rval = a[1] - b[1]
        rstr = "(" + a[0] + "-" + b[0] +  ")"
    if op =="*":
        rval = a[1]*b[1]
        rstr = "(" + a[0] + "*" + b[0] +  ")"
    if op =="/":
        if b[1] == 0:
            rval = -sqrt(3) #this value will be no use
            rstr = "(" + a[0] + "/" + b[0] +  ")"
        else:
            rval = a[1]/b[1]
            rstr = "(" + a[0] + "/" + b[0] +  ")"
    return (rstr,rval)


#prepare the inputs
opList =['+','-','*','/']

random.seed(5)
curList=[]
curList.append([])
ds = [7,7,3,3]
for d in ds:
   # d = random.randint(1,13)
    curList[0].append((str(d),d))


print (len(curList), curList[0])


# In[28]:


for _ in range(3):
    newList=[]
    for clist in curList:
        perm = permutations(clist)
        for p in list(perm):
            for op in opList:
                t =oprNum(p[0],p[1],op)
                tl=[]
                tl.append(t)
                newList.append([t, *p[2:]])
    del curList
    curList = newList.copy()


# In[29]:


for item in curList:
    if item[0][1] ==24:
        print (item)


# In[ ]:





# In[ ]:




