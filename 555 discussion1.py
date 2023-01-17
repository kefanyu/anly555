#!/usr/bin/env python
# coding: utf-8

# In[32]:


def computePi4(numTerms):
    
    pi_four = 0  # the initial value for pi_four
    k = 1  # the denominator for the factors in the summation
    
    for i in range(1, numTerms+1):
        
        if i % 2 != 0:  # if it is an odd term
            
            pi_four += 1/k   # add 1/k e.g. 1, 1/5, ...
        
        else:  # if it is an even term
            pi_four -= 1/k  # minus 1/k e.g. 1/3, 1/7, ...
            
        k+=2  # increment k by 2 since it is always odd
        
    return(pi_four)


# In[33]:


computePi4(1000)  # it is approximately pi/4


# In[34]:


def computePi4(numTerms):
    
    # using comprehension syntax. In this case, i would be the odd number similar as k in the precious function and (i-1)/2)+1 would be the integer
    pi_four = sum(1/i if (((i-1)/2)+1)%2 != 0 else -1/i for i in range(1,numTerms,2))
        
    return(pi_four)


# In[35]:


computePi4(1000)


# In[36]:


def computePi4(numTerms):
    
    pi_four = 0
    
    k = 1
    
    for i in range(1, numTerms+1):
        
        if i % 2 != 0:
            pi_four += 1/k
            
            # using yield statement to store the value of pi/4
            yield pi_four
        
        else:
            pi_four -= 1/k
            
            # similar approach here
            yield pi_four
            
        k+=2


# In[37]:


for n in computePi4(1000):
    print(n, end=" ")

