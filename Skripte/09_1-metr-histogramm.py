import plotly.express as px
import pandas as pd

foodblog_data = pd.read_csv("resources/foodblog-data.csv", sep="\t")

fig = px.histogram(
    foodblog_data,
    x="median_sentence_length",
    template="plotly_white",
    labels={"median_sentence_length": "Mittlere Satzlänge (Median)"},
)
fig.update_layout(yaxis_title="Anzahl")

fig.update_traces(marker_color="black")
fig.show()
