#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n=int(input())
for i in range(2**n):
    line = [i//2**j%2 for j in reversed(range(n))]
    print(line)


# In[ ]:





# In[ ]:




