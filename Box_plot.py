# In[1]:
import pandas as pd

# In[2]:
import seaborn as sns

# In[3]:
sns.set_theme(style="whitegrid")

# In[4]:
df = pd.read_csv(r'\Users\almas\Desktop\netflix_titles.csv')

# In[5]:
sns.boxplot(x=df["No_of_Episodes"])

# In[8]:
# failed
box_plot = sns.boxplot(x="Genre", y="No_of_Episodes", data=df)

# In[9]:
box_plot = sns.boxplot(x="No_of_Episodes", y="Genre", data=df)

# In[10]:
box_plot = sns.boxplot(x="No_of_Episodes", y="Genre",
                       hue="Watched", data=df, palette="Set1")
