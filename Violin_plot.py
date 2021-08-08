# In[1]:
import seaborn as sns

# In[2]:
sns.set_theme(style="whitegrid")

# In[3]:
penguins = sns.load_dataset("penguins")

# In[4]:
plot = sns.violinplot(x=penguins["flipper_length_mm"], palette="cool")

# In[5]:
plot = sns.violinplot(x="species", y="flipper_length_mm",
                      data=penguins, palette="cool")

# In[6]:
plot = sns.violinplot(x="species", y="flipper_length_mm", hue="sex",
                      data=penguins, palette="cool", split=True, scale="count")

# In[9]:
# ovaj ne radi due to Value error da hue moze imat samo 2 vrijednosti
plot = sns.violinplot(x="species", y="flipper_length_mm", hue="island",
                      data=penguins, palette="Set2", split=True,
                      scale="count")

# In[10]:
plot = sns.violinplot(x="island", y="body_mass_g", hue="sex", data=penguins,
                      palette="seismic", split=True, scale="count", inner="quartile")
