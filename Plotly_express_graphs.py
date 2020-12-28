import yfinance
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df_bist = yfinance.download("XU100.IS", start="2017-01-01", end="2018-01-01")
df_ftse = yfinance.download("^FTSE", start="2017-01-01", end="2018-01-01")

fig = make_subplots(rows=2, cols=2)
fig.add_trace(go.Bar(x=df_ftse.index, y=df_ftse["Open"], name="FTSE"), row=1, col=1)
fig.add_trace(go.Bar(x=df_bist.index, y =df_bist["Open"], name="BIST"), row=1, col=2)
fig.add_trace(go.Scatter(x=df_ftse.index, y=df_ftse["Open"], name="FTSE"), row=2, col=1)
fig.add_trace(go.Scatter(x=df_bist.index, y =df_bist["Open"], name="BIST"), row=2, col=2)
fig.show()