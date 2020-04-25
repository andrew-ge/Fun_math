#!/usr/bin/env python
# coding: utf-8

# In[11]:


digits =set([1,2,3,4,5,6,7,8,9])
for d1 in range(1,10):
    for d2 in range (1,10):
        for d3 in range (1,10):
            n1 = d1*10 + d2
            n2 = n1* d3
            if (n2 < 100):
                d4 = n2 //10
                d5 = n2 %10
                ulen = len(digits.intersection(set ([d1,d2,d3,d4,d5])) ) 
                if ( ulen == 5):
                    for d6 in range(1,10):
                        for d7 in range (1,10):
                            n3 = d6*10 +d7
                            n4 = n2 +n3
                            if (n4<100):
                                d8 = n4 // 10
                                d9 = n4 % 10
                                ulen  = len( digits.intersection(set([d1,d2,d3,d4,d5,d6,d7,d8,d9])) )
                                if (ulen ==9):
                                    print (d1,d2,d3,d4,d5,d6,d7,d8,d9)     


# In[12]:


digits.intersection(set([d1,d2,d3,d4,d5]))


# In[ ]:




