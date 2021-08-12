# In[1]:
import plotly

# In[2]:
from plotly.offline import iplot

# In[3]:
import plotly.graph_objs as go

# In[4]:
import numpy as np

# In[5]:
allergens = [
    "crkvina",
    "trave",
    "hrast",
    "borovi",
    "cempresi",
    "trputac",
    "pelin",
    "loboda"
]

# In[6]:
date = [
    "August 5th",
    "August 6th",
    "August 7th",
    "August 8th",
    "August 9th",
    "August 10th",
    "August 11th",
    "August 12th",
]
# In[7]:
pollen_concentration = np.array(
    [
        [5.8, 3.6, 1.3, 0.5, 0.4, 0.4, 0, 0],
        [6.0, 3.3, 1.5, 0.5, 0.5, 0.2, 0, 0],
        [6.1, 2.5, 0.9, 0.9, 0.5, 0.6, 0, 0],
        [6.2, 3.8, 1.6, 1.0, 0.9, 0.4, 0, 0],
        [4.8, 2.1, 1.2, 1.0, 0.7, 0.2, 0, 0],
        [3.9, 2.5, 1.0, 1.0, 0, 0, 0.6, 0.6],
        [3.9, 2.5, 1.0, 1.0, 0, 0, 0.6, 0.4],
        [4.4, 3.0, 0.6, 1.5, 0, 0, 0.4, 0.8]
    ]
)

# In[8]:
trace = go.Heatmap(
    x=allergens,
    y=date,
    z=pollen_concentration,
    type='heatmap',
    colorscale='greens'
)

# In[9]:
data = [trace]

# In[10]:
fig = go.Figure(data=data)

# In[11]:
iplot(fig)
