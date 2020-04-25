#!/usr/bin/env python
# coding: utf-8

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


curList=[]
curList.append([])
ds = [1,6,6,8]
for d in ds:
   # d = random.randint(1,13)
    curList[0].append((str(d),d))


print (len(curList), curList[0])


for _ in range(3):
    newList=[]
    print("Length of the list is", len(curList))
    for clist in curList:
        
        perm = permutations(clist,2)
        for p in list(perm):
            for op in opList:
                cclist=clist.copy()
                t =oprNum(p[0],p[1],op) 
                cclist.remove(p[0])
                cclist.remove(p[1])
                newList.append([t, *cclist])
    del curList
    curList = newList.copy()


# In[29]:

print(len(curList))
for item in curList:
    if item[0][1] ==24:
        print (item)
