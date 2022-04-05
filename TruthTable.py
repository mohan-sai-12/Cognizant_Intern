#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n=int(input("Enter Size of Truth Table :"))
for i in range(2**n):
    row = [i//2**j%2 for j in reversed(range(n))]
    print(row)


# In[ ]:





# In[ ]:




