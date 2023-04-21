import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.graph_objs as go



disney = pd.read_csv("bd.csv")
fig = plt.figure()
disney = disney.iloc[:, 0:8]
disney = disney.sort_values(by=['release_year'])
print(disney)

def filter_disney(x):
        if x == 2021:
                return None
        if x!=2021:
                return x

disney['release_year'] = disney['release_year'].apply(filter_disney)

#disney = disney.sort_values(by=['show_id'])
disney.fillna(disney.interpolate(limit_direction='both'), inplace=True)
print(disney)


count_year_df = disney.groupby('release_year', as_index = False).show_id.count()

trace = go.Bar(
    x = count_year_df.release_year,
    y = count_year_df.show_id
)
layout = go.Layout(
    title='Фильмы на Disney',
)

fig = go.Figure(data = [trace], layout = layout)
iplot(fig)

