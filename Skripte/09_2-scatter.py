import plotly.express as px
import pandas as pd

foodblog_data = pd.read_csv("resources/foodblog-data.csv", sep="\t")

fig = px.scatter(
    foodblog_data,
    y="median_sentence_length",
    x="unknown_ratio",
    template="plotly_white",
    labels={
        "median_sentence_length": "Mittlere Satzlänge (Median)",
        "unknown_ratio": "Anteil unbekannter Wörter",
    },
)
fig.update_traces(marker_color="black")

fig.show()
