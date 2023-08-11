import plotly.express as px
import pandas as pd

duck_trend = pd.read_csv("resources/Google-Trends_Ente.csv")

fig = px.line(duck_trend, x="Monat", y="Ente", template="plotly_white")
fig.update_traces(line_color="black")


fig.show()
