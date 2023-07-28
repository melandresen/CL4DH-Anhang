import plotly.express as px
import pandas as pd

foodblog_data = pd.read_csv('resources/foodblog-data.csv', sep='\t')

fig = px.box(foodblog_data, y='median_sentence_length', points='all', template='plotly_white',
             labels={'median_sentence_length':'Mittlere Satzlänge (Median)'})
fig.update_traces(marker_color='black')

fig.show()