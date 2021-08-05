#!/usr/bin/env python
# coding: utf-8

# # Swarm plot
# Prikaz odnosa tipa/vrste Pokemona i 'Attack' svojstva + odnos tip/vrsta Pokemona u ovinosti o 'Defensive' svojstvu.

# In[1]:
import pandas as pd

# In[2]:
from matplotlib import pyplot as plt

# In[3]:
import seaborn as sns

# In[4]:
df = pd.read_csv(r'\Users\almas\Desktop\pokemons.csv')

# In[5]:
df.head()

# In[6]:
sns.lmplot(x='Attack', y='Defense', data=df)

# In[7]:
sns.lmplot(x='HP', y='Speed', data=df)

# In[9]:

pokemon_type_colors = ['#78C850',  # Grass
                       '#F08030',  # Fire
                       '#6890F0',  # Water
                       '#A8B820',  # Bug
                       '#A8A878',  # Normal
                       '#A040A0',  # Poison
                       '#F8D030',  # Electric
                       '#E0C068',  # Ground
                       '#EE99AC',  # Fairy
                       '#C03028',  # Fighting
                       '#F85888',  # Psychic
                       '#B8A038',  # Rock
                       '#705898',  # Ghost
                       '#98D8D8',  # Ice
                       '#7038F8',  # Dragon
                       ]

# In[10]:

plt.figure(figsize=(20, 5))
sns.swarmplot(x='Type 1', y='Attack', data=df, palette=pokemon_type_colors)

# In[11]:
plt.figure(figsize=(25, 5))
sns.swarmplot(x='Type 1', y='Defense', data=df, palette=pokemon_type_colors)

# In[ ]:

# In[ ]:
