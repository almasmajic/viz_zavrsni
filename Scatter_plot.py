#!/usr/bin/env python
# coding: utf-8

# # Scatter plot (dijagram raspršenja)
# Graf će kao x-os koristiti Votes, a kao y-os Rates. Treća, kategorička varijabla je 'Viewers per Million'. Pregledi se broje u milijunima i odnose se samo na SAD.

# In[1]:
from matplotlib import pyplot as plt
import pandas as pd

# In[2]:
dataset = pd.read_csv(r'\Users\almas\Desktop\the_office_series.csv')

# In[3]:
dataset.head()

# In[4]:
dataset.tail()

# In[5]:

# In[6]:
plt.style.use('seaborn')

# In[7]:

view_count = dataset['Viewership']
rates = dataset['Ratings']
votes = dataset['Votes']

# In[8]:
plt.scatter(votes, rates, edgecolor='black', linewidth=1, alpha=0.75)
plt.title('The Office - TV Show; Ratings')

plt.xlabel('Votes')
plt.ylabel('Rates')

plt.tight_layout()

# In[9]:

plt.scatter(votes, rates, c=view_count, cmap='summer',
            edgecolor='black', linewidth=1, alpha=0.75)

cbar = plt.colorbar()
cbar.set_label('Views per Million')

plt.title('The Office - TV Show')

plt.xlabel('Votes')
plt.ylabel('Rates')

plt.tight_layout()

# In[12]:

plt.scatter(votes, rates, c=view_count, cmap='Blues',
            edgecolor='black', linewidth=1, alpha=0.75)

cbar = plt.colorbar()
cbar.set_label('Views per Million')

plt.title('The Office - TV Show')

plt.xlabel('Votes')
plt.ylabel('Rates')

plt.tight_layout()

# In[ ]:

# In[ ]:
