import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.graph_objs as go



data = pd.read_csv("bd.csv")
fig = plt.figure()
#axes = fig.add_axes([0.0, 0.0, 1.0, 1.0])
#bins = 20 #  количество столбцов
#index = np.arange(bins) # создаем список от 0 до bins - 1 
#axes.hist(data[data['country'] == 'United States']['release_year'].dropna(), bins=bins, alpha=0.6, label='сша') 
#axes.hist(data[data['country'] == 'Canada']['release_year'].dropna(), bins=bins, alpha=0.6, label='канада')
#axes.legend() # строим легенду
#axes.set_xlabel('год', fontsize=20) 
#axes.set_ylabel('страна', fontsize=20)


#plt.show()

#data[
#data['country'] == 'United States'
#].set_index('type')['release_year'].plot(
#kind='line',
#figsize=(12,8)
#)
#plt.show()

#data[data['country'] == 'United Kingdom'].set_index('type')['release_year'].plot(kind='line',figsize=(12,8))

count_year_df = data.groupby('release_year', as_index = False).show_id.count()

trace = go.Bar(
    x = count_year_df.release_year,
    y = count_year_df.show_id
)
layout = go.Layout(
    title='Фильмы на Disney',
)

fig = go.Figure(data = [trace], layout = layout)
iplot(fig)
