# In[1]:
import plotly
from plotly.offline import iplot
import plotly.graph_objs as go

# In[2]:
nutrients = ['Carbohydrates', 'Salt', 'Vitamin C', 'Niacin', 'Vitamin E',
             'Pantothenic acid', 'Vitamin B6', 'Riboflavin', 'Tiamin', 'Folic acid', 'Vitamin B12', 'other']
# In[3]:
nutrition_value = [88, 1.4, 0.213, 0.043, 0.032, 0.016,
                   0.0037, 0.0037, 0.0029, 0.000533, 0.000067, 10.259]
# In[4]:
trace = go.Pie(labels=nutrients, values=nutrition_value)

# In[5]:
data = [trace]

# In[6]:
fig = go.Figure(data=data)

# In[7]:
iplot(fig)

# In[8]:
cookie_nutrients = ['Fat', 'Carbohydrates', 'Proteins', 'Salt', 'Other']

# In[9]:
cookie_nutr_value = [27.1, 59.1, 5.9, 0.62, 7.28]

# In[10]:
trace = go.Pie(labels=cookie_nutrients, values=cookie_nutr_value)
# In[11]:
data = [trace]

# In[12]:
fig = go.Figure(data=data)

# In[13]:
iplot(fig)
