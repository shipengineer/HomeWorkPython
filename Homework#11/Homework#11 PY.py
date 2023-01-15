#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sympy as sp


# In[3]:


x = sp.Symbol('x')
expr = sp.sin(x)**2-sp.cos(x)**2
expr
# введение уравнения


# In[4]:


expr_solve = sp.solve(expr) 
expr_solve
# нахождение корней


# In[5]:


expr_diff = sp.diff(expr)
expr_diff
# Нахождение производной


# In[6]:


graph = sp.plot(expr)
# построение граффика


# In[7]:


rise_exp = sp.solve(expr_diff>0)
rise_exp
# возрастание функции


# In[8]:


fall_exp = sp.solve(expr_diff<0)
fall_exp
# убывание функции


# In[9]:


peak_exp = sp.solve(expr_diff)
peak_exp
#экстремумы


# In[10]:


rise_exp_origin = sp.solve(expr>0)
rise_exp_origin
# промежутки роста


# In[11]:


fall_exp_origin = sp.solve(expr<0)
fall_exp_origin 
# промежутки падения


# In[ ]:




