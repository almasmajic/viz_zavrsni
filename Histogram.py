# In[1]:
import pandas as pd

# In[2]:
import matplotlib.pyplot as plt

# In[3]:
df = pd.read_csv(r'\Users\almas\Desktop\netflix_titles.csv')

# In[4]:
plt.hist(df['No_of_Seasons'], edgecolor='black', color='#409caf')
plt.title('Number of series seasons')
plt.xlabel('Seasons')
plt.ylabel('Frequency')

# In[5]:
plt.hist(df['No_of_Episodes'], edgecolor='black', color='#c9fff3')
plt.title('Number of series episodes')
plt.xlabel('Episodes')
plt.ylabel('Frequency')

# In[ ]: