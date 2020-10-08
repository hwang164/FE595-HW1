#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-np.pi,np.pi,1024)
s=np.sin(x)
c=np.cos(x)
plt.plot(x,s)
plt.plot(x,c)
plt.show()


# In[ ]:




