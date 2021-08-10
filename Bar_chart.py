# In[1]:
import pandas as pd

# In[2]:
import numpy as np

# In[3]:
import matplotlib.pyplot as plt

# In[4]:
import plotly.graph_objs as go

# In[5]:
from plotly.offline import iplot
# In[6]:
import seaborn as sns
# In[7]:
df = pd.read_csv(r'\Users\almas\Desktop\Tokyo Medals 2021.csv')
# In[8]:
winner = df.sort_values(by="Rank By Total", ascending=True)[:16]
# In[9]:
winner
# In[10]:
trace1 = go.Bar(
    x=winner['Country'],
    y=winner['Gold Medal'],
    name='Zlato',
    marker=dict(color='#FFD700')
)
trace2 = go.Bar(
    x=winner['Country'],
    y=winner['Silver Medal'],
    name='Srebro',
    marker=dict(color='#9EA0A1')
)
trace3 = go.Bar(
    x=winner['Country'],
    y=winner['Bronze Medal'],
    name='Bronca',
    marker=dict(color='#CD7F32')
)
data = [trace3, trace2, trace1]
layout = go.Layout(
    title='Medalje po zemljama 2021. - top 15', barmode='stack'
)
fig = go.Figure(data=data, layout=layout)
iplot(fig)
