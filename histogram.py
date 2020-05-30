#!/usr/bin/env python
# coding: utf-8

# In[13]:


#ROK ROZMAN
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
#%pylab inline
#matplotlib.rcParams['figure.figsize'] = [9,6]


# In[14]:


def RGB_hist(slika):
    # rgb histogram
    #print("RGB histogram")
    r = np.zeros(256).reshape(256,1)
    g = np.zeros(256).reshape(256,1)
    b = np.zeros(256).reshape(256,1)
    for i in range(0,slika.shape[1]):
        for j in range(0,slika.shape[0]):
            r[slika[j][i][0]] += 1
            g[slika[j][i][1]] += 1
            b[slika[j][i][2]] += 1
    x = np.column_stack((r,g,b))
    x = x.astype(int)
    #print(x)
    return x


# In[15]:


def GRAY_hist(slika):
    # gray histogram
    #print("GREY histogram")
    hist = np.zeros(256).reshape(256,1)
    for i in range(0,slika.shape[0]):
        for j in range(0,slika.shape[1]):
            hist[slika[i][j]] += 1
    x = hist.astype(int)
    #print(x)   
    return(x)


# In[18]:


if __name__ == '__main__':
    print("Modul za izdelavo histograma slike!")
    #I = pyplot.imread('slike/236969406_ecc45ed0f1.jpg')
    #I.show()
    #x = RGB_hist(I)
    #x = GRAY_hist(I)
    #print(x)
    
    # s ze narejeno funkcijo test
    #print("---------------------------")
    #image = Image.open("slike/236969406_ecc45ed0f1.jpg")
    #histogram = image.histogram()
    #image.show()
    #print(histogram)


# In[ ]:





# In[ ]:





# In[ ]:




