import plotly.express as px
import pandas as pd

animals = pd.DataFrame(
    {"Lieblingstier": ["Katze"] * 12 + ["Alpaka"] * 6 + ["Hund"] * 5 + ["Ente"] * 2}
)

fig = px.histogram(animals, x="Lieblingstier", template="plotly_white")

fig.update_layout(yaxis_title="Anzahl")
fig.update_traces(marker_color="black")
fig.show()
