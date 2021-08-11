# In[1]:
import pandas as pd

# In[2]:
import seaborn as sns

# In[3]:
sns.set_theme(style="whitegrid")

# In[4]:
df = pd.read_csv(r'\Users\almas\Desktop\diamonds.csv')

# In[5]:
sns.kdeplot(
    data=df, x="carat", hue="cut",
    fill=True, common_norm=False, palette="plasma",
    alpha=.5, linewidth=0,
)

# In[6]:
sns.kdeplot(
    data=df, x="depth", hue="cut",
    fill=True, common_norm=False, palette="plasma",
    alpha=.5, linewidth=0,  # moze i alpha=0.5
)
